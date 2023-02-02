
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


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
class ConnectionProfileGCPDataFlow(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:GCP DataFlow', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:GCP DataFlow'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    identity_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Identity Type'})
    data_flow_url: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'DataFlow URL'})
    service_account_key: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Service Account Key'})


@attrs.define
class ConnectionProfileGCPDataproc(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:GCP Dataproc', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:GCP Dataproc'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    identity_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Identity Type'})
    dataproc_url: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Dataproc URL'})
    service_account_key__json_format: str = attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'Service Account Key (JSON Format)'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection timeout'})


@attrs.define
class ConnectionProfileAwsGlue(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS Glue', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS Glue'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    glue_url: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Glue url'})
    aws_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AWS_REGION'})
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
    redirect_uri: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Redirect URI'})


@attrs.define
class ConnectionProfileTalendDataManagement(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Talend Data Management', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Talend Data Management'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    api_url: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'API URL'})
    personal_access_token_authorization: str = attrs.field(kw_only=True, default=None, metadata={
                                                           '_aapi_repr_': 'Personal access token authorization'})


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
