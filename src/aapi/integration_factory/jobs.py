
from __future__ import annotations
import attrs
import typing
import enum
from aapi.bases import AAPIObject
from aapi.job import Job
from aapi.connectionprofile import ConnectionProfile


@attrs.define
class JobAwsDataSync(Job):

    _type: str = attrs.field(init=False, default='Job:AWS DataSync', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS DataSync'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    task_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Task ARN'})
    output_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Output Logs'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAwsDynamoDB(Job):

    _type: str = attrs.field(init=False, default='Job:AWS DynamoDB', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS DynamoDB'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    statement: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Statement'})
    run_statement_with_parameter: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'Run Statement with Parameter'})
    statement_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Statement Parameters'})
    transaction_statments: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Transaction Statments'})
    idempotency_token: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Idempotency Token'})
    export_format: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Export Format'})
    s3_bucket_name: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'S3 Bucket Name'})
    s3_path_prefix: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'S3 Path Prefix'})
    s3_bucket_owner_id: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'S3 Bucket Owner ID'})
    table_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Table ARN'})
    import_format: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Import Format'})
    import_compression_type: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Import Compression Type'})
    table_creation_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Table Creation Parameters'})
    table_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Table Name'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolarance_: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Failure Tolarance '})


@attrs.define
class JobAzureDevOps(Job):

    _type: str = attrs.field(init=False, default='Job:Azure DevOps', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure DevOps'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    project_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Project Name'})
    actions: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Actions'})
    pipeline_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Pipeline Id'})
    repository_path: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Repository Path'})
    variables: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Variables'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    stages_to_skip: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Stages To Skip'})
    show_build_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Show Build Logs'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobGCPDeploymentManager(Job):

    _type: str = attrs.field(init=False, default='Job:GCP Deployment Manager', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Deployment Manager'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    project_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project ID'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    deployment_name: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Deployment Name'})
    yaml_config_content: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Yaml Config Content'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAwsEC2(Job):

    _type: str = attrs.field(init=False, default='Job:AWS EC2', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS EC2'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    operations: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Operations'})
    instance_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Instance ID'})
    placement_availability_zone: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Placement Availability Zone'})
    instance_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Instance Type'})
    instance_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Instance Name'})
    subnet_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Subnet ID'})
    key_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Key Name'})
    image_id: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Image ID'})
    number_of_copies: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Number of copies'})
    launch_template_id: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Launch Template ID'})
    tag_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Tag Name'})
    tag_value: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tag Value'})
    idempotent_token: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Idempotent Token'})
    tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tolerance'})
    verification_poll_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Verification Poll Interval'})
    get_instances_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Get Instances logs'})


@attrs.define
class JobRubrik(Job):

    _type: str = attrs.field(init=False, default='Job:Rubrik', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Rubrik'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    s_l_a_id: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'SLA ID'})
    vm_id: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'VM ID'})
    oracle_db_id: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Oracle DB ID'})
    n_a_s_id: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'NAS ID'})
    sql_db_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'SQL DB ID'})
    delay_logs_retrieval: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Delay Logs Retrieval'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    year: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'YEAR'})
    month: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'MONTH'})
    day: str = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'DAY'})


@attrs.define
class JobAwsBackup(Job):

    _type: str = attrs.field(init=False, default='Job:AWS Backup', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Backup'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    windows_vss: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Windows VSS'})
    backup_vault_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Backup Vault Name'})
    role_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Role ARN'})
    idempotency_token: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Idempotency Token'})
    resource_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Resource ARN'})
    restore_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Restore Parameters'})
    recovery_point_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Recovery Point ARN'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


@attrs.define
class JobAirbyte(Job):

    _type: str = attrs.field(init=False, default='Job:Airbyte', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Airbyte'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    connection_id: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Connection Id'})
    job_type: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Job Type'})
    show_results: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Show Results'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobGCPVM(Job):

    _type: str = attrs.field(init=False, default='Job:GCP VM', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP VM'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    project_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project ID'})
    zone: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Zone'})
    operation: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Operation'})
    tag_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Tag Name'})
    tag_value: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tag Value'})
    template_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Template Name'})
    instance_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Instance Name'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    verification_poll_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Verification Poll Interval'})
    tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tolerance'})
    get_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Get Logs'})


@attrs.define
class JobAwsAppRunner(Job):

    _type: str = attrs.field(init=False, default='Job:AWS App Runner', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS App Runner'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    service_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Service Arn'})
    output_job_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Output Job Logs'})
    failure_tolerance_: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Failure Tolerance  '})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


@attrs.define
class JobGCPDataFusion(Job):

    _type: str = attrs.field(init=False, default='Job:GCP Data Fusion', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Data Fusion'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    region: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Region'})
    project_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Project Name'})
    instance_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Instance Name'})
    name_space_id: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Name Space ID'})
    pipeline_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Pipeline Name'})
    runtime_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Runtime Parameters'})
    get_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Get Logs'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobDatadog(Job):

    _type: str = attrs.field(init=False, default='Job:Datadog', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Datadog'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    workflow_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Workflow ID'})
    workflow_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Workflow Parameters'})
    synthetics_test_type: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Synthetics Test Type'})
    test_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Test Parameters'})
    event_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Event Parameters'})
    incident_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Incident ID'})
    incident_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Incident Parameters'})
    delay_logs_retrieval: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Delay Logs Retrieval'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobUIPath(Job):

    _type: str = attrs.field(init=False, default='Job:UI Path', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:UI Path'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    folder_name: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Folder Name'})
    folder_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Folder Id'})
    process_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Process Name'})
    robot_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Robot Name'})
    robot_id: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Robot Id'})
    optional_input_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Optional Input Parameters'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


@attrs.define
class JobAwsGlue(Job):

    _type: str = attrs.field(init=False, default='Job:AWS Glue', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Glue'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    glue_job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Glue Job Name'})
    glue_workflow_name: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Glue Workflow Name'})
    crawler_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Crawler Name'})
    glue_job_arguments: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Glue Job Arguments'})
    arguments: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Arguments'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})
    output_job_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Output Job Logs'})
    log_type: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Log type'})


