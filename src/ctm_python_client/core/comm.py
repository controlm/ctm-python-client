import abc
import typing
import json
from unittest import result
import attrs
import enum

from clients import ctm_api_client, ctm_saas_client
from ctm_python_client.core.credential import AbstractCredentials, SimpleCredentials

import urllib3

from clients.ctm_api_client.rest import ApiException
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

__all__ = ['AbstractAAPIClient', 'AAPIClientResponse',
           'OnPremAAPIClient', 'SaasAAPIClient', 'EnvironmentMode', 'Environment']


class AAPIClientResponse:

    def __init__(self, success: bool, result: typing.Any = None, errors: typing.List[typing.Any] = None) -> None:
        self.success = success
        self.result = result
        self.errors = errors

    def is_ok(self):
        return self.success


def sanitize_output(apirequest):
    def wrap(*args, **kwargs):
        try:
            res = apirequest(*args, **kwargs)
            return AAPIClientResponse(True, res)
        except Exception as e:
            errors = [err.get('message', '') + ' ' + err.get('item', '')
                      for err in json.loads(e.body)['errors']]
            return AAPIClientResponse(False, None, errors)

    return wrap


class AbstractAAPIClient(abc.ABC):

    @abc.abstractclassmethod
    def authenticate(self):
        pass


class OnPremAAPIClient(AbstractAAPIClient):

    def __init__(self, endpoint: str, credentials: AbstractCredentials) -> None:
        super().__init__()

        self.endpoint = endpoint
        self.credentials = credentials

        self.configuration = ctm_api_client.Configuration()
        self.configuration.host = self.endpoint
        self.configuration.verify_ssl = False
        self.configuration.api_key_prefix['Authorization'] = 'Bearer'

        self.apiclient = ctm_api_client.ApiClient(self.configuration)

        # apis
        self.session_api = ctm_api_client.SessionApi(self.apiclient)
        self.config_api = ctm_api_client.ConfigApi(self.apiclient)
        self.build_api = ctm_api_client.BuildApi(self.apiclient)
        self.deploy_api = ctm_api_client.DeployApi(self.apiclient)
        self.run_api = ctm_api_client.RunApi(self.apiclient)

        # self.authenticate()

    def authenticate(self):
        self.apiclient.configuration.host = self.endpoint
        self.apiclient.configuration.verify_ssl = False
        self.apiclient.configuration.api_key_prefix['Authorization'] = 'Bearer'

        token = self.session_api.do_login(
            {
                'username': self.credentials.get_username(),
                'password': self.credentials.get_password()
            }
        ).token
        self.apiclient.configuration.api_key['Authorization'] = token


class SaasAAPIClient(AbstractAAPIClient):

    def __init__(self, endpoint: str, credentials: AbstractCredentials) -> None:
        super().__init__()

        self.endpoint = endpoint
        self.credentials = credentials

        self.configuration = ctm_saas_client.Configuration()
        self.configuration.host = self.endpoint
        self.configuration.verify_ssl = False
        self.configuration.api_key['x-api-key'] = self.credentials.get_password()

        self.apiclient = ctm_saas_client.ApiClient(self.configuration)

        # apis
        self.config_api = ctm_saas_client.ConfigApi(self.apiclient)
        self.build_api = ctm_saas_client.BuildApi(self.apiclient)
        self.deploy_api = ctm_saas_client.DeployApi(self.apiclient)
        self.run_api = ctm_saas_client.RunApi(self.apiclient)

        self.authenticate()

    def authenticate(self):

        self.apiclient.configuration.host = self.endpoint
        self.apiclient.configuration.verify_ssl = False
        self.apiclient.configuration.api_key['x-api-key'] = self.credentials.get_password()


class EnvironmentMode(enum.Enum):
    ONPREM = 'Control-M'
    WORKBENCH = 'Control-M Workbench'
    SAAS = 'Control-M Helix'


class Environment:

    @staticmethod
    def create_workbench(host: str = 'localhost', port: str = '8443'):
        return Environment(f'https://{host}:{port}/automation-api', 'workbench', 'workbench', mode=EnvironmentMode.WORKBENCH)

    @staticmethod
    def create_onprem(host: str, port: str = '8443',  username: str = None, password: str = None, credentials: AbstractCredentials = None):
        return Environment(f'https://{host}:{port}/automation-api', username=username, password=password, credentials=credentials, mode=EnvironmentMode.ONPREM)

    @staticmethod
    def create_saas(endpoint: str, api_key: str = None, credentials: AbstractCredentials = None):
        return Environment(endpoint=endpoint, api_key=api_key, credentials=credentials, mode=EnvironmentMode.SAAS)

    def __init__(self, endpoint: str, username: str = None, password: str = None, api_key: str = None, credentials: AbstractCredentials = None, mode: EnvironmentMode = None) -> None:
        self.endpoint = endpoint
        self.credentials = credentials
        self.mode = mode

        self._validate_input(username, password, api_key, credentials, mode)

    def _validate_input(self, username: str = None,  password: str = None, api_key: str = None, credentials: AbstractCredentials = None, mode: EnvironmentMode = None):
        if mode is None:
            if credentials is not None:
                raise Exception(
                    'Please define EnvironmentMode when working with Credentials object')
            else:
                if api_key and (password or username):
                    raise Exception(
                        'Cannot define api_key and password or username')

                if api_key is None and username is None and password is None:
                    raise Exception(
                        'api_key or (username + password) needs to be defined')

                if username and not password:
                    raise Exception('Cannot define username without password')

                if password and not username:
                    raise Exception('Cannot define password without username')

                if api_key:
                    self.mode = EnvironmentMode.SAAS
                    self.credentials = SimpleCredentials('', api_key)

                else:
                    self.mode = EnvironmentMode.ONPREM
                    self.credentials = SimpleCredentials(
                        username=username, password=password)

        else:
            # TO DO : Validate
            if credentials is None:
                if mode == EnvironmentMode.SAAS:
                    self.credentials = SimpleCredentials('', api_key)
                else:
                    self.credentials = SimpleCredentials(username, password)
