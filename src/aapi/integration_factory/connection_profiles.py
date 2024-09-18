
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class ConnectionProfileGCPBatch(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:GCP Batch', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:GCP Batch'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    identity_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Identity Type'})
    batch_url: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Batch URL'})
    service_account_key: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Service Account Key'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAwsDynamoDB(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS DynamoDB', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS DynamoDB'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    aws_dynamo_db_url: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AWS DynamoDB URL'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    aws_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Access Key'})
    aws_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Secret'})
    iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IAM Role'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAwsMainframeModernization(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS Mainframe Modernization', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS Mainframe Modernization'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    mainframe_modernization_url: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Mainframe Modernization URL'})
    aws_logs_url: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Logs URL'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    aws_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Access key'})
    aws_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Secret'})
    iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IAM Role'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAzureDevOps(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Azure DevOps', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Azure DevOps'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    azure_dev_ops_url: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Azure DevOps URL'})
    organization_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Organization ID'})
    azure_username: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Azure Username'})
    azure_devops_token: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Azure Devops Token'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileGCPDeploymentManager(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:GCP Deployment Manager', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:GCP Deployment Manager'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    identity_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Identity Type'})
    deployment_manager_url: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Deployment Manager URL'})
    service_account_key: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Service Account Key'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileControlMReports(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:ControlM Reports', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:ControlM Reports'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    control_m_hostname: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Control-M Hostname'})
    control_m_port: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Control-M Port'})
    authentication_method: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Authentication Method'})
    api_token: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'API Token'})
    username: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Username'})
    password: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Password'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileWebServicesREST(ConnectionProfile):

    @attrs.define
    class WebServiceAuthenticationBasic(AAPIObject):

        user: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'User'})
        use_preemptive_auth: bool = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'UsePreemptiveAuth'})
        password: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Password'})

    @attrs.define
    class WebServiceAuthenticationOauth2(AAPIObject):

        @attrs.define
        class BasicAuthentication(AAPIObject):

            user: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'User'})
            password: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Password'})

        @attrs.define
        class GrantTypePassword(AAPIObject):

            user: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'User'})
            password: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Password'})

        basic_authentication: BasicAuthentication = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'BasicAuthentication'})
        api_url: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'ApiUrl'})
        grant_type_password: GrantTypePassword = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'GrantTypePassword'})
        client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'ClientId'})
        client_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'ClientSecret'})
        content_type: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ContentType'})
        headers: typing.List[str] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'Headers'})
        body: typing.List[str] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'Body'})

    @attrs.define
    class WebServiceAuthenticationAws(AAPIObject):

        @attrs.define
        class AuthMethodAccessAndSecretKeys(AAPIObject):

            access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AccessKey'})
            secret_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'SecretAccessKey'})

        @attrs.define
        class AuthMethodIAMRole(AAPIObject):

            iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'IAMRole'})

        region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Region'})
        custom_service_name: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'CustomServiceName'})
        auth_method_access_and_secret_keys: AuthMethodAccessAndSecretKeys = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'AuthMethodAccessAndSecretKeys'})
        auth_method_iam_role: AuthMethodIAMRole = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'AuthMethodIAMRole'})

    @attrs.define
    class WebServiceAuthenticationGoogle(AAPIObject):

        class TokenType(enum.Enum):

            Access = "Access"
            Identity = "Identity"

        token_type: TokenType = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'TokenType'})
        service_account_key: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'ServiceAccountKey'})

    _type: str = attrs.field(init=False, default='ConnectionProfile:Web Services REST', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Web Services REST'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    web_service_authentication_basic: WebServiceAuthenticationBasic = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'WebServiceAuthenticationBasic'})
    web_service_authentication_oauth2: WebServiceAuthenticationOauth2 = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'WebServiceAuthenticationOauth2'})
    web_service_authentication_aws: WebServiceAuthenticationAws = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'WebServiceAuthenticationAws'})
    web_service_authentication_google: WebServiceAuthenticationGoogle = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'WebServiceAuthenticationGoogle'})


@attrs.define
class ConnectionProfileAwsEC2(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS EC2', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS EC2'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    ec2_region: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'EC2 Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    aws_access_key_id: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AWS Access key ID'})
    aws_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Secret'})
    iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IAM Role'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection timeout'})


