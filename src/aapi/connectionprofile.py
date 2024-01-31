
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class ConnectionProfile(AAPIObject):

    _type: str = attrs.field(init=False, default='ConnectionProfile', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    target_ctm: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'TargetCTM'})
    target_agent: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'TargetAgent'})
    test_on_build: bool = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'TestOnBuild'})
    no_test_on_deploy: bool = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'NoTestOnDeploy'})
    description: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Description'})
    centralized: bool = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Centralized'})


@attrs.define
class ConnectionProfileAirflow(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Airflow', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Airflow'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class ConnectionProfileAirflowGoogleComposer(ConnectionProfileAirflow):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Airflow:GoogleComposer', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Airflow:GoogleComposer'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    service_account_key: str = attrs.field(
        metadata={'_aapi_repr_': 'ServiceAccountKey'})
    service_account_key_filename: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ServiceAccountKeyFilename'})
    base_url: str = attrs.field(metadata={'_aapi_repr_': 'BaseURL'})
    target_audience: str = attrs.field(
        metadata={'_aapi_repr_': 'TargetAudience'})


@attrs.define
class ConnectionProfileAirflowStandalone(ConnectionProfileAirflow):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Airflow:Standalone', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Airflow:Standalone'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    host: str = attrs.field(metadata={'_aapi_repr_': 'Host'})
    port: int = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Port'})
    secured_connection: bool = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'SecuredConnection'})
    user: str = attrs.field(metadata={'_aapi_repr_': 'User'})
    password: str = attrs.field(metadata={'_aapi_repr_': 'Password'})


@attrs.define
class ConnectionProfileAWS(ConnectionProfile):

    @attrs.define
    class ProxySettings(AAPIObject):

        host: str = attrs.field(metadata={'_aapi_repr_': 'Host'})
        port: int = attrs.field(metadata={'_aapi_repr_': 'Port'})
        username: str = attrs.field(metadata={'_aapi_repr_': 'Username'})
        password: str = attrs.field(metadata={'_aapi_repr_': 'Password'})

    _type: str = attrs.field(init=False, default='ConnectionProfile:AWS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:AWS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AccessKey'})
    secret_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'SecretAccessKey'})
    region: str = attrs.field(metadata={'_aapi_repr_': 'Region'})
    iam_role: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IAMRole'})
    proxy_settings: ProxySettings = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ProxySettings'})


@attrs.define
class ConnectionProfileAzure(ConnectionProfile):

    @attrs.define
    class Batch(AAPIObject):

        batch_account_name: str = attrs.field(
            metadata={'_aapi_repr_': 'BatchAccountName'})
        batch_account_key: str = attrs.field(
            metadata={'_aapi_repr_': 'BatchAccountKey'})
        location: str = attrs.field(metadata={'_aapi_repr_': 'Location'})

    _type: str = attrs.field(init=False, default='ConnectionProfile:Azure', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Azure'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    active_directory_domain_name: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ActiveDirectoryDomainName'})
    subscription_id: str = attrs.field(
        metadata={'_aapi_repr_': 'SubscriptionID'})
    application_id: str = attrs.field(
        metadata={'_aapi_repr_': 'ApplicationID'})
    password: str = attrs.field(metadata={'_aapi_repr_': 'Password'})
    user: str = attrs.field(metadata={'_aapi_repr_': 'User'})
    batch: Batch = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Batch'})


@attrs.define
class ConnectionProfileDatabase(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Database', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Database'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    user: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'User'})
    password: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Password'})
    max_concurrent_connections: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'MaxConcurrentConnections'})
    connection_retry_num: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'ConnectionRetryNum'})
    connection_retry_time_out: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ConnectionRetryTimeOut'})
    connection_idle_time: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'ConnectionIdleTime'})


@attrs.define
class ConnectionProfileDatabasePostgreSql(ConnectionProfileDatabase):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Database:PostgreSQL', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Database:PostgreSQL'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    database_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'DatabaseType'})
    database_version: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'DatabaseVersion'})
    host: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Host'})
    port: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Port'})
    database_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'DatabaseName'})