@attrs.define
class JobApacheAirflow(Job):

    _type: str = attrs.field(init=False, default='Job:Apache Airflow', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Apache Airflow'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    airflow_rest_version: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Airflow REST Version'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    d_a_g_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'DAG Name'})
    d_a_g_run_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'DAG Run ID'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    logical_date: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Logical Date'})
    only_failed_tasks: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Only Failed Tasks'})
    include_subdags: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Include Subdags'})
    include_upstream: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Include Upstream'})
    include_downstream: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Include Downstream'})
    url_request_path: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'URL Request Path'})
    json: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'JSON'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAwsCloudFormation(Job):

    _type: str = attrs.field(init=False, default='Job:AWS CloudFormation', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS CloudFormation'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    stack_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Stack Name'})
    stack_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Stack Parameters'})
    template_body: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Template Body'})
    template_url: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Template URL'})
    role_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Role ARN'})
    capabilities_type: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Capabilities Type'})
    enable_termination_protection: str = attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'Enable Termination Protection'})
    on_failure: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'On Failure'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAwsAppFlow(Job):

    _type: str = attrs.field(init=False, default='Job:AWS AppFlow', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS AppFlow'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    flow_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Flow Name'})
    flow_name__iam: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Flow Name - IAM'})
    flow_name__assume_role: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Flow Name - Assume Role'})
    trigger_flow_with_idempotency_token: str = attrs.field(kw_only=True, default=None, metadata={
                                                           '_aapi_repr_': 'Trigger Flow with Idempotency Token'})
    client_token: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Client Token'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAzureBatchAccounts(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Batch Accounts', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Batch Accounts'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    batch_job_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Batch Job ID'})
    task_id_prefix: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Task ID Prefix'})
    task_command_line: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Task Command Line'})
    max_wall_clock_time: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Max Wall Clock Time'})
    max_wall_time_digits: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Max Wall Time Digits'})
    max_wall_time_unit: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Max Wall Time Unit'})
    max_task_retry_count: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Max Task Retry Count'})
    retry_number: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Retry Number'})
    retention_time: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Retention Time'})
    retention_time_digits: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Retention Time Digits'})
    retention_time_unit: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Retention Time Unit'})
    append_log_to_output: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Append Log to Output'})
    status_polling_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Status polling interval'})
    task_id_variable: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Task ID variable'})
    content_type: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Content-Type'})


@attrs.define
class JobAzureFunctions(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Functions', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Functions'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    function_app: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Function App'})
    azure_resource: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Azure Resource'})
    azure_resource_scope: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Azure Resource Scope'})
    function_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Function Name'})
    optional_input_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Optional Input Parameters'})
    function_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Function Type'})
    verification_poll_intervall: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Verification Poll Intervall'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})
    api_v_e_r_s_i_o_n: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'API-VERSION'})


@attrs.define
class JobAwsEMR(Job):

    _type: str = attrs.field(init=False, default='Job:AWS EMR', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS EMR'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    cluster_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Cluster Id'})
    notebook_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Notebook ID'})
    relative_path: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Relative Path'})
    notebook_execution_name: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Notebook Execution Name'})
    service_role: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Service Role'})
    use_advanced_json_format: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Use Advanced JSON Format'})
    json_body: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'JSON Body'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tolerance'})


@attrs.define
class JobTableau(Job):

    _type: str = attrs.field(init=False, default='Job:Tableau', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Tableau'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    datasource_name: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Datasource Name'})
    flow_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Flow Name'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobGCPComposer(Job):

    _type: str = attrs.field(init=False, default='Job:GCP Composer', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Composer'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    d_a_g_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'DAG Name'})
    d_a_g_run_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'DAG Run ID'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    only_failed_tasks: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Only Failed Tasks'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobGCPDataplex(Job):

    _type: str = attrs.field(init=False, default='Job:GCP Dataplex', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Dataplex'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    project_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project ID'})
    location: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Location'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    scan_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Scan Name'})
    lake_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Lake Name'})
    task_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Task Name'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAzureVM(Job):

    _type: str = attrs.field(init=False, default='Job:Azure VM', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure VM'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    vm_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'VM Name'})
    operation: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Operation'})
    tag_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Tag Name'})
    tag_value: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tag Value'})
    input_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Input Parameters'})
    verification_poll_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Verification Poll Interval'})
    delete_vm_os_disk: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Delete VM OS Disk'})
    tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tolerance'})
    api_v_e_r_s_i_o_n: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'API-VERSION'})
    get_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Get Logs'})


@attrs.define
class JobApacheNiFi(Job):

    _type: str = attrs.field(init=False, default='Job:Apache NiFi', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Apache NiFi'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    processor_group_id: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Processor Group ID'})
    processor_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Processor ID'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    disconnected_node_ack: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Disconnected Node Ack'})
    parameters_: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Parameters '})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobSAPBTPScheduler(Job):

    _type: str = attrs.field(init=False, default='Job:SAP BTP Scheduler', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP BTP Scheduler'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    s_a_p_job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'SAP Job Name'})
    job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Job Name'})
    job_description: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Job Description'})
    job_url: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Job URL'})
    http_method: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'HTTP Method'})
    notification_on_success: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Notification On Success'})
    notification_on_error: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Notification On Error'})
    job_data: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Job Data'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobGCPDataflow(Job):

    _type: str = attrs.field(init=False, default='Job:GCP Dataflow', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Dataflow'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    project_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project ID'})
    region: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Region'})
    template_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Template Type'})
    template_location_gs_: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Template Location (gs://)'})
    parameters__json_format: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Parameters (JSON Format)'})
    verification_poll_interval_in_seconds: str = attrs.field(kw_only=True, default=None, metadata={
                                                             '_aapi_repr_': 'Verification Poll Interval (in seconds)'})
    log_level: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Log Level'})


@attrs.define
class JobAwsMWAA(Job):

    _type: str = attrs.field(init=False, default='Job:AWS MWAA', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS MWAA'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    m_w_a_a_environment_name: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'MWAA Environment Name'})
    d_a_g_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'DAG Name'})
    d_a_g_run_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'DAG Run ID'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    only_failed: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Only Failed'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobVeritasNetBackup(Job):

    _type: str = attrs.field(init=False, default='Job:Veritas NetBackup', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Veritas NetBackup'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    json_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'JSON Parameters'})
    create_jobs_per_client: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Create Jobs Per Client'})
    policy_name: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Policy Name'})
    client_name: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Client Name'})
    schedule_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Schedule Name'})
    keyword: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Keyword'})
    instance_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Instance Name'})
    database_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Database Name'})
    db_unique_name: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'DB Unique Name'})
    db_id: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'DB ID'})
    trial_backup: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Trial Backup'})
    output__management: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Output  Management'})
    restart_job_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Restart Job ID'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobGCPDataproc(Job):

    _type: str = attrs.field(init=False, default='Job:GCP Dataproc', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Dataproc'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    project_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project ID'})
    account_region: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Account Region'})
    dataproc_task_type: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Dataproc task type'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    batch_id: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Batch ID'})
    request_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Request ID'})
    workflow_template: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Workflow Template'})
    parameters__json_format: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Parameters (JSON Format)'})
    verification_poll_interval_in_seconds: str = attrs.field(kw_only=True, default=None, metadata={
                                                             '_aapi_repr_': 'Verification Poll Interval (in seconds)'})
    tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tolerance'})
    interactive_session_id: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Interactive Session ID'})