@attrs.define
class ConnectionProfileTalendOAuth(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Talend OAuth', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Talend OAuth'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    talend_api_url: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Talend API URL'})
    region: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Region'})
    client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Client ID'})
    client_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Client Secret'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAwsBackup(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS Backup', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS Backup'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    aws_backup_url: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AWS Backup URL'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    aws_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Access Key'})
    aws_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Secret'})
    iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IAM Role'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAzureHDInsight(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Azure HDInsight', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Azure HDInsight'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    cluster_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Cluster Name'})
    cluster_username: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Cluster Username'})
    cluster_password: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Cluster Password'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAwsQuickSight(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS QuickSight', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS QuickSight'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    aws_quick_sight_url: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AWS QuickSight URL'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Region'})
    aws_account_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Account ID'})
    authentication_method: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Authentication Method'})
    aws_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Access Key'})
    aws_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Secret'})
    iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IAM Role'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAirbyte(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Airbyte', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Airbyte'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    airbyte_base_url: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Airbyte Base URL'})
    api_key: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'API Key'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileGCPVM(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:GCP VM', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:GCP VM'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    identity_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Identity Type'})
    gcp_api_url: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'GCP API URL'})
    service_account_key: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Service Account Key'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection timeout'})


@attrs.define
class ConnectionProfileAwsSageMaker(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS SageMaker', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS SageMaker'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    sage_maker_url: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'SageMaker URL'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    aws_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Access key'})
    aws_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Secret'})
    iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IAM Role'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileGCPDataFusion(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:GCP Data Fusion', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:GCP Data Fusion'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    gcp_data_fusion_url: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'GCP Data Fusion URL'})
    identity_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Identity Type'})
    service_account_key: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Service Account Key'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileKubernetes(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Kubernetes', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Kubernetes'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    namespace: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Namespace'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})
    kubernetes_cluster_url: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Kubernetes Cluster URL'})
    service_token_file: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Service Token File'})


@attrs.define
class ConnectionProfileAwsSNS(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS SNS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS SNS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    aws_sns_url: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AWS SNS URL'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Region'})
    aws_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Access Key'})
    aws_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Secret'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAwsLambda(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS Lambda', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS Lambda'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    lambda_url: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Lambda URL'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    aws_access_key_id: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AWS Access key ID'})
    aws_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Secret'})
    iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IAM Role'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileUIPath(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:UI Path', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:UI Path'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    tenant_name: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Tenant Name'})
    tenant_url: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Tenant Url'})
    app_id: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'App ID'})
    app_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'App Secret'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAlteryxTrifacta(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Alteryx Trifacta', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Alteryx Trifacta'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    trifacta_url: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Trifacta URL'})
    username: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Username'})
    password: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Password'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAwsSQS(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS SQS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS SQS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    aws_sqs_url: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AWS SQS URL'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Region'})
    aws_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Access Key'})
    aws_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Secret'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileSnowflakeIdP(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Snowflake IdP', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Snowflake IdP'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    account_identifier: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Account Identifier'})
    region: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Region'})
    client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Client ID'})
    client_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Client Secret'})
    idp_url: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'IDP URL'})
    scope: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Scope'})


@attrs.define
class ConnectionProfileGCPDataprep(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:GCP Dataprep', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:GCP Dataprep'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    gcp_dataprep_url: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'GCP Dataprep URL'})
    user_access_token: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'User Access Token'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAwsGlue(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS Glue', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS Glue'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    glue_url: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Glue url'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    aws_access_key_id: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AWS Access key ID'})
    aws_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Secret'})
    iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IAM Role'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAwsGlueDataBrew(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS Glue DataBrew', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS Glue DataBrew'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    aws_api_base_url: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AWS API Base URL'})
    aws_logs_url: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Logs URL'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    aws_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Access Key'})
    aws_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Secret'})
    iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IAM Role'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAwsCloudFormation(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS CloudFormation', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS CloudFormation'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    cloud_formation_url: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'CloudFormation URL'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    aws_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Access key'})
    aws_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Secret'})
    iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IAM Role'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAzureFunctions(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Azure Functions', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Azure Functions'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    subscription_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Subscription ID'})
    identity_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Identity Type'})
    specify_managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'Specify Managed Identity Client ID'})
    managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Managed Identity Client ID'})
    tenant_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tenant ID'})
    resource_group: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Resource Group'})
    application_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Application ID'})
    client_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Client Secret'})
    azure_login_url: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Azure Login url'})
    function_app_web_site: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Function App Web Site'})
    custom_app_key: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Custom App Key'})