@attrs.define
class ConnectionProfileDatabaseMSSql(ConnectionProfileDatabase):

    class AuthenticationType(enum.Enum):

        SQL_Server_Authentication = "SQL_Server_Authentication"
        Windows_Authentication = "Windows_Authentication"
        NTLM2_Windows_Authentication = "NTLM2_Windows_Authentication"

    _type: str = attrs.field(init=False, default='ConnectionProfile:Database:MSSQL', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Database:MSSQL'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    database_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'DatabaseType'})
    database_version: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'DatabaseVersion'})
    host: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Host'})
    port: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Port'})
    authentication_type: AuthenticationType = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AuthenticationType'})
    database_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'DatabaseName'})
    secure: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Secure'})


@attrs.define
class ConnectionProfileDatabaseMSSqlSSIS(ConnectionProfileDatabaseMSSql):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Database:MSSQL:SSIS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Database:MSSQL:SSIS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    skip_packages_test: bool = attrs.field(
        metadata={'_aapi_repr_': 'SkipPackagesTest'})
    ssis: typing.List[Package] = attrs.field(metadata={'_aapi_repr_': 'SSIS'})


@attrs.define
class ConnectionProfileDatabaseDB2(ConnectionProfileDatabase):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Database:DB2', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Database:DB2'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    database_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'DatabaseType'})
    database_version: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'DatabaseVersion'})
    host: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Host'})
    port: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Port'})
    database_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'DatabaseName'})


@attrs.define
class ConnectionProfileDatabaseSybase(ConnectionProfileDatabase):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Database:Sybase', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Database:Sybase'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    database_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'DatabaseType'})
    database_version: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'DatabaseVersion'})
    host: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Host'})
    port: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Port'})
    database_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'DatabaseName'})


@attrs.define
class ConnectionProfileDatabaseOracle(ConnectionProfileDatabase):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Database:Oracle', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Database:Oracle'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    database_version: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'DatabaseVersion'})


@attrs.define
class ConnectionProfileDatabaseOracleSID(ConnectionProfileDatabaseOracle):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Database:Oracle:SID', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Database:Oracle:SID'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    sid: str = attrs.field(metadata={'_aapi_repr_': 'SID'})
    port: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Port'})
    host: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Host'})


@attrs.define
class ConnectionProfileDatabaseOracleServiceName(ConnectionProfileDatabaseOracle):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Database:Oracle:ServiceName', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Database:Oracle:ServiceName'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    service_name: str = attrs.field(metadata={'_aapi_repr_': 'ServiceName'})
    port: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Port'})
    host: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Host'})


@attrs.define
class ConnectionProfileDatabaseOracleConnectionString(ConnectionProfileDatabaseOracle):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Database:Oracle:ConnectionString', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Database:Oracle:ConnectionString'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_string: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'ConnectionString'})


@attrs.define
class ConnectionProfileDatabaseJDBC(ConnectionProfileDatabase):

    _type: str = attrs.field(init=False, default='ConnectionProfile:Database:JDBC', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Database:JDBC'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    port: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Port'})
    database_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'DatabaseName'})
    host: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Host'})
    driver: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Driver'})


@attrs.define
class ConnectionProfileFileTransferDualEndPoint(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:DualEndPoint', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:DualEndPoint'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    workload_automation_users: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'WorkloadAutomationUsers'})
    workload_automation_groups: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'WorkloadAutomationGroups'})
    verify_bytes: bool = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'VerifyBytes'})
    verify_destination: bool = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'VerifyDestination'})
    verify_checksum: bool = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'VerifyChecksum'})
    endpoint_src_ftp_list: typing.List[EndpointSrcFtp] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    endpoint_dest_ftp_list: typing.List[EndpointDestFtp] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    endpoint_src_ftps_list: typing.List[EndpointSrcFtps] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    endpoint_dest_ftps_list: typing.List[EndpointDestFtps] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    endpoint_src_sftp_list: typing.List[EndpointSrcSftp] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    endpoint_dest_sftp_list: typing.List[EndpointDestSftp] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    endpoint_src_local_list: typing.List[EndpointSrcLocal] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    endpoint_dest_local_list: typing.List[EndpointDestLocal] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})