@attrs.define
class JobAzureSynapse(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Synapse', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Synapse'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    pipeline_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Pipeline Name'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    status_polling_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Status polling interval'})


@attrs.define
class JobVMwareByBroadcom(Job):

    _type: str = attrs.field(init=False, default='Job:VMware By Broadcom', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware By Broadcom'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    configuration_options: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Configuration Options'})
    power_tasks: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Power Tasks'})
    reconfigure_action: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Reconfigure Action'})
    snapshot_operations: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Snapshot Operations'})
    vm_logical_name: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'VM Logical Name'})
    vm_location: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'VM Location'})
    resource_pool: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Resource Pool'})
    folder: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Folder'})
    e_s_xi_host: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'ESXi Host'})
    datacenter: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Datacenter'})
    cluster: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Cluster'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    placement_json: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Placement JSON'})
    hot_remove: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Hot Remove'})
    hot_add: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Hot Add'})
    cpu_count: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'CPU Count'})
    cores_per_socket: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Cores Per Socket'})
    size_in_mi_b: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Size In MiB'})
    template_library_item_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Template Library Item ID'})
    snapshot_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Snapshot Name'})
    snapshot_description: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Snapshot Description'})
    memory_dump: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Memory Dump'})
    quiesce: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Quiesce'})
    snapshot_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Snapshot ID'})
    release_schema: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Release Schema'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobCommunicationSuite(Job):

    _type: str = attrs.field(init=False, default='Job:Communication Suite', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Communication Suite'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    application_name: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Application Name'})
    slack_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Slack Parameters'})
    telegram_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Telegram Parameters'})
    silent_message: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Silent Message'})
    protect_content: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Protect Content'})
    whats_app_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'WhatsApp Parameters'})
    teams_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Teams Parameters'})


@attrs.define
class JobAzureMachineLearning(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Machine Learning', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Machine Learning'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    workspace_name: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Workspace Name'})
    resource_group_name: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Resource Group Name'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    pipeline_endpoint_id: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Pipeline Endpoint ID'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    compute_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Compute Name'})
    compute_action: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Compute Action'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAzureDataFactory(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Data Factory', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Data Factory'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    resource_group_name: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Resource Group Name'})
    data_factory_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Data Factory Name'})
    pipeline_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Pipeline Name'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})
    restart_on_rerun: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Restart on Rerun'})
    reference_pipeline_run_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Reference Pipeline Run ID'})


@attrs.define
class JobOCIDataFlow(Job):

    _type: str = attrs.field(init=False, default='Job:OCI Data Flow', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OCI Data Flow'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    compartment_ocid: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Compartment OCID'})
    application_ocid: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Application OCID'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobWebServicesSOAP(Job):

    @attrs.define
    class SoapRequest(AAPIObject):

        request_definition: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'RequestDefinition'})
        file_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'FileName'})
        soap_request_field: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'SoapRequestField'})

    _type: str = attrs.field(init=False, default='Job:Web Services SOAP', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Web Services SOAP'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    endpoint_url: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Endpoint URL'})
    soap_action: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'SOAP Action'})
    soap_request: SoapRequest = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'SoapRequest'})
    http_headers: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'HTTP Headers'})
    output_handling: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'OutputHandling'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})
    append_request: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Append Request'})
    append_response: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Append Response'})


@attrs.define
class JobOCIDataScience(Job):

    _type: str = attrs.field(init=False, default='Job:OCI Data Science', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OCI Data Science'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    model_deployment_id: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Model Deployment ID'})
    notebook_session_id: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Notebook Session ID'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobBoomiAtomsphere(Job):

    _type: str = attrs.field(init=False, default='Job:Boomi Atomsphere', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Boomi Atomsphere'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    process_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Process Name'})
    atom_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Atom Name'})
    polling_interval_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Polling Interval Frequency'})
    tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tolerance'})


@attrs.define
class JobAzureDatabricks(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Databricks', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Databricks'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    databricks_job_id: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Databricks Job ID'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    idempotency_token: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Idempotency Token'})
    show_tasks_output: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Show Tasks Output'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAwsECS(Job):

    _type: str = attrs.field(init=False, default='Job:AWS ECS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS ECS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    ecs_cluster_name: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ECS Cluster Name'})
    ecs_task_definition: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'ECS Task Definition'})
    task_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Task ARN'})
    stop_reason: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Stop Reason'})
    launch_type: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Launch Type'})
    assign_public_ip: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Assign Public IP'})
    network_security_groups: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Network Security Groups'})
    network_subnets: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Network Subnets'})
    overrides: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Overrides'})
    override_container: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Override Container'})
    override_command: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Override Command'})
    environment_variables: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Environment Variables'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    get_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Get Logs'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAutomationAnywhere(Job):

    _type: str = attrs.field(init=False, default='Job:Automation Anywhere', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Automation Anywhere'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    automation_type: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Automation Type'})
    bot_to_run: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Bot to run'})
    process_uri_path: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Process Uri path'})
    process_to_run: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Process to run'})
    bot_input_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Bot input parameters'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection timeout'})