@attrs.define
class ConnectionProfileAzureBatchAccounts(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Azure Batch Accounts', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Azure Batch Accounts'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    azure_ad_url: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Azure AD url'})
    authentication_method: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Authentication Method'})
    specify_managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'Specify Managed Identity Client ID'})
    managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Managed Identity Client ID'})
    tenant_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tenant ID'})
    app_id: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'App ID'})
    client_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Client Secret'})
    batch_resource_url: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Batch Resource url'})
    batch_account_name: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Batch Account Name'})
    batch_region_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Batch Region ID'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileDatabricks(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Databricks', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Databricks'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    databricks_workspace_url: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Databricks workspace url'})
    databricks_personal_access_token: str = attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'Databricks personal access token'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAwsEMR(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS EMR', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS EMR'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    aws_base_url: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Base URL'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    aws_access_key_id: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AWS Access Key ID'})
    aws_secret_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AWS Secret Access Key'})
    iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IAM Role'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileTableau(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Tableau', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Tableau'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    tableau_url: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Tableau URL'})
    token_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Token Name'})
    token_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Token Secret'})
    site_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Site Name'})
    api_version: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'API Version'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection timeout'})


@attrs.define
class ConnectionProfileAzureVM(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Azure VM', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Azure VM'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    subscription_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Subscription ID'})
    authentication_method: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Authentication Method'})
    specify_managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'Specify Managed Identity Client ID'})
    managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Managed Identity Client ID'})
    resource_group: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Resource Group'})
    tenant_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tenant ID'})
    application_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Application ID'})
    client_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Client Secret'})
    azure_login_url: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Azure Login url'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection timeout'})


@attrs.define
class ConnectionProfileGCPComposer(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:GCP Composer', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:GCP Composer'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    composer_url: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Composer URL'})
    identity_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Identity Type'})
    service_account_key: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Service Account Key'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileGCPDataplex(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:GCP Dataplex', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:GCP Dataplex'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    identity_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Identity Type'})
    gcp_dataplex_url: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'GCP Dataplex URL'})
    service_account_key: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Service Account Key'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection timeout'})


@attrs.define
class ConnectionProfileDBT(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:DBT', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:DBT'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    dbt_url: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'DBT URL'})
    dbt_token: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'DBT Token'})
    account_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Account ID'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAwsAthena(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS Athena', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS Athena'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    aws_base_url: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Base URL'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    aws_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Access Key'})
    aws_secret_key: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Secret Key'})
    iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IAM Role'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileApacheNiFi(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Apache NiFi', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Apache NiFi'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    ni_fi_url: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'NiFi URL'})
    port: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Port'})
    username: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Username'})
    password: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Password'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAwsBatch(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS Batch', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS Batch'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    batch_url: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Batch URL'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    aws_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Access Key'})
    aws_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Secret'})
    iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IAM Role'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileGCPWorkflows(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:GCP Workflows', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:GCP Workflows'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    identity_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Identity Type'})
    gcp_api_url: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'GCP API URL'})
    service_account_key: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Service Account Key'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileGCPDataflow(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:GCP Dataflow', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:GCP Dataflow'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    identity_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Identity Type'})
    data_flow_url: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'DataFlow URL'})
    service_account_key: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Service Account Key'})


@attrs.define
class ConnectionProfileGCPBigQuery(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:GCP BigQuery', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:GCP BigQuery'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    identity_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Identity Type'})
    gcp_big_query_url: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'GCP BigQuery URL'})
    service_account_key: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Service Account Key'})


@attrs.define
class ConnectionProfileTalendDataManagement(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Talend Data Management', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Talend Data Management'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    api_url: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'API URL'})
    personal_access_token_authorization: str = attrs.field(kw_only=True, default=None, metadata={
                                                           '_aapi_repr_': 'Personal access token authorization'})
    region: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Region'})


@attrs.define
class ConnectionProfileGCPDataproc(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:GCP Dataproc', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:GCP Dataproc'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    identity_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Identity Type'})
    dataproc_url: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Dataproc URL'})
    service_account_key_json_format: str = attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'Service Account Key (JSON Format)'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection timeout'})


@attrs.define
class ConnectionProfileAzureSynapse(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Azure Synapse', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Azure Synapse'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    azure_ad_url: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Azure AD url'})
    authentication_method: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Authentication Method'})
    specify_managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'Specify Managed Identity Client ID'})
    managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Managed Identity Client ID'})
    tenant_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tenant ID'})
    app_id: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'App ID'})
    client_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Client Secret'})
    synapse_resource: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Synapse Resource'})
    synapse_url: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Synapse url'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileMicroFocusLinux(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Micro Focus Linux', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Micro Focus Linux'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    mfbsi_directory_path: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'MFBSI Directory Path'})
    mfbsi_config_path: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'MFBSI Config Path'})
    runtime_environment: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Runtime Environment'})
    additional_micro_focus_settings_script: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Additional Micro Focus Settings Script'})
    run_as: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Run As'})
    run_as_pass: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'RunAs-Pass'})