@attrs.define
class ConnectionProfileFileTransferGroup(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:Group', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:Group'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    workload_automation_users: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'WorkloadAutomationUsers'})
    workload_automation_groups: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'WorkloadAutomationGroups'})
    group_accounts: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'GroupAccounts'})
    connection_profile_file_transfer_as2_list: typing.List[ConnectionProfileFileTransferAS2] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    connection_profile_file_transfer_s3_compatible_list: typing.List[ConnectionProfileFileTransferS3Compatible] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    connection_profile_file_transfer_s3_amazon_list: typing.List[ConnectionProfileFileTransferS3Amazon] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    connection_profile_file_transfer_s3_list: typing.List[ConnectionProfileFileTransferS3] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    connection_profile_file_transfer_azure_list: typing.List[ConnectionProfileFileTransferAzure] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    connection_profile_file_transfer_gcs_list: typing.List[ConnectionProfileFileTransferGcs] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    connection_profile_file_transfer_sftp_list: typing.List[ConnectionProfileFileTransferSFTP] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    connection_profile_file_transfer_ftps_list: typing.List[ConnectionProfileFileTransferFTPS] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    connection_profile_file_transfer_ftp_list: typing.List[ConnectionProfileFileTransferFTP] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})


@attrs.define
class ConnectionProfileFileTransfer(ConnectionProfile):


    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    host_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'HostName'})
    os_type: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'OsType'})
    user: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'User'})
    port: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Port'})
    home_directory: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'HomeDirectory'})
    password: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Password'})
    conntype: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Conntype'})
    workload_automation_users: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'WorkloadAutomationUsers'})
    workload_automation_groups: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'WorkloadAutomationGroups'})
    verify_bytes: bool = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'VerifyBytes'})
    verify_destination: bool = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'VerifyDestination'})
    private_key_name: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'PrivateKeyName'})
    passphrase: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Passphrase'})
    verify_checksum: bool = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'VerifyChecksum'})
    additional_parameters: typing.List[PackageParams] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AdditionalParameters'})


@attrs.define
class ConnectionProfileFileTransferLocal(ConnectionProfileFileTransfer):

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:Local', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:Local'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class ConnectionProfileFileTransferFTP(ConnectionProfileFileTransfer):

    class ConnectionMode(enum.Enum):

        Active = "Active"
        Passive = "Passive"
        PassiveSubstituteIpAddress = "PassiveSubstituteIpAddress"
        EPSV = "EPSV"
        EPSVSubstituteIpAddress = "EPSVSubstituteIpAddress"
        off = "off"
        on = "on"
        noSubstituteIP = "noSubstituteIP"

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:FTP', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:FTP'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_mode: ConnectionMode = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ConnectionMode'})


@attrs.define
class ConnectionProfileFileTransferFTPS(ConnectionProfileFileTransfer):

    class ConnectionMode(enum.Enum):

        Active = "Active"
        Passive = "Passive"
        PassiveSubstituteIpAddress = "PassiveSubstituteIpAddress"
        EPSV = "EPSV"
        EPSVSubstituteIpAddress = "EPSVSubstituteIpAddress"
        off = "off"
        on = "on"
        noSubstituteIP = "noSubstituteIP"

    class SslLevel(enum.Enum):

        NoAuthentication = "NoAuthentication"
        ServerAuthentication = "ServerAuthentication"
        ClientServerAuthentication = "ClientServerAuthentication"

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:FTPS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:FTPS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_mode: ConnectionMode = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ConnectionMode'})
    ssl_level: SslLevel = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'SSLLevel'})
    ssl_implicit: bool = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'SSLImplicit'})
    clear_data_channel: bool = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'ClearDataChannel'})
    clear_command_channel: bool = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'ClearCommandChannel'})


@attrs.define
class ConnectionProfileFileTransferSFTP(ConnectionProfileFileTransfer):

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:SFTP', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:SFTP'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    ssh_compression: bool = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'SSHCompression'})


@attrs.define
class ConnectionProfileFileTransferS3(ConnectionProfileFileTransfer):

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:S3', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:S3'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AccessKey'})
    secret_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'SecretAccessKey'})
    s3_storage_type: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'S3StorageType'})


@attrs.define
class ConnectionProfileFileTransferS3Amazon(ConnectionProfileFileTransferS3):

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:S3:Amazon', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:S3:Amazon'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    region: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Region'})