@attrs.define
class JobJenkins(Job):

    _type: str = attrs.field(init=False, default='Job:Jenkins', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Jenkins'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    pipeline_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Pipeline Name'})
    add_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Add Parameters'})
    parameters: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Parameters'})
    add_branch_name: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Add Branch Name'})
    branch_name: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Branch Name'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobRabbitMQ(Job):

    _type: str = attrs.field(init=False, default='Job:RabbitMQ', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:RabbitMQ'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    vhost: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Vhost'})
    exchange: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Exchange'})
    routing_key: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Routing Key'})
    message_to_publish: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Message to Publish'})
    message_encoding: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Message Encoding'})
    properties: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Properties'})
    queue: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Queue'})


@attrs.define
class JobAwsRedshift(Job):

    _type: str = attrs.field(init=False, default='Job:AWS Redshift', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Redshift'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    actions: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Actions'})
    workgroup_name: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Workgroup Name'})
    secret_manager_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Secret Manager ARN'})
    database: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Database'})
    table_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Table Name'})
    load_redshift_sql_statement: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Load Redshift SQL Statement'})
    procedure_name: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Procedure Name'})
    procedure_arguments: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Procedure Arguments'})
    s3_bucket_uri: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'S3 Bucket URI'})
    file_format: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'File Format'})
    use_iam_role_for_s3_access: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Use IAM Role For S3 Access'})
    iam_role_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'IAM Role ARN'})
    show_statement_results: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Show Statement Results'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tolerance'})


@attrs.define
class JobVeeamBackup(Job):

    _type: str = attrs.field(init=False, default='Job:Veeam Backup', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Veeam Backup'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    backup_u_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Backup UID'})
    retry: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Retry'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobMicrosoftPowerBI(Job):

    _type: str = attrs.field(init=False, default='Job:Microsoft Power BI', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Microsoft Power BI'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    dataset_refresh_pipeline_deployment: str = attrs.field(kw_only=True, default=None, metadata={
                                                           '_aapi_repr_': 'Dataset Refresh/ Pipeline Deployment'})
    workspace_name: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Workspace Name'})
    workspace_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Workspace ID'})
    dataset_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Dataset ID'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    pipeline_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Pipeline ID'})


@attrs.define
class JobAzureBackup(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Backup', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Backup'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    vault_resource_group: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Vault Resource Group'})
    vault_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Vault Name'})
    vm_resource_group: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'VM Resource Group'})
    vm_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'VM Name'})
    policy_name: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Policy Name'})
    include_or_exclude_disks: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Include Or Exclude Disks'})
    disk_list: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_abstract_aapi_container_': True})
    restore_to_latest_recovery_point: str = attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'Restore to Latest Recovery Point'})
    recovery_point_name: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Recovery Point Name'})
    storage_account_name: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Storage Account Name'})
    restore_region: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Restore Region'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance_: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Failure Tolerance '})


@attrs.define
class JobSnowflake(Job):

    _type: str = attrs.field(init=False, default='Job:Snowflake', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Snowflake'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    database: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Database'})
    schema: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Schema'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    snowflake_sql_statement: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Snowflake SQL Statement'})
    query_to_location: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Query to Location'})
    query_input: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Query Input'})
    storage_integration: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Storage Integration'})
    overwrite: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Overwrite'})
    file_format: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'File Format'})
    create_table_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Create Table Name'})
    query: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Query'})
    add_condition: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Add Condition'})
    stored_procedure_name: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Stored Procedure Name'})
    procedure_argument: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Procedure Argument'})
    activity_options: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Activity Options'})
    table_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Table Name'})
    from_location: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'From Location'})
    stage_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Stage Name'})
    from_storage_integration: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'From Storage Integration'})
    stage_url: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Stage URL'})
    copy_destination: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Copy Destination'})
    from_table: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'From Table'})
    snowpipe_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Snowpipe Name'})
    start_or_pause_snowpipe: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Start or Pause Snowpipe'})
    stage_location: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Stage Location'})
    days_back: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Days Back'})
    status_file_cloud_location_path: str = attrs.field(kw_only=True, default=None, metadata={
                                                       '_aapi_repr_': 'Status File Cloud Location Path'})
    stoarge_integration_for_location: str = attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'Stoarge Integration for Location'})
    load_sql_file: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Load SQL File'})
    statement_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Statement Timeout'})
    show_more_options: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Show More Options'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    role: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Role'})
    bindings: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Bindings'})
    warehouse: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Warehouse'})
    show_output: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Show Output'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


@attrs.define
class JobMicrosoftPowerBISP(Job):

    _type: str = attrs.field(init=False, default='Job:Microsoft Power BI SP', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Microsoft Power BI SP'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    workspace_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Workspace ID'})
    dataset_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Dataset ID'})
    dataflow_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Dataflow ID'})
    workspace_id__s_p: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Workspace ID - SP'})
    dataset_id__s_p: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Dataset ID - SP'})
    dataflow_id__s_p: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Dataflow ID - SP'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    parameters_enhanced: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Parameters Enhanced'})
    pipeline_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Pipeline ID'})
    pipeline_id__s_p: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Pipeline ID - SP'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAwsDatabaseMigrationService(Job):

    _type: str = attrs.field(init=False, default='Job:AWS Database Migration Service', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Database Migration Service'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    data_migration_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Data Migration ARN'})
    start_type: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Start Type'})
    database_migration_task_arn: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Database Migration Task ARN'})
    output_job_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Output Job Logs'})
    failure_tolerance_: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Failure Tolerance  '})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


