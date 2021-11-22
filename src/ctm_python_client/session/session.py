from clients import ctm_api_client, ctm_saas_client

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Session:
    def __init__(self, endpoint=None, username=None, password=None, api_key=None):
        self.endpoint = endpoint
        self.username = username
        self.password = password
        self.api_key = api_key
        



        if password:
            self.configuration = ctm_api_client.Configuration()
            self.configuration.host = endpoint
            self.configuration.verify_ssl = False
            self.configuration.api_key_prefix["Authorization"] = "Bearer"
            self.configuration.api_key["Authorization"] = self.get_token()

            self.api_client = ctm_api_client.ApiClient(self.configuration)

            self.deploy_api = ctm_api_client.DeployApi(self.api_client)
            self.run_api = ctm_api_client.RunApi(self.api_client)

            self.saas = False

        else:         
            self.configuration = ctm_saas_client.Configuration()
            self.configuration.host = endpoint
            self.configuration.verify_ssl = False
            self.configuration.api_key['x-api-key'] = api_key


            self.api_client = ctm_saas_client.ApiClient(self.configuration)

            self.deploy_api = ctm_saas_client.DeployApi(self.api_client)
            self.run_api = ctm_saas_client.RunApi(self.api_client)

            self.saas = True

    def login(self):
        api_session = ctm_api_client.SessionApi(
            ctm_api_client.ApiClient(self.configuration)
        )
        res = api_session.do_login(
            {"username": self.username, "password": self.password}
        )

        return res

    def get_token(self):
        return self.login().token

    def format_endpoint(self):
        shorted = self.endpoint[:-len("/automation-api")]        

        parts = shorted.split('.')
        parts[0] = parts[0].replace('-aapi','')

        return '.'.join(parts)