@attrs.define
class ConnectionProfileFileTransferS3Compatible(ConnectionProfileFileTransferS3):

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:S3:Compatible', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:S3:Compatible'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    rest_end_point: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'RestEndPoint'})


@attrs.define
class ConnectionProfileFileTransferGcs(ConnectionProfileFileTransfer):

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:GCS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:GCS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    gcs_service_account_key: str = attrs.field(
        metadata={'_aapi_repr_': 'GCSServiceAccountKey'})
    gcs_service_account_key_file_name: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'GCSServiceAccountKeyFileName'})


@attrs.define
class ConnectionProfileFileTransferAzure(ConnectionProfileFileTransfer):

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:Azure', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:Azure'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    azure_account_name: str = attrs.field(
        metadata={'_aapi_repr_': 'AzureAccountName'})
    azure_storage_type: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AzureStorageType'})
    azure_endpoint: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AzureEndpoint'})
    azure_credential_method: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AzureCredentialMethod'})


@attrs.define
class ConnectionProfileFileTransferAzureSharedKey(ConnectionProfileFileTransferAzure):

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:Azure:SharedKey', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:Azure:SharedKey'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    azure_account_access_key: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AzureAccountAccessKey'})


@attrs.define
class ConnectionProfileFileTransferAzureConnectionString(ConnectionProfileFileTransferAzure):

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:Azure:ConnectionString', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:Azure:ConnectionString'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    azure_account_connection_string: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AzureAccountConnectionString'})


@attrs.define
class ConnectionProfileFileTransferAzureAdUserPass(ConnectionProfileFileTransferAzure):

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:Azure:AdUserPass', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:Azure:AdUserPass'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    azure_tenant_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AzureTenantId'})
    azure_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AzureClientId'})
    azure_user_name_ad: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AzureUserNameAD'})
    azure_user_password_ad: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AzureUserPasswordAD'})


@attrs.define
class ConnectionProfileFileTransferAzureAdClientSecret(ConnectionProfileFileTransferAzure):

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:Azure:AdClientSecret', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:Azure:AdClientSecret'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    azure_tenant_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AzureTenantId'})
    azure_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AzureClientId'})
    azure_client_secret: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AzureClientSecret'})


@attrs.define
class ConnectionProfileFileTransferAzureAdCertificate(ConnectionProfileFileTransferAzure):

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:Azure:AdCertificate', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:Azure:AdCertificate'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    azure_tenant_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AzureTenantId'})
    azure_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AzureClientId'})
    azure_client_certificate_format: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AzureClientCertificateFormat'})
    azure_client_certificate_path: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AzureClientCertificatePath'})
    azure_client_certificate_password: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AzureClientCertificatePassword'})


@attrs.define
class ConnectionProfileFileTransferAzureSharedAccessSignature(ConnectionProfileFileTransferAzure):

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:Azure:SharedAccessSignature', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:Azure:SharedAccessSignature'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    azure_account_sas_token: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AzureAccountSaSToken'})


@attrs.define
class ConnectionProfileFileTransferAzureManagedIdentity(ConnectionProfileFileTransferAzure):

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:Azure:ManagedIdentity', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:Azure:ManagedIdentity'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    azure_tenant_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AzureTenantId'})
    azure_client_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AzureClientId'})