@attrs.define
class JobMicroFocusWindows(Job):

    _type: str = attrs.field(init=False, default='Job:Micro Focus Windows', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Micro Focus Windows'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    jcl_filename: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'JCL Filename'})
    pds: str = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'PDS'})
    enable_jcl_variables: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Enable JCL Variables'})
    additional_variables: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Additional Variables'})
    restart_on_rerun: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Restart on Rerun'})
    from_step_proc: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'From Step/Proc'})
    to_step_proc: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'To Step/Proc'})
    recapture_abend_codes: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Recapture ABEND Codes'})
    recapture_cond_codes: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Recapture COND Codes'})
    auto_adjust_restart: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Auto Adjust Restart'})
    step_specific_condition_codes: str = attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'Step-Specific Condition Codes'})
    set_mf_ucc11: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Set MF_UCC11'})
    advanced_restart_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Advanced Restart Parameters'})
    rerun_job_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Rerun Job ID'})
    restart_with_modified_jcl: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Restart with Modified JCL'})
    modified_jcl_path_and_filename: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Modified JCL Path and Filename'})


@attrs.define
class JobIBMDataStageLinux(Job):

    _type: str = attrs.field(init=False, default='Job:IBM DataStage Linux', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:IBM DataStage Linux'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    project: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Project'})
    datastage_job: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Datastage Job'})
    job_invocation_id__optional: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Job Invocation ID (Optional)'})
    parameters_type: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Parameters Type'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    parameter_file: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Parameter File'})
    stop_stages_after_number_of_rows: str = attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'Stop Stages After Number Of Rows'})
    abort_job_after_number_of_warnings: str = attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'Abort Job After Number Of Warnings'})
    append_log_to_output: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Append Log To Output'})
    run_in_restart_mode: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Run In Restart Mode'})
    reset_job_before_run: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Reset Job Before Run'})
    empty1: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Empty1'})


@attrs.define
class JobAlibabaECS(Job):

    _type: str = attrs.field(init=False, default='Job:Alibaba ECS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Alibaba ECS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    instance_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Instance ID'})
    tag_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Tag Name'})
    tag_value: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tag Value'})
    verification_poll_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Verification Poll Interval'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAnsibleAWX(Job):

    _type: str = attrs.field(init=False, default='Job:Ansible AWX', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Ansible AWX'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    job_template_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Job Template Name'})
    job_template_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Job Template ID'})
    workflow_template_name: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Workflow Template Name'})
    workflow_template_id: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Workflow Template ID'})
    inventory: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Inventory'})
    inventory_source: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Inventory Source'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    project_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Project Name'})
    project_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project ID'})
    output_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Output Logs'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobGCPBatch(Job):

    _type: str = attrs.field(init=False, default='Job:GCP Batch', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Batch'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    service_account__email_format: str = attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'Service Account (Email Format)'})
    project_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project ID'})
    region: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Region'})
    override_region: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Override Region'})
    allowed_locations: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Allowed Locations'})
    job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Job Name'})
    priority: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Priority'})
    runnable_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Runnable Type'})
    task_script_text: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Task Script Text'})
    container_image_uri: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Container Image URI'})
    entry_point: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Entry Point'})
    override_commands: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Override Commands'})
    commands: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Commands'})
    container_volumes: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Container Volumes'})
    cpu: str = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'CPU'})
    memory: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Memory'})
    maximum_retry_count: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Maximum Retry Count'})
    instance_policy: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Instance Policy'})
    machine_type: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Machine Type'})
    provisioning_model: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Provisioning Model'})
    machine_template: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Machine Template'})
    log_policy: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Log Policy'})
    use_advanced_json_format: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Use Advanced JSON Format'})
    json_format: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'JSON Format'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


@attrs.define
class JobAwsMainframeModernization(Job):

    _type: str = attrs.field(init=False, default='Job:AWS Mainframe Modernization', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Mainframe Modernization'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    application_name: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Application Name'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    jcl_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'JCL Name'})
    rerun_execution_id: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Rerun Execution ID'})
    secret_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Secret ARN'})
    from_step: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'From Step'})
    from_proc_step: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'From Proc Step'})
    to_step: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'To Step'})
    to_proc_step: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'To Proc Step'})
    retrieve_cloud_watch_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Retrieve CloudWatch Logs'})
    delay_logs_retrieval_: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Delay Logs Retrieval '})
    application_action: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Application Action'})
    client_token: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Client Token'})
    application_version: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Application Version'})
    environment_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Environment ID'})
    latest_application_version: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Latest Application Version'})
    definition_s3_location: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Definition S3 Location'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobWebServicesREST(Job):

    @attrs.define
    class WsRestBody(AAPIObject):

        request_definition: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'RequestDefinition'})
        body_request: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'BodyRequest'})
        file_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'FileName'})

    _type: str = attrs.field(init=False, default='Job:Web Services REST', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Web Services REST'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    endpoint_url: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Endpoint URL'})
    method: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Method'})
    url_request_path: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'URL Request Path'})
    ws_rest_body: WsRestBody = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'WsRestBody'})
    url_parameters: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'URL Parameters'})
    http_headers: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'HTTP Headers'})
    output_handling: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'OutputHandling'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})
    append_request: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Append Request'})
    append_response: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Append Response'})