@attrs.define
class ConnectionProfileCommunicationSuite(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Communication Suite', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Communication Suite'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    microsoft_teams_webhook_url: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Microsoft Teams Webhook URL'})
    slack_webhook_url: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Slack Webhook URL'})
    telegram_url: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Telegram URL'})
    telegram_bot_token: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Telegram Bot Token'})
    telegram_chat_id: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Telegram Chat ID'})
    whats_app_url: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'WhatsApp URL'})
    whats_app_business_id: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'WhatsApp Business ID'})
    phone_number_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Phone Number ID'})
    recipient_phone_number: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Recipient Phone Number'})
    user_access_token: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'User Access Token'})
    version: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Version'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAzureResourceManager(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Azure Resource Manager', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Azure Resource Manager'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    azure_login_url: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Azure Login URL'})
    azure_base_url: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Azure Base URL'})
    subscription_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Subscription ID'})
    authentication_method: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Authentication Method'})
    specify_managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'Specify Managed Identity Client ID'})
    managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Managed Identity Client ID'})
    tenant_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tenant ID'})
    app_id: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'App ID'})
    client_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Client Secret'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAzureMachineLearning(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Azure Machine Learning', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Azure Machine Learning'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    azure_login_url: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Azure Login URL'})
    azure_management_url: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Azure Management URL'})
    azure_m_l_url: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Azure ML URL'})
    location_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Location Name'})
    subscription_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Subscription ID'})
    authentication_method: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Authentication Method'})
    specify_managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'Specify Managed Identity Client ID'})
    managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Managed Identity Client ID'})
    tenant_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tenant ID'})
    application_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Application ID'})
    client_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Client Secret'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAzureDataFactory(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Azure Data Factory', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Azure Data Factory'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    subscription_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Subscription ID'})
    identity_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Identity Type'})
    specify_managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'Specify Managed Identity Client ID'})
    managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Managed Identity Client ID'})
    tenant_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tenant ID'})
    application_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Application ID'})
    client_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Client Secret'})
    rest_login_url: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'REST Login url'})
    management_url: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Management url'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileOCIDataFlow(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:OCI Data Flow', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:OCI Data Flow'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    oci_data_flow_url: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'OCI Data Flow URL'})
    oci_region: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'OCI Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    user_ocid: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'User OCID'})
    tenancy_ocid: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Tenancy OCID'})
    fingerprint: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Fingerprint'})
    private_key: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Private Key'})
    config_file_path: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Config File Path'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAwsStepFunctions(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS Step Functions', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS Step Functions'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    step_functions_url: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Step Functions URL'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    aws_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Access Key'})
    aws_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Secret'})
    iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IAM Role'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileInformaticaCS(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Informatica CS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Informatica CS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    login_url: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Login URL'})
    base_url: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Base URL'})
    username: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Username'})
    password: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Password'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileWebServicesSOAP(ConnectionProfile):

    @attrs.define
    class WebServiceAuthenticationBasic(AAPIObject):

        user: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'User'})
        use_preemptive_auth: bool = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'UsePreemptiveAuth'})
        password: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Password'})

    _type: str = attrs.field(init=False, default='ConnectionProfile:Web Services SOAP', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Web Services SOAP'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    web_service_authentication_basic: WebServiceAuthenticationBasic = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'WebServiceAuthenticationBasic'})


@attrs.define
class ConnectionProfileOCIDataScience(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:OCI Data Science', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:OCI Data Science'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    oci_instances_url: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'OCI Instances URL'})
    oci_region: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'OCI Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    user_ocid: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'User OCID'})
    tenancy_ocid: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Tenancy OCID'})
    fingerprint: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Fingerprint'})
    private_key: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Private Key'})
    config_file_path: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Config File Path'})
    profile: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Profile'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileBoomiAtomsphere(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Boomi Atomsphere', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Boomi Atomsphere'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    api_username: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'API Username'})
    api_token: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'API Token'})
    end_point: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'End Point'})
    account_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AccountId'})