@attrs.define
class ConnectionProfileFileTransferAS2(ConnectionProfileFileTransfer):

    @attrs.define
    class SignMessageParameters(AAPIObject):

        class SignatureAlgorithm(enum.Enum):

            RSA_with_SHA_1 = "RSA_with_SHA_1"
            RSA_with_SHA_224 = "RSA_with_SHA_224"
            RSA_with_SHA_256 = "RSA_with_SHA_256"
            RSA_with_SHA_384 = "RSA_with_SHA_384"
            RSA_with_SHA_512 = "RSA_with_SHA_512"
            RSA_with_MD5 = "RSA_with_MD5"

        sign_message: bool = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'SignMessage'})
        signature_algorithm: SignatureAlgorithm = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'SignatureAlgorithm'})

    @attrs.define
    class EncryptMessageParameters(AAPIObject):

        class EncryptionAlgorithm(enum.Enum):

            CAST5_CBC = "CAST5_CBC"
            IDEA_CBC = "IDEA_CBC"
            RC2_CBC = "RC2_CBC"
            tripleDES_DES_EDE3 = "tripleDES_DES_EDE3"
            AES128_CBC = "AES128_CBC"
            AES192_CBC = "AES192_CBC"
            AES256_CBC = "AES256_CBC"
            AES128_GCM = "AES128_GCM"
            AES192_GCM = "AES192_GCM"
            AES256_GCM = "AES256_GCM"

        encrypt_message: bool = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'EncryptMessage'})
        encryption_algorithm: EncryptionAlgorithm = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'EncryptionAlgorithm'})

    @attrs.define
    class RequestReceiptParameters(AAPIObject):

        class Sign(enum.Enum):

            Signed = "Signed"
            Unsigned = "Unsigned"

        class Mode(enum.Enum):

            Asynchronous = "Asynchronous"
            Synchronous = "Synchronous"

        request_receipt: bool = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'RequestReceipt'})
        sign: Sign = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Sign'})
        mode: Mode = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Mode'})

    _type: str = attrs.field(init=False, default='ConnectionProfile:FileTransfer:AS2', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:FileTransfer:AS2'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    partner_as2_id: str = attrs.field(metadata={'_aapi_repr_': 'PartnerAS2Id'})
    partner_destination_url: str = attrs.field(
        metadata={'_aapi_repr_': 'PartnerDestinationUrl'})
    partner_certificate_alias: str = attrs.field(
        metadata={'_aapi_repr_': 'PartnerCertificateAlias'})
    sign_message_parameters: SignMessageParameters = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'SignMessageParameters'})
    encrypt_message_parameters: EncryptMessageParameters = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'EncryptMessageParameters'})
    compress_message: bool = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'CompressMessage'})
    request_receipt_parameters: RequestReceiptParameters = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'RequestReceiptParameters'})
    send_message_timeout: int = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'SendMessageTimeout'})
    async_mdn_timeout: int = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AsyncMdnTimeout'})


@attrs.define
class ConnectionProfileHadoop(ConnectionProfile):

    @attrs.define
    class Sqoop(AAPIObject):

        user: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'User'})
        password: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Password'})
        password_file: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'PasswordFile'})
        database_vendor: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'DatabaseVendor'})
        database_host: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'DatabaseHost'})
        database_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'DatabaseName'})
        database_port: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'DatabasePort'})
        connection_string: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'ConnectionString'})
        driver_class: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'DriverClass'})
        database_type: bool = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'DatabaseType'})

    @attrs.define
    class Hive(AAPIObject):

        class ConnectionDefinitionsType(enum.Enum):

            Properties = "Properties"
            String = "String"

        database_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'DatabaseName'})
        host: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Host'})
        port: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Port'})
        user: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'User'})
        password: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Password'})
        principal: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Principal'})
        connection_definitions_type: ConnectionDefinitionsType = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'ConnectionDefinitionsType'})
        connection_string: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'ConnectionString'})

    @attrs.define
    class Tajo(AAPIObject):

        binary_path: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'BinaryPath'})
        database_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'DatabaseName'})
        master_server_name: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'MasterServerName'})
        master_server_port: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'MasterServerPort'})

    @attrs.define
    class Oozie(AAPIObject):

        host: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Host'})
        port: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Port'})
        ssl_enabled: bool = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'SslEnabled'})
        extraction_rules: typing.List[ExtractRule] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'ExtractionRules'})

    @attrs.define
    class Spark(AAPIObject):

        custom_path: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'CustomPath'})

    _type: str = attrs.field(init=False, default='ConnectionProfile:Hadoop', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Hadoop'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    run_as: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'RunAs'})
    key_tab_path: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'KeyTabPath'})
    sqoop: Sqoop = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Sqoop'})
    hive: Hive = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'Hive'})
    tajo: Tajo = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'Tajo'})
    oozie: Oozie = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Oozie'})
    spark: Spark = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Spark'})