@attrs.define
class JobTalendOAuth(Job):

    _type: str = attrs.field(init=False, default='Job:Talend OAuth', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Talend OAuth'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    task_executable: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Task Executable'})
    environment_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Environment ID'})
    task_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Task Name'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    log_level: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Log Level'})
    task_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Task Timeout'})
    append_task_logs_to_output: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Append Task Logs to Output'})
    plan_executable: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Plan Executable'})
    append_failed_plan_logs_to_output: str = attrs.field(kw_only=True, default=None, metadata={
                                                         '_aapi_repr_': 'Append Failed Plan Logs to Output'})
    rerun_only_failed_tasks: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Rerun Only Failed Tasks'})
    execution_plan_id: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Execution Plan ID'})
    step_id: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Step ID'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAzureHDInsight(Job):

    _type: str = attrs.field(init=False, default='Job:Azure HDInsight', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure HDInsight'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    bring_job_logs_to_output: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Bring job logs to output'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAwsQuickSight(Job):

    _type: str = attrs.field(init=False, default='Job:AWS QuickSight', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS QuickSight'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    aws_dataset_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AWS Dataset ID'})
    refresh_type: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Refresh Type'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobCircleCI(Job):

    _type: str = attrs.field(init=False, default='Job:CircleCI', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:CircleCI'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    project_slug: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Project Slug'})
    workflow_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Workflow ID'})
    pipeline_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Pipeline ID'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAzureAppServicesWebJobs(Job):

    _type: str = attrs.field(init=False, default='Job:Azure App Services WebJobs', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure App Services WebJobs'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    resource_group_name: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Resource Group Name'})
    web_app_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Web App Name'})
    web_job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Web Job Name'})
    slot: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Slot'})
    show_output: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Show Output'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAwsSageMaker(Job):

    _type: str = attrs.field(init=False, default='Job:AWS SageMaker', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS SageMaker'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    pipeline_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Pipeline Name'})
    idempotency_token: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Idempotency Token'})
    add_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Add Parameters'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    retry_pipeline_execution: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Retry Pipeline Execution'})
    pipeline_execution_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Pipeline Execution ARN'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAstronomer(Job):

    _type: str = attrs.field(init=False, default='Job:Astronomer', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Astronomer'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    d_a_g_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'DAG Name'})
    d_a_g_run_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'DAG Run ID'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    only_failed_tasks: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Only Failed Tasks'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobKubernetes(Job):

    @attrs.define
    class WsRestBody(AAPIObject):

        request_definition: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'RequestDefinition'})
        body_request: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'BodyRequest'})
        file_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'FileName'})

    _type: str = attrs.field(init=False, default='Job:Kubernetes', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Kubernetes'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    job_spec_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Job Spec Type'})
    job_spec_yaml: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Job Spec Yaml'})
    job_spec_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Job Spec Parameters'})
    spec_request_path: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Spec Request Path'})
    spec_request_method: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Spec Request Method'})
    spec_request_parameters: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Spec Request Parameters'})
    spec_request_headers: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Spec Request Headers'})
    ws_rest_body: WsRestBody = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'WsRestBody'})
    get_pod_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Get Pod Logs'})
    os_exit_code: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'OS Exit Code'})
    job_cleanup: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Job Cleanup'})
    job_status_polling_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Job Status Polling Interval'})


@attrs.define
class JobAwsSNS(Job):

    _type: str = attrs.field(init=False, default='Job:AWS SNS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS SNS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    message_type: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Message Type'})
    topic_type: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Topic Type'})
    individual_type: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Individual Type'})
    target_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Target ARN'})
    phone_number: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Phone Number'})
    json_message_structure: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Json Message Structure'})
    subject: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Subject'})
    message: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Message'})
    message_deduplication_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Message Deduplication ID'})
    message_group_id: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Message Group ID'})
    attributes: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Attributes'})
    attribute1_name: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.1 Name'})
    attribute1_value: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.1 Value'})
    attribute2_name: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.2 Name'})
    attribute2_value: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.2 Value'})
    attribute3_name: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.3 Name'})
    attribute3_value: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.3 Value'})
    sms_attributes: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'SMS Attributes'})
    sender_identifier: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Sender Identifier'})
    sender_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Sender ID'})
    origination_number: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Origination Number'})
    max_price: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Max Price'})
    sms_type: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'SMS Type'})
    push_notifications_attributes: str = attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'Push Notifications Attributes'})
    push_attribute1_name: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.1 Name'})
    push_attribute1_value: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.1 Value'})
    push_attribute2_name: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.2 Name'})
    push_attribute2_value: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.2 Value'})
    push_attribute3_name: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.3 Name'})
    push_attribute3_value: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.3 Value'})
    push_attribute4_name: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.4 Name'})
    push_attribute4_value: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.4 Value'})
    push_attribute5_name: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.5 Name'})
    push_attribute5_value: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.5 Value'})


@attrs.define
class JobAwsLambda(Job):

    _type: str = attrs.field(init=False, default='Job:AWS Lambda', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Lambda'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    function_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Function Name'})
    function_version: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Function Version'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    append_log_to_output: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Append Log to Output'})


@attrs.define
class JobAlteryxTrifacta(Job):

    _type: str = attrs.field(init=False, default='Job:Alteryx Trifacta', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Alteryx Trifacta'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    flow_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Flow Name'})
    rerun_with_new_idempotency_token: str = attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'Rerun With New Idempotency Token'})
    idempotent_token: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Idempotent Token'})
    retrack_job_status: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Retrack Job Status'})
    run_id: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Run-ID'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


@attrs.define
class JobIBMDataStageWindows(Job):

    _type: str = attrs.field(init=False, default='Job:IBM DataStage Windows', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:IBM DataStage Windows'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    project: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Project'})
    datastage_job: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Datastage Job'})
    job_invocation_id__optional: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Job Invocation ID (Optional)'})
    parameters_type: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Parameters Type'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    parameter_file: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Parameter File'})
    stop_stages_after_number_of_rows: str = attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'Stop Stages After Number Of Rows'})
    abort_job_after_number_of_warnings: str = attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'Abort Job After Number Of Warnings'})
    append_log_to_output: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Append Log To Output'})
    run_in_restart_mode: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Run In Restart Mode'})
    reset_job_before_run: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Reset Job Before Run'})
    empty1: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Empty1'})


@attrs.define
class JobAwsSQS(Job):

    _type: str = attrs.field(init=False, default='Job:AWS SQS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS SQS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action_type: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Action Type'})
    queue_type: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Queue Type'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    queue_url: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Queue URL'})
    message_body: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Message Body'})
    delay_seconds: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Delay Seconds'})
    message_deduplication_id: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Message Deduplication ID'})
    message_group_id: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Message Group ID'})
    message_attributes: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Message Attributes'})
    attribute1_name: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.1 Name'})
    attribute1_data_type: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.1 DataType'})
    attribute1_value: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.1 Value'})
    attribute2_name: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.2 Name'})
    attribute2_data_type: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.2 DataType'})
    attribute2_value: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.2 Value'})
    attribute3_name: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.3 Name'})
    attribute3_data_type: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.3 DataType'})
    attribute3_value: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.3 Value'})