@attrs.define
class ConnectionProfileAzureDatabricks(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Azure Databricks', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Azure Databricks'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    tenant_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tenant ID'})
    application_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Application ID'})
    client_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Client Secret'})
    azure_login_url: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Azure Login url'})
    databricks_url: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Databricks url'})
    databricks_resource: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Databricks Resource'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileTerraform(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Terraform', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Terraform'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    terraform_org_name: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Terraform Org Name'})
    token: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Token'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAwsECS(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS ECS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS ECS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    aws_ecs_url: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AWS ECS URL'})
    cloud_watch_url: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Cloud Watch URL'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Region'})
    authentication_method: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Authentication Method'})
    aws_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Access Key'})
    aws_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Secret'})
    aws_iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS IAM Role'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAutomationAnywhere(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Automation Anywhere', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Automation Anywhere'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    host: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Host'})
    user_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'User Name'})
    password: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Password'})


@attrs.define
class ConnectionProfileGCPFunctions(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:GCP Functions', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:GCP Functions'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    identity_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Identity Type'})
    gcp_api_url: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'GCP API URL'})
    service_account_key: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Service Account Key'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAzureLogicApps(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Azure Logic Apps', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Azure Logic Apps'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    subscription_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Subscription ID'})
    authentication_method: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Authentication Method'})
    specify_managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'Specify Managed Identity Client ID'})
    managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Managed Identity Client ID'})
    resource_group: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Resource Group'})
    tenant_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tenant ID'})
    application_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Application ID'})
    client_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Client Secret'})
    azure_login_url: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Azure Login URL'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileQlikCloud(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Qlik Cloud', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Qlik Cloud'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    qlik_api_url: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Qlik API URL'})
    tenant_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tenant ID'})
    region: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Region'})
    api_key: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'API Key'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileJenkins(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Jenkins', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Jenkins'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    jenkins_url: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Jenkins URL'})
    username: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Username'})
    user_api_token: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'User API Token'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileMicrosoftPowerBI(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Microsoft Power BI', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Microsoft Power BI'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    application_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Application ID'})
    client_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Client Secret'})
    user_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'User Name'})
    password: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Password'})
    resource_group: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Resource Group'})
    api_url: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'API URL'})


@attrs.define
class ConnectionProfileAzureBackup(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Azure Backup', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Azure Backup'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    azure_login_url: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Azure Login URL'})
    azure_management_url: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Azure Management URL'})
    subscription_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Subscription ID'})
    authentication_method: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Authentication Method'})
    specify_managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'Specify Managed Identity Client ID'})
    managed_identity_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Managed Identity Client ID'})
    tenant_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tenant ID'})
    application_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Application  ID'})
    client_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Client Secret'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileSnowflake(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Snowflake', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Snowflake'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    account_identifier: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Account Identifier'})
    region: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Region'})
    client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Client ID'})
    client_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Client Secret'})
    refresh_token: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Refresh Token'})
    redirect_url: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Redirect URL'})


@attrs.define
class ConnectionProfileOCIVM(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:OCI VM', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:OCI VM'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    oci_instances_url: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'OCI Instances URL'})
    oci_region: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'OCI Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    user_ocid: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'User OCID'})
    tenancy_ocid: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Tenancy OCID'})
    fingerprint: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Fingerprint'})
    private_key: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Private Key'})
    config_file_path: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Config File Path'})
    profile: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Profile'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileAwsDataPipeline(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS Data Pipeline', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS Data Pipeline'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    data_pipeline_url: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Data Pipeline URL'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    aws_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Access Key'})
    aws_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS Secret'})
    iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IAM Role'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileOCIDataIntegration(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:OCI Data Integration', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:OCI Data Integration'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    oci_data_integration_url: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'OCI Data Integration URL'})
    oci_region: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'OCI Region'})
    authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Authentication'})
    user_ocid: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'User OCID'})
    tenancy_ocid: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Tenancy OCID'})
    fingerprint: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Fingerprint'})
    private_key: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Private Key'})
    config_file_path: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Config File Path'})
    profile: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Profile'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})


@attrs.define
class ConnectionProfileMicroFocusWindows(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Micro Focus Windows', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Micro Focus Windows'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    mfbsi_directory_path: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'MFBSI Directory Path'})
    mfbsi_config_path: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'MFBSI Config Path'})
    runtime_environment: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Runtime Environment'})
    additional_micro_focus_settings_script: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Additional Micro Focus Settings Script'})
    run_as: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Run As'})
    run_as_pass: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'RunAs-Pass'})