@attrs.define
class ConnectionProfileInformatica(ConnectionProfile):

    class ConnectionType(enum.Enum):

        HTTP = "HTTP"
        HTTPS = "HTTPS"

    _type: str = attrs.field(init=False, default='ConnectionProfile:Informatica', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:Informatica'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    host: str = attrs.field(metadata={'_aapi_repr_': 'Host'})
    port: int = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Port'})
    user: str = attrs.field(metadata={'_aapi_repr_': 'User'})
    password: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Password'})
    power_center_domain: str = attrs.field(
        metadata={'_aapi_repr_': 'PowerCenterDomain'})
    repository: str = attrs.field(metadata={'_aapi_repr_': 'Repository'})
    integration_service: str = attrs.field(
        metadata={'_aapi_repr_': 'IntegrationService'})
    security_domain: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'SecurityDomain'})
    max_concurrent_connections: int = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'MaxConcurrentConnections'})
    connection_type: ConnectionType = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ConnectionType'})


@attrs.define
class ConnectionProfilePeopleSoft(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:PeopleSoft', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:PeopleSoft'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    user: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'User'})
    application_servers: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ApplicationServers'})
    password: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Password'})
    domain_password: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'DomainPassword'})
    people_tools_version: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'PeopleToolsVersion'})


@attrs.define
class ConnectionProfileSAP(ConnectionProfile):

    @attrs.define
    class GroupLogon(AAPIObject):

        system_id: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'SystemID'})
        message_server_host_name: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'MessageServerHostName'})
        group_name: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'GroupName'})
        sapr3_use_logon_group: str = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'SAPR3-USE_LOGON_GROUP'})

    @attrs.define
    class ApplicationServerLogon(AAPIObject):

        host: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Host'})
        system_number: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'SystemNumber'})
        sapr3_use_logon_group: str = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'SAPR3-USE_LOGON_GROUP'})

    @attrs.define
    class SecuredNetworkConnection(AAPIObject):

        snc_lib: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'SncLib'})
        snc_partner_name: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'SncPartnerName'})
        quality_of_protection: str = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'QualityOfProtection'})
        snc_my_name: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'SncMyName'})
        snc_mode: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'SNC_MODE'})

    _type: str = attrs.field(init=False, default='ConnectionProfile:SAP', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:SAP'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    user: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'User'})
    password: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Password'})
    sap_client: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'SapClient'})
    language: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Language'})
    xbp_version: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'XBPVersion'})
    app_version: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AppVersion'})
    sap_response_time_out: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'SapResponseTimeOut'})
    use_extended: bool = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'UseExtended'})
    is_solution_manager_connection_profile: bool = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'IsSolutionManagerConnectionProfile'})
    solution_manager_connection_profile: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'SolutionManagerConnectionProfile'})
    group_logon: GroupLogon = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'GroupLogon'})
    application_server_logon: ApplicationServerLogon = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ApplicationServerLogon'})
    secured_network_connection: SecuredNetworkConnection = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'SecuredNetworkConnection'})
    sap_router: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'SapRouter'})


@attrs.define
class ConnectionProfileWebServices(ConnectionProfile):

    class ServiceType(enum.Enum):

        WebServices = "WebServices"
        Rest = "Rest"
        File = "File"

    _type: str = attrs.field(init=False, default='ConnectionProfile:WebServices', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:WebServices'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    old_account_name: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'OldAccountName'})
    service_type: ServiceType = attrs.field(
        metadata={'_aapi_repr_': 'ServiceType'})
    location: str = attrs.field(metadata={'_aapi_repr_': 'Location'})
    http_authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'HttpAuthentication'})
    login_url: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'LoginUrl'})
    login_header: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'LoginHeader'})
    login_body: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'LoginBody'})
    job_preset: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'JobPreset'})


@attrs.define
class ConnectionProfileWSCONFIG(ConnectionProfile):

    _type: str = attrs.field(init=False, default='ConnectionProfile:WSCONFIG', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ConnectionProfile:WSCONFIG'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    http_proxy_host: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'HttpProxyHost'})
    http_proxy_port: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'HttpProxyPort'})
    http_non_proxy_hosts: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'HttpNonProxyHosts'})
    http_authentication: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'HttpAuthentication'})
    cm_container_port: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'CmContainerPort'})