@attrs.define
class JobSnowflakeIdP(Job):

    _type: str = attrs.field(init=False, default='Job:Snowflake IdP', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Snowflake IdP'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    database: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Database'})
    schema: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Schema'})
    actions: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Actions'})
    snowflake_sql_statement: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Snowflake SQL Statement'})
    query_to_location: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Query To Location'})
    query_input: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Query Input'})
    storage_integration: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Storage Integration'})
    overwrite: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Overwrite'})
    file_format: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'File Format'})
    create_table_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Create Table Name'})
    query: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Query'})
    add_condition: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Add Condition'})
    stored_procedure_name: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Stored Procedure Name'})
    procedure_argument: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Procedure Argument'})
    activity_options: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Activity Options'})
    table_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Table Name'})
    from_location: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'From Location'})
    stage_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Stage Name'})
    from_storage_integration: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'From Storage Integration'})
    stage_url: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Stage URL'})
    copy_destination: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Copy Destination'})
    from_table: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'From Table'})
    pipe_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Pipe Name'})
    start_or_pause_pipe: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Start Or Pause Pipe'})
    stage_location: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Stage Location'})
    snowpipe_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Snowpipe Name'})
    days_back: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Days Back'})
    status_file_cloud_location_path: str = attrs.field(kw_only=True, default=None, metadata={
                                                       '_aapi_repr_': 'Status File Cloud Location Path'})
    stoarge_integration_for_location: str = attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'Stoarge Integration For Location'})
    load_sql_file: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Load SQL File'})
    statement_timeout__sec: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Statement Timeout (Sec)'})
    show_more_options: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Show More Options'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    role: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Role'})
    bindings: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Bindings'})
    warehouse: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Warehouse'})
    show_output: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Show Output'})
    polling_interval__sec: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Polling Interval (Sec)'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobGCPDataprep(Job):

    _type: str = attrs.field(init=False, default='Job:GCP Dataprep', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Dataprep'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    flow_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Flow Name'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    execute_job_with_idempotency_token: str = attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'Execute Job with Idempotency Token'})
    idempotency_token: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Idempotency Token'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAwsGlueDataBrew(Job):

    _type: str = attrs.field(init=False, default='Job:AWS Glue DataBrew', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Glue DataBrew'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Job Name'})
    output_job_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Output Job Logs'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobDatabricks(Job):

    _type: str = attrs.field(init=False, default='Job:Databricks', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Databricks'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    databricks_job_id: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Databricks Job ID'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    idempotency_token: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Idempotency Token'})
    show_tasks_output: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Show Tasks Output'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAwsAthena(Job):

    _type: str = attrs.field(init=False, default='Job:AWS Athena', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Athena'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    athena_client_request_token: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Athena Client Request Token'})
    db_catalog_name: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'DB Catalog Name'})
    database_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Database Name'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    query: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Query'})
    table_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Table Name'})
    prepared_query_name: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Prepared Query Name'})
    unload_file_type: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Unload File Type'})
    output_location: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Output Location'})
    workgroup: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Workgroup'})
    add_configurations: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Add Configurations'})
    s3_acl_option: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'S3 ACL Option'})
    encryption_options: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Encryption Options'})
    kms_key: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'KMS Key'})
    bucket_owner: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Bucket Owner'})
    show_json_output: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Show JSON Output'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tolerance'})
    no_perm: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'NoPerm'})


@attrs.define
class JobDBT(Job):

    _type: str = attrs.field(init=False, default='Job:DBT', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:DBT'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    dbt_job_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'DBT Job Id'})
    run_comment: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Run Comment'})
    override_job_commands: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Override Job Commands'})
    define_commands: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Define Commands'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAzureServiceBus(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Service Bus', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Service Bus'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    service_bus_namespace: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Service Bus Namespace'})
    queue_topic_name: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'QueueTopic Name'})
    message_format: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Message Format'})
    message_body: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Message Body'})


@attrs.define
class JobFivetran(Job):

    _type: str = attrs.field(init=False, default='Job:Fivetran', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Fivetran'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    job_type: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Job Type'})
    connection_id: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Connection ID'})
    connection_name: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Connection Name'})
    force_incremental_sync: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Force Incremental Sync'})
    transformation_id: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Transformation ID'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAwsBatch(Job):

    _type: str = attrs.field(init=False, default='Job:AWS Batch', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Batch'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    use_advanced_json_format: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Use Advanced JSON Format'})
    job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Job Name'})
    job_definition_and_revision: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Job Definition and Revision'})
    job_queue: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Job Queue'})
    container_overrides_command: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Container Overrides Command'})
    job_attempts: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Job Attempts'})
    execution_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Execution Timeout'})
    json_format: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'JSON Format'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


@attrs.define
class JobNetBackup(Job):

    _type: str = attrs.field(init=False, default='Job:NetBackup', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:NetBackup'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    json_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'JSON Parameters'})
    policy_name: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Policy Name'})
    schedule_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Schedule Name'})
    client_name: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Client Name'})
    keyword: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Keyword'})
    instance_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Instance Name'})
    database_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Database Name'})
    db_unique_name: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'DB Unique Name'})
    db_id: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'DB ID'})
    trial_backup: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Trial Backup'})
    output__management: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Output  Management'})
    restart_job_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Restart Job ID'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobGCPWorkflows(Job):

    _type: str = attrs.field(init=False, default='Job:GCP Workflows', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Workflows'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    project_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project ID'})
    location: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Location'})
    workflow_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Workflow Name'})
    parameters_json_input: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Parameters JSON Input'})
    execution_label: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Execution Label'})
    show_workflow_results: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Show Workflow Results'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobGCPBigQuery(Job):

    _type: str = attrs.field(init=False, default='Job:GCP BigQuery', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP BigQuery'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    project_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Project Name'})
    dataset_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Dataset Name'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    run_select_query_and_copy_to_table: str = attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'Run Select Query and Copy to Table'})
    table_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Table Name'})
    query_type: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Query Type'})
    sql_statement: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'SQL Statement'})
    load_query_from_file: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Load Query From File'})
    query_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Query Parameters'})
    routine: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Routine'})
    extract_as: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Extract As'})
    copy_operation_type: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Copy Operation Type'})
    source_tables_properties: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Source Tables Properties'})
    destination_source_bucket_uris: str = attrs.field(kw_only=True, default=None, metadata={
                                                      '_aapi_repr_': 'Destination/Source Bucket URIs'})
    destination_table_properties: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'Destination Table Properties'})
    show_load_options: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Show Load Options'})
    load_options: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Load Options'})
    job_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Job Timeout'})
    connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Connection Timeout'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


@attrs.define
class JobPagerDuty(Job):

    _type: str = attrs.field(init=False, default='Job:PagerDuty', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:PagerDuty'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    incident_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Incident ID'})
    email_address: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Email Address'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    duration: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Duration'})
    title: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Title'})
    service_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Service ID'})
    urgency: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Urgency'})
    incident_key: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Incident Key'})
    incident_body: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Incident Body'})


@attrs.define
class JobTalendDataManagement(Job):

    _type: str = attrs.field(init=False, default='Job:Talend Data Management', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Talend Data Management'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    task_plan_execution: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Task/Plan Execution'})
    task_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Task Name'})
    environment_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Environment ID'})
    workspace_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Workspace ID'})
    task_id: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Task ID'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    log_level: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Log Level'})
    bring_logs_to_output: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Bring logs to output'})
    task_polling_intervals: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Task Polling Intervals'})
    plan_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Plan Name'})
    plan_body_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Plan Body Parameters'})
    save_failed_plan_log: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Save Failed Plan Log'})
    plan_polling_intervals: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Plan Polling Intervals'})


@attrs.define
class JobMicroFocusLinux(Job):

    _type: str = attrs.field(init=False, default='Job:Micro Focus Linux', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Micro Focus Linux'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    jcl_filename: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'JCL Filename'})
    pds: str = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'PDS'})
    enable_jcl_variables: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Enable JCL Variables'})
    additional_variables: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Additional Variables'})
    restart_on_rerun: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Restart on Rerun'})
    from_step_proc: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'From Step/Proc'})
    to_step_proc: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'To Step/Proc'})
    recapture_abend_codes: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Recapture ABEND Codes'})
    recapture_cond_codes: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Recapture COND Codes'})
    auto_adjust_restart: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Auto Adjust Restart'})
    step_specific_condition_codes: str = attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'Step-Specific Condition Codes'})
    set_mf_ucc11: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Set MF_UCC11'})
    advanced_restart_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Advanced Restart Parameters'})
    rerun_job_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Rerun Job ID'})
    restart_with_modified_jcl: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Restart with Modified JCL'})
    modified_jcl_path_and_filename: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Modified JCL Path and Filename'})


@attrs.define
class JobAzureResourceManager(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Resource Manager', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Resource Manager'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    resource_group_name: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Resource Group Name'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    deployment_name: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Deployment Name'})
    deployment_properties: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Deployment Properties'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


@attrs.define
class JobAwsStepFunctions(Job):

    _type: str = attrs.field(init=False, default='Job:AWS Step Functions', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Step Functions'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    execution_name: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Execution Name'})
    state_machine_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'State Machine ARN'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    show_execution_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Show Execution Logs'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobInformaticaCS(Job):

    _type: str = attrs.field(init=False, default='Job:Informatica CS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Informatica CS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    task_type: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Task Type'})
    use_federation_id: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Use Federation ID'})
    task_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Task Name'})
    folder_path: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Folder Path'})
    taskflow_job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Taskflow Job Name'})
    task_flow_url: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'TaskFlow URL'})
    rerun_suspended_taskflow: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Rerun Suspended Taskflow'})
    rerun_run_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Rerun Run ID'})
    input_fields: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Input Fields'})
    call_back_url: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Call Back URL'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobTerraform(Job):

    _type: str = attrs.field(init=False, default='Job:Terraform', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Terraform'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    workspace_name: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Workspace Name'})
    run_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Run Name'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    workspace_params: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Workspace Params'})
    variable: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Variable'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobGCPFunctions(Job):

    _type: str = attrs.field(init=False, default='Job:GCP Functions', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Functions'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    project_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project ID'})
    location: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Location'})
    function_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Function Name'})
    function_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Function Parameters'})
    url_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'URL Parameters'})
    body: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Body'})
    api_version: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'API Version'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})
    get_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Get Logs'})


@attrs.define
class JobAzureLogicApps(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Logic Apps', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Logic Apps'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    workflow: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Workflow'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    get_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Get Logs'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


@attrs.define
class JobQlikCloud(Job):

    _type: str = attrs.field(init=False, default='Job:Qlik Cloud', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Qlik Cloud'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    reload_type: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Reload Type'})
    app_id: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'App ID'})
    print_log_to_output: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Print Log to Output'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tolerance'})


@attrs.define
class JobOCIVM(Job):

    _type: str = attrs.field(init=False, default='Job:OCI VM', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OCI VM'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    instance_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Instance ID'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobOCIDataIntegration(Job):

    _type: str = attrs.field(init=False, default='Job:OCI Data Integration', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OCI Data Integration'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    actions: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Actions'})
    workspace_ocid: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Workspace OCID'})
    application_key: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Application Key'})
    task_key: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Task Key'})
    task_run_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Task Run Name'})
    task_run_input_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Task Run Input Parameters'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobAwsDataPipeline(Job):

    _type: str = attrs.field(init=False, default='Job:AWS Data Pipeline', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Data Pipeline'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    pipeline_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Pipeline ID'})
    pipeline_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Pipeline Name'})
    pipeline_unique_id: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Pipeline Unique ID'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    trigger_created_pipeline: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Trigger Created Pipeline'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})


@attrs.define
class JobGCPCloudRun(Job):

    _type: str = attrs.field(init=False, default='Job:GCP Cloud Run', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Cloud Run'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    project_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project ID'})
    location: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Location'})
    job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Job Name'})
    overrides_specification: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Overrides Specification'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
