
from __future__ import annotations
import attrs
import typing
import enum
from aapi.bases import AAPIObject
from aapi.job import Job
from aapi.connectionprofile import ConnectionProfile


@attrs.define
class JobSAPIntegrationSuite(Job):

    _type: str = attrs.field(init=False, default='Job:SAP Integration Suite', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP Integration Suite'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    a_ii_flow_endpoint: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-iFlow Endpoint'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Failure Tolerance'})


@attrs.define
class JobAwsDataSync(Job):

    _type: str = attrs.field(init=False, default='Job:AWS DataSync', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS DataSync'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    ai_action: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Action'})
    task_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Task ARN'})
    ai_task_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Task ARN'})
    output_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Output Logs'})
    ai_output_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Output Logs'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    ai_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Parameters'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Failure Tolerance'})


@attrs.define
class JobIBMMQ(Job):

    _type: str = attrs.field(init=False, default='Job:IBM MQ', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:IBM MQ'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    correlation_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Correlation ID'})
    ai_correlation_id: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Correlation ID'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    ai_action: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Action'})
    job_output_assignment: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Job Output Assignment'})
    ai_job_output_assignment: str = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Job Output Assignment'})
    free_text_message: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Free Text Message'})
    ai_free_text_message: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Free Text Message'})
    variable_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Variable Name'})
    ai_variable_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Variable Name'})
    file_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'File Name'})
    ai_file_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-File Name'})
    use_predefined_message: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Use Predefined Message'})
    ai_use_predefined_message: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Use Predefined Message'})
    verification_poll_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Verification Poll Interval'})
    ai_verification_poll_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                                      '_aapi_repr_': 'AI-Verification Poll Interval'})
    a_iextraction: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-extraction'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Failure Tolerance'})


@attrs.define
class JobGCPVertexAI(Job):

    _type: str = attrs.field(init=False, default='Job:GCP Vertex AI', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Vertex AI'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    ai_action: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Action'})
    project_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Project Name'})
    ai_project_name: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Project Name'})
    instance_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Instance Name'})
    ai_instance_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Instance Name'})
    pipeline_run_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Pipeline Run Name'})
    ai_pipeline_run_name: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Pipeline Run Name'})
    zone: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Zone'})
    ai_zone: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Zone'})
    service_account: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Service Account'})
    ai_service_account: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Service Account'})
    pipeline_specification: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Pipeline Specification'})
    ai_pipeline_specification: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Pipeline Specification'})
    gcs_output_directory: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'GCS Output Directory'})
    ai_gcs_output_directory: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-GCS Output Directory'})
    add_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Add Parameters'})
    ai_add_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Add Parameters'})
    pipeline_runtime_paramaters: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Pipeline Runtime Paramaters'})
    ai_pipeline_runtime_paramaters: str = attrs.field(kw_only=True, default=None, metadata={
                                                       '_aapi_repr_': 'AI-Pipeline Runtime Paramaters'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Status Polling Frequency'})
    empty: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'EMPTY'})
    ai_e_m_p_t_y: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-EMPTY'})


@attrs.define
class JobAwsDynamoDB(Job):

    _type: str = attrs.field(init=False, default='Job:AWS DynamoDB', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS DynamoDB'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    ai_action: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Action'})
    statement: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Statement'})
    ai_statement: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Statement'})
    run_statement_with_parameter: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'Run Statement with Parameter'})
    ai_run_statement_with_parameter: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Run Statement with Parameter'})
    statement_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Statement Parameters'})
    ai_statement_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Statement Parameters'})
    transaction_statments: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Transaction Statments'})
    ai_transaction_statments: str = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Transaction Statments'})
    idempotency_token: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Idempotency Token'})
    ai_idempotency_token: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Idempotency Token'})
    export_format: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Export Format'})
    ai_export_format: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Export Format'})
    s3_bucket_name: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'S3 Bucket Name'})
    ai_s3_bucket_name: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-S3 Bucket Name'})
    s3_path_prefix: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'S3 Path Prefix'})
    ai_s3_path_prefix: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-S3 Path Prefix'})
    s3_bucket_owner_id: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'S3 Bucket Owner ID'})
    ai_s3_bucket_owner_id: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-S3 Bucket Owner ID'})
    table_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Table ARN'})
    ai_table_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Table ARN'})
    import_format: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Import Format'})
    ai_import_format: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Import Format'})
    import_compression_type: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Import Compression Type'})
    ai_import_compression_type: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'AI-Import Compression Type'})
    table_creation_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Table Creation Parameters'})
    ai_table_creation_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'AI-Table Creation Parameters'})
    table_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Table Name'})
    ai_table_name: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Table Name'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolarance_: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Failure Tolarance '})
    ai_failure_tolarance_: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Failure Tolarance '})
    a_iopen: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-open'})
    a_iclose: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-close'})
    a_iq1: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'AI-q1'})


@attrs.define
class JobSAPBuildProcessAutomation(Job):

    _type: str = attrs.field(init=False, default='Job:SAP Build Process Automation', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP Build Process Automation'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    flow_url: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Flow URL'})
    ai_flow_url: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Flow URL'})
    flow_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Flow Parameters'})
    ai_flow_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Flow Parameters'})
    fetch_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Fetch Logs'})
    ai_fetch_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Fetch Logs'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Failure Tolerance'})


@attrs.define
class JobAzureDevOps(Job):

    _type: str = attrs.field(init=False, default='Job:Azure DevOps', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure DevOps'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    project_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Project Name'})
    ai_project_name: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Project Name'})
    actions: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Actions'})
    ai_actions: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Actions'})
    pipeline_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Pipeline Id'})
    ai_pipeline_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Pipeline Id'})
    repository_path: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Repository Path'})
    ai_repository_path: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Repository Path'})
    variables: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Variables'})
    ai_variables: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Variables'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    ai_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Parameters'})
    stages_to_skip: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Stages To Skip'})
    ai_stages_to_skip: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Stages To Skip'})
    show_build_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Show Build Logs'})
    ai_show_build_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Show Build Logs'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Failure Tolerance'})
    a_iq1: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'AI-q1'})


@attrs.define
class JobGCPDeploymentManager(Job):

    _type: str = attrs.field(init=False, default='Job:GCP Deployment Manager', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Deployment Manager'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    project_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project ID'})
    ai_project_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Project ID'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    ai_action: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Action'})
    deployment_name: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Deployment Name'})
    ai_deployment_name: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Deployment Name'})
    yaml_config_content: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Yaml Config Content'})
    ai_yaml_config_content: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Yaml Config Content'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Failure Tolerance'})
    a_iq1: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'AI-q1'})


@attrs.define
class JobAwsRDS(Job):

    _type: str = attrs.field(init=False, default='Job:AWS RDS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS RDS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    ai_action: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Action'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    db_instance_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'DB Instance ID'})
    ai_db_instance_id: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-DB Instance ID'})
    db_cluster_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'DB Cluster ID'})
    ai_db_cluster_id: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-DB Cluster ID'})
    export_task_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Export Task ID'})
    ai_export_task_id: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Export Task ID'})
    snapshot_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Snapshot ID'})
    ai_snapshot_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Snapshot ID'})
    db_engine: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'DB Engine'})
    ai_db_engine: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-DB Engine'})
    iam_role_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'IAM Role ARN'})
    ai_iam_role_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-IAM Role ARN'})
    kms_key_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'KMS Key ID'})
    ai_kms_key_id: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-KMS Key ID'})
    source_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Source ARN'})
    ai_source_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Source ARN'})
    s3_bucket_name: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'S3 Bucket Name'})
    ai_s3_bucket_name: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-S3 Bucket Name'})
    s3_prefix: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'S3 Prefix'})
    ai_s3_prefix: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-S3 Prefix'})
    allocated_storage: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Allocated Storage'})
    ai_allocated_storage: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Allocated Storage'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance_: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Failure Tolerance  '})
    ai_failure_tolerance_: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Failure Tolerance  '})


@attrs.define
class JobSAPIBP(Job):

    _type: str = attrs.field(init=False, default='Job:SAP IBP', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP IBP'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    job_template_type: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'JobTemplate Type'})
    ai_job_template_type: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-JobTemplate Type'})
    job_template: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Job Template'})
    ai_job_template: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Job Template'})
    job_user: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Job User'})
    ai_job_user: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Job User'})
    job_text_suffix: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Job Text Suffix'})
    ai_job_text_suffix: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Job Text Suffix'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    ai_action: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Action'})
    restart_a_failed_application_job: str = attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'Restart a Failed Application Job'})
    ai_restart_a_failed_application_job: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Restart a Failed Application Job'})
    job_run_count: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Job Run Count'})
    ai_job_run_count: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Job Run Count'})
    ibpjobname: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'IBPJOBNAME'})
    ai_i_b_p_j_o_b_n_a_m_e: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-IBPJOBNAME'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Failure Tolerance'})


@attrs.define
class JobAwsEC2(Job):

    _type: str = attrs.field(init=False, default='Job:AWS EC2', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS EC2'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    operations: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Operations'})
    ai_operations: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Operations'})
    instance_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Instance ID'})
    ai_instance_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Instance ID'})
    placement_availability_zone: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Placement Availability Zone'})
    ai_placement_availability_zone: str = attrs.field(kw_only=True, default=None, metadata={
                                                       '_aapi_repr_': 'AI-Placement Availability Zone'})
    instance_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Instance Type'})
    ai_instance_type: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Instance Type'})
    instance_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Instance Name'})
    ai_instance_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Instance Name'})
    subnet_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Subnet ID'})
    ai_subnet_id: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Subnet ID'})
    key_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Key Name'})
    ai_key_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Key Name'})
    image_id: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Image ID'})
    ai_image_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Image ID'})
    number_of_copies: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Number of copies'})
    ai_number_of_copies: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Number of copies'})
    launch_template_id: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Launch Template ID'})
    ai_launch_template_id: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Launch Template ID'})
    tag_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Tag Name'})
    ai_tag_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Tag Name'})
    tag_value: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tag Value'})
    ai_tag_value: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Tag Value'})
    idempotent_token: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Idempotent Token'})
    ai_idempotent_token: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Idempotent Token'})
    tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tolerance'})
    ai_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Tolerance'})
    verification_poll_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Verification Poll Interval'})
    ai_verification_poll_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                                      '_aapi_repr_': 'AI-Verification Poll Interval'})
    get_instances_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Get Instances logs'})
    ai_get_instances_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Get Instances logs'})


@attrs.define
class JobAwsAutoScalingGroups(Job):

    _type: str = attrs.field(init=False, default='Job:AWS Auto Scaling Groups', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Auto Scaling Groups'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    instance_ids: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Instance IDs'})
    ai_instance_ids: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Instance IDs'})
    tag_key: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Tag Key'})
    ai_tag_key: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Tag Key'})
    tag_value: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tag Value'})
    ai_tag_value: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Tag Value'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    operations: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Operations'})
    ai_operations: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Operations'})
    auto_scaling_group_name: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Auto Scaling Group Name'})
    ai_auto_scaling_group_name: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'AI-Auto Scaling Group Name'})
    launch_template_name: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Launch Template Name'})
    ai_launch_template_name: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Launch Template Name'})
    launch_template_version: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Launch Template Version'})
    ai_launch_template_version: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'AI-Launch Template Version'})
    minimum_size: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Minimum Size'})
    ai_minimum_size: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Minimum Size'})
    maximum_size: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Maximum Size'})
    ai_maximum_size: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Maximum Size'})
    desired_capacity: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Desired Capacity'})
    ai_desired_capacity: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Desired Capacity'})
    url_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'URL Parameters'})
    ai_url_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-URL Parameters'})
    idempotent_token: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Idempotent Token'})
    ai_idempotent_token: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Idempotent Token'})
    tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tolerance'})
    ai_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Tolerance'})
    verification_poll_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Verification Poll Interval'})
    ai_verification_poll_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                                      '_aapi_repr_': 'AI-Verification Poll Interval'})
    get_instances_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Get Instances logs'})
    ai_get_instances_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Get Instances logs'})


@attrs.define
class JobRubrik(Job):

    _type: str = attrs.field(init=False, default='Job:Rubrik', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Rubrik'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    ai_action: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Action'})
    s_l_a_id: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'SLA ID'})
    ai_s_l_a_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-SLA ID'})
    vm_id: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'VM ID'})
    ai_vm_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-VM ID'})
    oracle_db_id: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Oracle DB ID'})
    ai_oracle_db_id: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Oracle DB ID'})
    n_a_s_id: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'NAS ID'})
    ai_n_a_s_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-NAS ID'})
    sql_db_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'SQL DB ID'})
    ai_sql_db_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-SQL DB ID'})
    delay_logs_retrieval: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Delay Logs Retrieval'})
    ai_delay_logs_retrieval: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Delay Logs Retrieval'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Status Polling Frequency'})
    year: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'YEAR'})
    ai_y_e_a_r: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-YEAR'})
    month: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'MONTH'})
    ai_m_o_n_t_h: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-MONTH'})
    day: str = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'DAY'})
    ai_d_a_y: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-DAY'})


@attrs.define
class JobAwsBackup(Job):

    _type: str = attrs.field(init=False, default='Job:AWS Backup', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Backup'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    ai_action: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Action'})
    windows_vss: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Windows VSS'})
    ai_windows_vss: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Windows VSS'})
    backup_vault_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Backup Vault Name'})
    ai_backup_vault_name: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Backup Vault Name'})
    role_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Role ARN'})
    ai_role_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Role ARN'})
    idempotency_token: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Idempotency Token'})
    ai_idempotency_token: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Idempotency Token'})
    resource_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Resource ARN'})
    ai_resource_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Resource ARN'})
    restore_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Restore Parameters'})
    ai_restore_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Restore Parameters'})
    recovery_point_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Recovery Point ARN'})
    ai_recovery_point_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Recovery Point ARN'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Status Polling Frequency'})
    a_iopen: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-open'})
    a_iclose: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-close'})
    a_iq1: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'AI-q1'})


@attrs.define
class JobAirbyte(Job):

    _type: str = attrs.field(init=False, default='Job:Airbyte', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Airbyte'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    connection_id: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Connection Id'})
    ai_connection_id: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Connection Id'})
    job_type: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Job Type'})
    ai_job_type: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Job Type'})
    show_results: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Show Results'})
    ai_show_results: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Show Results'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Failure Tolerance'})


@attrs.define
class JobGCPVM(Job):

    _type: str = attrs.field(init=False, default='Job:GCP VM', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP VM'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    project_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project ID'})
    ai_project_id: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Project ID'})
    zone: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Zone'})
    ai_zone: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Zone'})
    operation: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Operation'})
    ai_operation: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Operation'})
    tag_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Tag Name'})
    ai_tag_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Tag Name'})
    tag_value: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tag Value'})
    ai_tag_value: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Tag Value'})
    template_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Template Name'})
    ai_template_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Template Name'})
    instance_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Instance Name'})
    ai_instance_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Instance Name'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    ai_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Parameters'})
    verification_poll_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Verification Poll Interval'})
    ai_verification_poll_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                                      '_aapi_repr_': 'AI-Verification Poll Interval'})
    tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tolerance'})
    ai_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Tolerance'})
    get_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Get Logs'})
    ai_get_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Get Logs'})
    a_ib1: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'AI-b1'})
    a_ib2: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'AI-b2'})
    a_iinst: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-inst'})
    a_iinstend: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-instend'})


@attrs.define
class JobAwsAppRunner(Job):

    _type: str = attrs.field(init=False, default='Job:AWS App Runner', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS App Runner'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    ai_action: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Action'})
    service_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Service Arn'})
    ai_service_arn: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Service Arn'})
    output_job_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Output Job Logs'})
    ai_output_job_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Output Job Logs'})
    failure_tolerance_: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Failure Tolerance  '})
    ai_failure_tolerance_: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Failure Tolerance  '})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Status Polling Frequency'})


@attrs.define
class JobGCPDataFusion(Job):

    _type: str = attrs.field(init=False, default='Job:GCP Data Fusion', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Data Fusion'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    region: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Region'})
    ai_region: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Region'})
    project_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Project Name'})
    ai_project_name: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Project Name'})
    instance_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Instance Name'})
    ai_instance_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Instance Name'})
    name_space_id: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Name Space ID'})
    ai_name_space_id: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Name Space ID'})
    pipeline_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Pipeline Name'})
    ai_pipeline_name: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Pipeline Name'})
    runtime_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Runtime Parameters'})
    ai_runtime_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Runtime Parameters'})
    get_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Get Logs'})
    ai_get_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Get Logs'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Failure Tolerance'})


@attrs.define
class JobUIPath(Job):

    _type: str = attrs.field(init=False, default='Job:UI Path', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:UI Path'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    folder_type: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Folder Type'})
    ai_folder_type: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Folder Type'})
    folder_name: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Folder Name'})
    ai_folder_name: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Folder Name'})
    folder_id: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Folder Id'})
    ai_folder_id: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Folder Id'})
    process_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Process Name'})
    ai_process_name: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Process Name'})
    a_ipackagekey: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-packagekey'})
    robot_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Robot Name'})
    ai_robot_name: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Robot Name'})
    robot_id: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Robot Id'})
    ai_robot_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Robot Id'})
    optional_input_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Optional Input Parameters'})
    ai_optional_input_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'AI-Optional Input Parameters'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Status Polling Frequency'})
    a_ib1: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'AI-b1'})
    a_ib2: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'AI-b2'})
    a_igrant: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-grant'})
    a_ireftok: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-reftok'})
    a_iclid: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-clid'})
    a_iq1: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'AI-q1'})
    a_ireftok2: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-reftok2'})
    a_istrtinfo: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-strtinfo'})
    a_istrat: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-strat'})
    a_isqbl: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-sqbl'})
    a_isqbr: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-sqbr'})
    a_ibotargs: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-botargs'})
    a_iheadauth: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-headauth'})
    a_isetjobid: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-setjobid'})
    a_ijobkill: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-jobkill'})


@attrs.define
class JobDatadog(Job):

    _type: str = attrs.field(init=False, default='Job:Datadog', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Datadog'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    ai_action: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Action'})
    workflow_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Workflow ID'})
    ai_workflow_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Workflow ID'})
    workflow_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Workflow Parameters'})
    ai_workflow_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Workflow Parameters'})
    synthetics_test_type: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Synthetics Test Type'})
    ai_synthetics_test_type: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Synthetics Test Type'})
    test_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Test Parameters'})
    ai_test_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Test Parameters'})
    event_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Event Parameters'})
    ai_event_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Event Parameters'})
    incident_id: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Incident ID'})
    ai_incident_id: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Incident ID'})
    incident_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Incident Parameters'})
    ai_incident_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Incident Parameters'})
    delay_logs_retrieval: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Delay Logs Retrieval'})
    ai_delay_logs_retrieval: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Delay Logs Retrieval'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Failure Tolerance'})


@attrs.define
class JobAzureVirtualMachineScaleSets(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Virtual Machine Scale Sets', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Virtual Machine Scale Sets'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-ConnectionProfile'})
    virtual_machine_scale_set_name: str = attrs.field(kw_only=True, default=None, metadata={
                                                      '_aapi_repr_': 'Virtual Machine Scale Set Name'})
    ai_virtual_machine_scale_set_name: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Virtual Machine Scale Set Name'})
    action: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Action'})
    ai_action: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Action'})
    json_body: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'JSON Body'})
    ai_json_body: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-JSON Body'})
    instance_ids: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': "Instance ID's"})
    ai_instance_ids: str = attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': "AI-Instance ID's"})
    verification_polling_interval: str=attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Verification Polling Interval'})
    ai_verification_polling_interval: str=attrs.field(kw_only=True, default=None, metadata={
                                                       '_aapi_repr_': 'AI-Verification Polling Interval'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobAwsGlue(Job):




    _type: str=attrs.field(init=False, default='Job:AWS Glue', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Glue'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    glue_job_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Glue Job Name'})
    ai_glue_job_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Glue Job Name'})
    glue_workflow_name: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Glue Workflow Name'})
    ai_glue_workflow_name: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Glue Workflow Name'})
    crawler_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Crawler Name'})
    ai_crawler_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Crawler Name'})
    glue_job_arguments: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Glue Job Arguments'})
    ai_glue_job_arguments: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Glue Job Arguments'})
    arguments: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Arguments'})
    ai_arguments: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Arguments'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_iyes: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'AI-yes'})
    a_ino: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-no'})
    a_ijobkey: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-jobkey'})
    a_ib1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b1'})
    a_ib2: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b2'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})
    a_irunkey: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-runkey'})
    a_icanrunids: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-canrunids'})
    a_ibr1: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'AI-br1'})
    a_ibr2: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'AI-br2'})
    output_job_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Output Job Logs'})
    ai_output_job_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Output Job Logs'})
    log_type: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Log type'})
    ai_log_type: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Log type'})


@ attrs.define
class JobApacheAirflow(Job):




    _type: str=attrs.field(init=False, default='Job:Apache Airflow', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Apache Airflow'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    airflow_rest_version: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Airflow REST Version'})
    ai_airflow_rest_version: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Airflow REST Version'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    d_a_g_name: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'DAG Name'})
    ai_d_a_g_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-DAG Name'})
    d_a_g_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'DAG Run ID'})
    ai_d_a_g_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-DAG Run ID'})
    rerun_d_a_g_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Rerun DAG ID'})
    ai_rerun_d_a_g_id: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Rerun DAG ID'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    logical_date: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Logical Date'})
    ai_logical_date: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Logical Date'})
    only_failed_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Only Failed Tasks'})
    ai_only_failed_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Only Failed Tasks'})
    include_subdags: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Include Subdags'})
    ai_include_subdags: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Include Subdags'})
    include_upstream: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Include Upstream'})
    ai_include_upstream: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Include Upstream'})
    include_downstream: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Include Downstream'})
    ai_include_downstream: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Include Downstream'})
    url_request_path: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'URL Request Path'})
    ai_url_request_path: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-URL Request Path'})
    json: str=attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'JSON'})
    ai_json: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'AI-JSON'})
    switch_to_rerun: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Switch to Rerun'})
    ai_switch_to_rerun: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Switch to Rerun'})
    keep_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Keep Run ID'})
    ai_keep_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Keep Run ID'})
    get_tasks_output: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Get Tasks Output'})
    ai_get_tasks_output: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Get Tasks Output'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobAwsCloudFormation(Job):




    _type: str=attrs.field(init=False, default='Job:AWS CloudFormation', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS CloudFormation'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    stack_name: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Stack Name'})
    ai_stack_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Stack Name'})
    stack_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Stack Parameters'})
    ai_stack_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Stack Parameters'})
    template_body: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Template Body'})
    ai_template_body: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Template Body'})
    template_url: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Template URL'})
    ai_template_url: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Template URL'})
    role_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Role ARN'})
    ai_role_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Role ARN'})
    capabilities_type: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Capabilities Type'})
    ai_capabilities_type: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Capabilities Type'})
    enable_termination_protection: str=attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Enable Termination Protection'})
    ai_enable_termination_protection: str=attrs.field(kw_only=True, default=None, metadata={
                                                       '_aapi_repr_': 'AI-Enable Termination Protection'})
    on_failure: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'On Failure'})
    ai_on_failure: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-On Failure'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobMicrosoftPowerAutomate(Job):




    _type: str=attrs.field(init=False, default='Job:Microsoft Power Automate', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Microsoft Power Automate'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    environment_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Environment ID'})
    ai_environment_id: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Environment ID'})
    flow_name: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Flow Name'})
    ai_flow_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Flow Name'})
    endpoint_url: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Endpoint URL'})
    ai_endpoint_url: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Endpoint URL'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    fetch_detailed_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Fetch Detailed Logs'})
    ai_fetch_detailed_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Fetch Detailed Logs'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobAzureBatchAccounts(Job):




    _type: str=attrs.field(init=False, default='Job:Azure Batch Accounts', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Batch Accounts'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    batch_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Batch Job ID'})
    ai_batch_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Batch Job ID'})
    task_id_prefix: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Task ID Prefix'})
    ai_task_id_prefix: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Task ID Prefix'})
    task_command_line: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Task Command Line'})
    ai_task_command_line: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Task Command Line'})
    max_wall_clock_time: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Max Wall Clock Time'})
    ai_max_wall_clock_time: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Max Wall Clock Time'})
    max_wall_time_digits: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Max Wall Time Digits'})
    ai_max_wall_time_digits: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Max Wall Time Digits'})
    max_wall_time_unit: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Max Wall Time Unit'})
    ai_max_wall_time_unit: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Max Wall Time Unit'})
    max_task_retry_count: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Max Task Retry Count'})
    ai_max_task_retry_count: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Max Task Retry Count'})
    retry_number: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Retry Number'})
    ai_retry_number: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Retry Number'})
    retention_time: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Retention Time'})
    ai_retention_time: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Retention Time'})
    retention_time_digits: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Retention Time Digits'})
    ai_retention_time_digits: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Retention Time Digits'})
    retention_time_unit: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Retention Time Unit'})
    ai_retention_time_unit: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Retention Time Unit'})
    append_log_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Append Log to Output'})
    ai_append_log_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Append Log to Output'})
    status_polling_interval: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Status polling interval'})
    ai_status_polling_interval: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Status polling interval'})
    task_id_variable: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Task ID variable'})
    ai_task_id_variable: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Task ID variable'})
    content_type: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Content-Type'})
    ai_content_type: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Content-Type'})
    a_iempty1: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-empty1'})
    a_iempty2: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-empty2'})
    a_iempty3: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-empty3'})


@ attrs.define
class JobAzureFunctions(Job):




    _type: str=attrs.field(init=False, default='Job:Azure Functions', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Functions'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    function_app: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Function App'})
    ai_function_app: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Function App'})
    azure_resource: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Azure Resource'})
    ai_azure_resource: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Azure Resource'})
    azure_resource_scope: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Azure Resource Scope'})
    ai_azure_resource_scope: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Azure Resource Scope'})
    function_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Function Name'})
    ai_function_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Function Name'})
    optional_input_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Optional Input Parameters'})
    ai_optional_input_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'AI-Optional Input Parameters'})
    function_type: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Function Type'})
    ai_function_type: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Function Type'})
    verification_poll_intervall: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Verification Poll Intervall'})
    ai_verification_poll_intervall: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'AI-Verification Poll Intervall'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    api_v_e_r_s_i_o_n: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'API-VERSION'})
    ai_api_v_e_r_s_i_o_n: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-API-VERSION'})


@ attrs.define
class JobAwsAppFlow(Job):




    _type: str=attrs.field(init=False, default='Job:AWS AppFlow', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS AppFlow'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    flow_name: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Flow Name'})
    ai_flow_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Flow Name'})
    flow_name__iam: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Flow Name - IAM'})
    ai_flow_name__iam: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Flow Name - IAM'})
    flow_name__assume_role: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Flow Name - Assume Role'})
    ai_flow_name__assume_role: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Flow Name - Assume Role'})
    trigger_flow_with_idempotency_token: str=attrs.field(kw_only=True, default=None, metadata={
                                                         '_aapi_repr_': 'Trigger Flow with Idempotency Token'})
    ai_trigger_flow_with_idempotency_token: str=attrs.field(kw_only=True, default=None, metadata={
                                                             '_aapi_repr_': 'AI-Trigger Flow with Idempotency Token'})
    client_token: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Client Token'})
    ai_client_token: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Client Token'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobAwsEMR(Job):




    _type: str=attrs.field(init=False, default='Job:AWS EMR', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS EMR'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    cluster_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Cluster Id'})
    ai_cluster_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Cluster Id'})
    notebook_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Notebook ID'})
    ai_notebook_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Notebook ID'})
    relative_path: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Relative Path'})
    ai_relative_path: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Relative Path'})
    notebook_execution_name: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Notebook Execution Name'})
    ai_notebook_execution_name: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Notebook Execution Name'})
    service_role: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Service Role'})
    ai_service_role: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Service Role'})
    use_advanced_json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Use Advanced JSON Format'})
    ai_use_advanced_json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Use Advanced JSON Format'})
    json_body: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'JSON Body'})
    ai_json_body: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-JSON Body'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Tolerance'})
    ai_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Tolerance'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})


@ attrs.define
class JobDataiku(Job):




    _type: str=attrs.field(init=False, default='Job:Dataiku', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Dataiku'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    project_key: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Project Key'})
    ai_project_key: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Project Key'})
    job_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Job Parameters'})
    ai_job_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Job Parameters'})
    scenario_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Scenario ID'})
    ai_scenario_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Scenario ID'})
    scenario_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Scenario Parameters'})
    ai_scenario_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Scenario Parameters'})
    dataset_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Dataset Name'})
    ai_dataset_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Dataset Name'})
    fetch_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Fetch Logs'})
    ai_fetch_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Fetch Logs'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobTableau(Job):




    _type: str=attrs.field(init=False, default='Job:Tableau', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Tableau'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    datasource_name: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Datasource Name'})
    ai_datasource_name: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Datasource Name'})
    flow_name: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Flow Name'})
    ai_flow_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Flow Name'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})
    a_ib1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b1'})
    a_ib2: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b2'})


@ attrs.define
class JobAzureVM(Job):




    _type: str=attrs.field(init=False, default='Job:Azure VM', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure VM'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    vm_name: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'VM Name'})
    ai_vm_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-VM Name'})
    operation: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Operation'})
    ai_operation: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Operation'})
    tag_name: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Tag Name'})
    ai_tag_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Tag Name'})
    tag_value: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Tag Value'})
    ai_tag_value: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Tag Value'})
    input_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Input Parameters'})
    ai_input_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Input Parameters'})
    verification_poll_interval: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Verification Poll Interval'})
    ai_verification_poll_interval: str=attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Verification Poll Interval'})
    a_ib1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b1'})
    a_ib2: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b2'})
    delete_vm_os_disk: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Delete VM OS Disk'})
    ai_delete_vm_os_disk: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Delete VM OS Disk'})
    tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Tolerance'})
    ai_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Tolerance'})
    api_v_e_r_s_i_o_n: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'API-VERSION'})
    ai_api_v_e_r_s_i_o_n: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-API-VERSION'})
    get_logs: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Get Logs'})
    ai_get_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Get Logs'})


@ attrs.define
class JobGCPDataplex(Job):




    _type: str=attrs.field(init=False, default='Job:GCP Dataplex', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Dataplex'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Project ID'})
    ai_project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Project ID'})
    location: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Location'})
    ai_location: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Location'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    scan_name: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Scan Name'})
    ai_scan_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Scan Name'})
    lake_name: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Lake Name'})
    ai_lake_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Lake Name'})
    task_name: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Task Name'})
    ai_task_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Task Name'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_iq2: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q2'})
    a_iq3: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q3'})


@ attrs.define
class JobGCPComposer(Job):




    _type: str=attrs.field(init=False, default='Job:GCP Composer', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Composer'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    airflow_rest_version: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Airflow REST Version'})
    ai_airflow_rest_version: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Airflow REST Version'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    d_a_g_name: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'DAG Name'})
    ai_d_a_g_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-DAG Name'})
    d_a_g_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'DAG Run ID'})
    ai_d_a_g_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-DAG Run ID'})
    rerun_d_a_g_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Rerun DAG ID'})
    ai_rerun_d_a_g_id: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Rerun DAG ID'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    logical_date: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Logical Date'})
    ai_logical_date: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Logical Date'})
    only_failed_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Only Failed Tasks'})
    ai_only_failed_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Only Failed Tasks'})
    include_subdags: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Include Subdags'})
    ai_include_subdags: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Include Subdags'})
    include_upstream: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Include Upstream'})
    ai_include_upstream: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Include Upstream'})
    include_downstream: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Include Downstream'})
    ai_include_downstream: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Include Downstream'})
    switch_to_rerun: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Switch to Rerun'})
    ai_switch_to_rerun: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Switch to Rerun'})
    keep_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Keep Run ID'})
    ai_keep_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Keep Run ID'})
    get_tasks_output: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Get Tasks Output'})
    ai_get_tasks_output: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Get Tasks Output'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobApacheNiFi(Job):




    _type: str=attrs.field(init=False, default='Job:Apache NiFi', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Apache NiFi'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    processor_group_id: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Processor Group ID'})
    ai_processor_group_id: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Processor Group ID'})
    processor_id: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Processor ID'})
    ai_processor_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Processor ID'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    disconnected_node_ack: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Disconnected Node Ack'})
    ai_disconnected_node_ack: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Disconnected Node Ack'})
    parameters_: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Parameters '})
    ai_parameters_: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Parameters '})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobSAPBTPScheduler(Job):




    _type: str=attrs.field(init=False, default='Job:SAP BTP Scheduler', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP BTP Scheduler'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    s_a_p_job_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'SAP Job Name'})
    ai_s_a_p_job_name: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-SAP Job Name'})
    job_name: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Job Name'})
    ai_job_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Job Name'})
    job_description: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Job Description'})
    ai_job_description: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Job Description'})
    job_url: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Job URL'})
    ai_job_url: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Job URL'})
    http_method: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'HTTP Method'})
    ai_http_method: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-HTTP Method'})
    notification_on_success: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Notification On Success'})
    ai_notification_on_success: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Notification On Success'})
    notification_on_error: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Notification On Error'})
    ai_notification_on_error: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Notification On Error'})
    job_data: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Job Data'})
    ai_job_data: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Job Data'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobArgoWorkflows(Job):




    _type: str=attrs.field(init=False, default='Job:Argo Workflows', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Argo Workflows'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    argo_workflow_action: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Argo Workflow Action'})
    ai_argo_workflow_action: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Argo Workflow Action'})
    namespace: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Namespace'})
    ai_namespace: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Namespace'})
    workflow_template_name: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Workflow Template Name'})
    ai_workflow_template_name: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Workflow Template Name'})
    resource_kind: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Resource Kind'})
    ai_resource_kind: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Resource Kind'})
    workflow_u_id: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Workflow UID'})
    ai_workflow_u_id: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Workflow UID'})
    runtime_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Runtime Parameters'})
    ai_runtime_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Runtime Parameters'})
    get_node_details: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Get Node Details'})
    ai_get_node_details: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Get Node Details'})
    switch_to_retry: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Switch to Retry'})
    ai_switch_to_retry: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Switch to Retry'})
    retry_switch_action: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Retry Switch Action'})
    ai_retry_switch_action: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Retry Switch Action'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobGCPEventArc(Job):




    _type: str=attrs.field(init=False, default='Job:GCP EventArc', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP EventArc'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    operation: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Operation'})
    ai_operation: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Operation'})
    trigger_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Trigger Name'})
    ai_trigger_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Trigger Name'})
    service_account__email_format: str=attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Service Account (Email Format)'})
    ai_service_account__email_format: str=attrs.field(kw_only=True, default=None, metadata={
                                                       '_aapi_repr_': 'AI-Service Account (Email Format)'})
    event_filters: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Event Filters'})
    ai_event_filters: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Event Filters'})
    destination: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Destination'})
    ai_destination: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Destination'})
    service: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Service'})
    ai_service: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Service'})
    region: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Region'})
    ai_region: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Region'})
    path: str=attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'Path'})
    ai_path: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'AI-Path'})
    destination_uri: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Destination URI'})
    ai_destination_uri: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Destination URI'})
    network_attachment: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Network Attachment'})
    ai_network_attachment: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Network Attachment'})
    cluster: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Cluster'})
    ai_cluster: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Cluster'})
    location: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Location'})
    ai_location: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Location'})
    namespace: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Namespace'})
    ai_namespace: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Namespace'})
    workflow: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Workflow'})
    ai_workflow: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Workflow'})
    project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Project ID'})
    ai_project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Project ID'})
    a_iq: str=attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'AI-q'})
    use_advanced_json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Use Advanced JSON Format'})
    ai_use_advanced_json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Use Advanced JSON Format'})
    json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'JSON Format'})
    ai_json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-JSON Format'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    a_ib1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b1'})
    a_ib2: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b2'})
    a_iqb1: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'AI-qb1'})
    a_iqb2: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'AI-qb2'})


@ attrs.define
class JobGCPDataflow(Job):




    _type: str=attrs.field(init=False, default='Job:GCP Dataflow', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Dataflow'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Project ID'})
    ai_project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Project ID'})
    region: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Region'})
    ai_region: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Region'})
    template_type: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Template Type'})
    ai_template_type: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Template Type'})
    template_location_gs_: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Template Location (gs://)'})
    ai_template_location_gs_: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Template Location (gs://)'})
    parameters__json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Parameters (JSON Format)'})
    ai_parameters__json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Parameters (JSON Format)'})
    verification_poll_interval_in_seconds: str=attrs.field(kw_only=True, default=None, metadata={
                                                           '_aapi_repr_': 'Verification Poll Interval (in seconds)'})
    ai_verification_poll_interval_in_seconds: str=attrs.field(kw_only=True, default=None, metadata={
                                                               '_aapi_repr_': 'AI-Verification Poll Interval (in seconds)'})
    log_level: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Log Level'})
    ai_log_level: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Log Level'})


@ attrs.define
class JobAwsMWAA(Job):




    _type: str=attrs.field(init=False, default='Job:AWS MWAA', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS MWAA'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    airflow_rest_version: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Airflow REST Version'})
    ai_airflow_rest_version: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Airflow REST Version'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    m_w_a_a_environment_name: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'MWAA Environment Name'})
    ai_m_w_a_a_environment_name: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-MWAA Environment Name'})
    d_a_g_name: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'DAG Name'})
    ai_d_a_g_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-DAG Name'})
    d_a_g_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'DAG Run ID'})
    ai_d_a_g_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-DAG Run ID'})
    rerun_d_a_g_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Rerun DAG ID'})
    ai_rerun_d_a_g_id: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Rerun DAG ID'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    logical_date: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Logical Date'})
    ai_logical_date: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Logical Date'})
    only_failed: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Only Failed'})
    ai_only_failed: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Only Failed'})
    include_subdags: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Include Subdags'})
    ai_include_subdags: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Include Subdags'})
    include_upstream: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Include Upstream'})
    ai_include_upstream: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Include Upstream'})
    include_downstream: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Include Downstream'})
    ai_include_downstream: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Include Downstream'})
    url_request_path: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'URL Request Path'})
    ai_url_request_path: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-URL Request Path'})
    json: str=attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'JSON'})
    ai_json: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'AI-JSON'})
    switch_to_rerun: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Switch to Rerun'})
    ai_switch_to_rerun: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Switch to Rerun'})
    keep_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Keep Run ID'})
    ai_keep_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Keep Run ID'})
    get_tasks_output: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Get Tasks Output'})
    ai_get_tasks_output: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Get Tasks Output'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobAwsBedrock(Job):




    _type: str=attrs.field(init=False, default='Job:AWS Bedrock', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Bedrock'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    flow_id: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Flow Id'})
    ai_flow_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Flow Id'})
    alias: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Alias'})
    ai_alias: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Alias'})
    flow_text_input: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Flow Text Input'})
    ai_flow_text_input: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Flow Text Input'})
    input_node_name: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Input Node Name'})
    ai_input_node_name: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Input Node Name'})
    initial_node_output_name: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Initial Node Output Name'})
    ai_initial_node_output_name: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Initial Node Output Name'})
    latency: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Latency'})
    ai_latency: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Latency'})
    show_execution_events: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Show Execution Events'})
    ai_show_execution_events: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Show Execution Events'})
    event_type_presentation: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Event Type Presentation'})
    ai_event_type_presentation: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Event Type Presentation'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobVeritasNetBackup(Job):




    _type: str=attrs.field(init=False, default='Job:Veritas NetBackup', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Veritas NetBackup'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    json_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'JSON Parameters'})
    ai_json_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-JSON Parameters'})
    create_jobs_per_client: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Create Jobs Per Client'})
    ai_create_jobs_per_client: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Create Jobs Per Client'})
    policy_name: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Policy Name'})
    ai_policy_name: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Policy Name'})
    client_name: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Client Name'})
    ai_client_name: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Client Name'})
    schedule_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Schedule Name'})
    ai_schedule_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Schedule Name'})
    keyword: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Keyword'})
    ai_keyword: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Keyword'})
    instance_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Instance Name'})
    ai_instance_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Instance Name'})
    database_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Database Name'})
    ai_database_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Database Name'})
    db_unique_name: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'DB Unique Name'})
    ai_db_unique_name: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-DB Unique Name'})
    db_id: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'DB ID'})
    ai_db_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-DB ID'})
    trial_backup: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Trial Backup'})
    ai_trial_backup: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Trial Backup'})
    output__management: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Output  Management'})
    ai_output__management: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Output  Management'})
    restart_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Restart Job ID'})
    ai_restart_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Restart Job ID'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobMatillion(Job):




    _type: str=attrs.field(init=False, default='Job:Matillion', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Matillion'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    matillion_job_type: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Matillion Job Type'})
    ai_matillion_job_type: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Matillion Job Type'})
    project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Project Id'})
    ai_project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Project Id'})
    environment_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Environment Name'})
    ai_environment_name: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Environment Name'})
    pipeline_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Pipeline Name'})
    ai_pipeline_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Pipeline Name'})
    group_name: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Group Name'})
    ai_group_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Group Name'})
    project_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project Name'})
    ai_project_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Project Name'})
    version_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Version Name'})
    ai_version_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Version Name'})
    job_name: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Job Name'})
    ai_job_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Job Name'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Tolerance'})
    ai_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Tolerance'})


@ attrs.define
class JobGCPDataproc(Job):




    _type: str=attrs.field(init=False, default='Job:GCP Dataproc', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Dataproc'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Project ID'})
    ai_project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Project ID'})
    account_region: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Account Region'})
    ai_account_region: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Account Region'})
    dataproc_task_type: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Dataproc task type'})
    ai_dataproc_task_type: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Dataproc task type'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    batch_id: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Batch ID'})
    ai_batch_id: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Batch ID'})
    request_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Request ID'})
    ai_request_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Request ID'})
    workflow_template: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Workflow Template'})
    ai_workflow_template: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Workflow Template'})
    parameters__json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Parameters (JSON Format)'})
    ai_parameters__json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Parameters (JSON Format)'})
    verification_poll_interval_in_seconds: str=attrs.field(kw_only=True, default=None, metadata={
                                                           '_aapi_repr_': 'Verification Poll Interval (in seconds)'})
    ai_verification_poll_interval_in_seconds: str=attrs.field(kw_only=True, default=None, metadata={
                                                               '_aapi_repr_': 'AI-Verification Poll Interval (in seconds)'})
    tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Tolerance'})
    ai_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Tolerance'})
    a_ib1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b1'})
    a_ib2: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b2'})
    interactive_session_id: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Interactive Session ID'})
    ai_interactive_session_id: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Interactive Session ID'})


@ attrs.define
class JobAzureSynapse(Job):




    _type: str=attrs.field(init=False, default='Job:Azure Synapse', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Synapse'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    pipeline_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Pipeline Name'})
    ai_pipeline_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Pipeline Name'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    a_iapi_version: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-api version'})
    status_polling_interval: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Status polling interval'})
    ai_status_polling_interval: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Status polling interval'})
    a_icompdet_1: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-compdet_1'})
    a_icompdet_2: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-compdet_2'})
    a_icompdet_3: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-compdet_3'})
    a_ibrackets_left: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-brackets_left'})
    a_ibrackets_right: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-brackets_right'})


@ attrs.define
class JobVMwareByBroadcom(Job):




    _type: str=attrs.field(init=False, default='Job:VMware By Broadcom', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware By Broadcom'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    configuration_options: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Configuration Options'})
    ai_configuration_options: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Configuration Options'})
    power_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Power Tasks'})
    ai_power_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Power Tasks'})
    reconfigure_action: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Reconfigure Action'})
    ai_reconfigure_action: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Reconfigure Action'})
    snapshot_operations: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Snapshot Operations'})
    ai_snapshot_operations: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Snapshot Operations'})
    vm_logical_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'VM Logical Name'})
    ai_vm_logical_name: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-VM Logical Name'})
    vm_location: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'VM Location'})
    ai_vm_location: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-VM Location'})
    resource_pool: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Resource Pool'})
    ai_resource_pool: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Resource Pool'})
    folder: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Folder'})
    ai_folder: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Folder'})
    e_s_xi_host: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'ESXi Host'})
    ai_e_s_xi_host: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-ESXi Host'})
    datacenter: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Datacenter'})
    ai_datacenter: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Datacenter'})
    cluster: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Cluster'})
    ai_cluster: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Cluster'})
    template_library_item_id: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Template Library Item ID'})
    ai_template_library_item_id: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Template Library Item ID'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    placement_json: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Placement JSON'})
    ai_placement_json: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Placement JSON'})
    hot_remove: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Hot Remove'})
    ai_hot_remove: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Hot Remove'})
    hot_add: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Hot Add'})
    ai_hot_add: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Hot Add'})
    cpu_count: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'CPU Count'})
    ai_cpu_count: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-CPU Count'})
    cores_per_socket: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Cores Per Socket'})
    ai_cores_per_socket: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Cores Per Socket'})
    size_in_mi_b: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Size In MiB'})
    ai_size_in_mi_b: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Size In MiB'})
    snapshot_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Snapshot Name'})
    ai_snapshot_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Snapshot Name'})
    snapshot_description: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Snapshot Description'})
    ai_snapshot_description: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Snapshot Description'})
    memory_dump: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Memory Dump'})
    ai_memory_dump: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Memory Dump'})
    quiesce: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Quiesce'})
    ai_quiesce: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Quiesce'})
    snapshot_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Snapshot ID'})
    ai_snapshot_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Snapshot ID'})
    vm_mo_id: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'VM MoId'})
    ai_vm_mo_id: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-VM MoId'})
    release_schema: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Release Schema'})
    ai_release_schema: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Release Schema'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobCommunicationSuite(Job):




    _type: str=attrs.field(init=False, default='Job:Communication Suite', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Communication Suite'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    application_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Application Name'})
    ai_application_name: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Application Name'})
    slack_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Slack Parameters'})
    ai_slack_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Slack Parameters'})
    telegram_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Telegram Parameters'})
    ai_telegram_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Telegram Parameters'})
    silent_message: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Silent Message'})
    ai_silent_message: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Silent Message'})
    protect_content: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Protect Content'})
    ai_protect_content: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Protect Content'})
    whats_app_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'WhatsApp Parameters'})
    ai_whats_app_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-WhatsApp Parameters'})
    teams_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Teams Parameters'})
    ai_teams_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Teams Parameters'})


@ attrs.define
class JobAzureMachineLearning(Job):




    _type: str=attrs.field(init=False, default='Job:Azure Machine Learning', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Machine Learning'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    workspace_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Workspace Name'})
    ai_workspace_name: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Workspace Name'})
    resource_group_name: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Resource Group Name'})
    ai_resource_group_name: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Resource Group Name'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    pipeline_endpoint_id: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Pipeline Endpoint ID'})
    ai_pipeline_endpoint_id: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Pipeline Endpoint ID'})
    job_id: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Job ID'})
    ai_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Job ID'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    compute_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Compute Name'})
    ai_compute_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Compute Name'})
    compute_action: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Compute Action'})
    ai_compute_action: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Compute Action'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_ib1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b1'})
    a_ib2: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b2'})


@ attrs.define
class JobAzureDataFactory(Job):




    _type: str=attrs.field(init=False, default='Job:Azure Data Factory', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Data Factory'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    resource_group_name: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Resource Group Name'})
    ai_resource_group_name: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Resource Group Name'})
    data_factory_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Data Factory Name'})
    ai_data_factory_name: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Data Factory Name'})
    pipeline_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Pipeline Name'})
    ai_pipeline_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Pipeline Name'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_icompdet_1: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-compdet_1'})
    a_icompdet_2: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-compdet_2'})
    a_ibrackets_left: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-brackets_left'})
    a_ibrackets_right: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-brackets_right'})
    restart_on_rerun: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Restart on Rerun'})
    ai_restart_on_rerun: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Restart on Rerun'})
    reference_pipeline_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Reference Pipeline Run ID'})
    ai_reference_pipeline_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'AI-Reference Pipeline Run ID'})
    a_iempty: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'AI-empty'})


@ attrs.define
class JobWebServicesSOAP(Job):


    @ attrs.define
    class SoapRequest(AAPIObject):




        request_definition: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'RequestDefinition'})
        file_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'FileName'})
        soap_request_field: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'SoapRequestField'})

    @ attrs.define
    class AISoapRequest(AAPIObject):




        request_definition: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'RequestDefinition'})
        file_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'FileName'})
        soap_request_field: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'SoapRequestField'})



    _type: str=attrs.field(init=False, default='Job:Web Services SOAP', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Web Services SOAP'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    endpoint_url: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Endpoint URL'})
    ai_endpoint_url: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Endpoint URL'})
    soap_action: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'SOAP Action'})
    ai_soap_action: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-SOAP Action'})
    soap_request: SoapRequest=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'SoapRequest'})
    ai_soap_request: AISoapRequest=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-SoapRequest'})
    http_headers: typing.List[str]=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'HTTP Headers'})
    ai_http_headers: typing.List[str]=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-HTTP Headers'})
    output_handling: typing.List[str]=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'OutputHandling'})
    ai_output_handling: typing.List[str]=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-OutputHandling'})
    connection_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Connection Timeout'})
    ai_connection_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Connection Timeout'})
    append_request: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Append Request'})
    ai_append_request: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Append Request'})
    append_response: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Append Response'})
    ai_append_response: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Append Response'})


@ attrs.define
class JobOCIDataScience(Job):




    _type: str=attrs.field(init=False, default='Job:OCI Data Science', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OCI Data Science'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    model_deployment_id: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Model Deployment ID'})
    ai_model_deployment_id: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Model Deployment ID'})
    notebook_session_id: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Notebook Session ID'})
    ai_notebook_session_id: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Notebook Session ID'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobSAPDatasphere(Job):




    _type: str=attrs.field(init=False, default='Job:SAP Datasphere', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP Datasphere'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    space_id: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Space ID'})
    ai_space_id: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Space ID'})
    datasphere_task_type: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Datasphere Task Type'})
    ai_datasphere_task_type: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Datasphere Task Type'})
    task_chain_name: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Task Chain Name'})
    ai_task_chain_name: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Task Chain Name'})
    replication_flow_name: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Replication Flow Name'})
    ai_replication_flow_name: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Replication Flow Name'})
    correlation_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Correlation ID'})
    ai_correlation_id: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Correlation ID'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobBoomiAtomsphere(Job):




    _type: str=attrs.field(init=False, default='Job:Boomi Atomsphere', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Boomi Atomsphere'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    process_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Process Name'})
    ai_process_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Process Name'})
    atom_name: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Atom Name'})
    ai_atom_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Atom Name'})
    polling_interval_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Polling Interval Frequency'})
    ai_polling_interval_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Polling Interval Frequency'})
    tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Tolerance'})
    ai_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Tolerance'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})
    use_advanced_json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Use Advanced JSON Format'})
    ai_use_advanced_json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Use Advanced JSON Format'})
    json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'JSON Format'})
    ai_json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-JSON Format'})


@ attrs.define
class JobOracleJDEdwardsEnterpriseOne(Job):




    _type: str=attrs.field(init=False, default='Job:Oracle JD Edwards EnterpriseOne', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Oracle JD Edwards EnterpriseOne'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    report_name: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Report Name'})
    ai_report_name: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Report Name'})
    report_version: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Report Version'})
    ai_report_version: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Report Version'})
    environment: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Environment'})
    ai_environment: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Environment'})
    device_name: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'DeviceName'})
    ai_device_name: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-DeviceName'})
    orchestrator: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Orchestrator'})
    ai_orchestrator: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Orchestrator'})
    input: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Input'})
    ai_input: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Input'})
    query_device_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Query Device Name'})
    ai_query_device_name: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Query Device Name'})
    query_target_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Query Target Name'})
    ai_query_target_name: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Query Target Name'})
    query_target_type: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Query Target Type'})
    ai_query_target_type: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Query Target Type'})
    query_data_service_type: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Query Data Service Type'})
    ai_query_data_service_type: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Query Data Service Type'})
    query_max_page_size: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Query Max Page Size'})
    ai_query_max_page_size: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Query Max Page Size'})
    query_return_control_ids: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Query Return Control IDs'})
    ai_query_return_control_ids: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Query Return Control IDs'})
    query: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Query'})
    ai_query: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Query'})
    aggregation: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Aggregation'})
    ai_aggregation: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Aggregation'})
    u_i_automation_device_name: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'UI Automation Device Name'})
    ai_u_i_automation_device_name: str=attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-UI Automation Device Name'})
    u_i_automation_form_name: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'UI Automation Form Name'})
    ai_u_i_automation_form_name: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-UI Automation Form Name'})
    u_i_automation_output_type: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'UI Automation Output Type'})
    ai_u_i_automation_output_type: str=attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-UI Automation Output Type'})
    u_i_automation_form_service_action: str=attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'UI Automation Form Service Action'})
    ai_u_i_automation_form_service_action: str=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-UI Automation Form Service Action'})
    u_i_automation_return_control_ids: str=attrs.field(kw_only=True, default=None, metadata={
                                                       '_aapi_repr_': 'UI Automation Return Control IDs'})
    ai_u_i_automation_return_control_ids: str=attrs.field(kw_only=True, default=None, metadata={
                                                           '_aapi_repr_': 'AI-UI Automation Return Control IDs'})
    u_i_automation_query: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'UI Automation Query'})
    ai_u_i_automation_query: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-UI Automation Query'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Tolerance'})
    ai_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Tolerance'})


@ attrs.define
class JobAzureDatabricks(Job):




    _type: str=attrs.field(init=False, default='Job:Azure Databricks', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Databricks'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    databricks_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Databricks Job ID'})
    ai_databricks_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Databricks Job ID'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    idempotency_token: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Idempotency Token'})
    ai_idempotency_token: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Idempotency Token'})
    show_tasks_output: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Show Tasks Output'})
    ai_show_tasks_output: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Show Tasks Output'})
    repair_on_rerun: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Repair on Rerun'})
    ai_repair_on_rerun: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Repair on Rerun'})
    reference_job_run_id__: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Reference Job Run ID    '})
    ai_reference_job_run_id__: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Reference Job Run ID    '})
    latest_repair_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Latest Repair ID'})
    ai_latest_repair_id: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Latest Repair ID'})
    rerun_all_failed_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Rerun all Failed Tasks'})
    ai_rerun_all_failed_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Rerun all Failed Tasks'})
    rerun_dependent_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Rerun Dependent Tasks'})
    ai_rerun_dependent_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Rerun Dependent Tasks'})
    rerun_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Rerun Tasks'})
    ai_rerun_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Rerun Tasks'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobSAPAnalyticsCloud(Job):




    _type: str=attrs.field(init=False, default='Job:SAP Analytics Cloud', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP Analytics Cloud'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    calendar_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Calendar ID'})
    ai_calendar_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Calendar ID'})
    a_istatus: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-status'})
    a_inotify: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-notify'})
    a_iauto_activate: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-autoActivate'})
    model_id: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Model ID'})
    ai_model_id: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Model ID'})
    import_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Import Parameters'})
    ai_import_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Import Parameters'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobGitHubActions(Job):




    _type: str=attrs.field(init=False, default='Job:GitHub Actions', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GitHub Actions'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    pull_request_actions: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Pull Request Actions'})
    ai_pull_request_actions: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Pull Request Actions'})
    workflow_action: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Workflow Action'})
    ai_workflow_action: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Workflow Action'})
    rerun_options: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Rerun Options'})
    ai_rerun_options: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Rerun Options'})
    repository_owner: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Repository Owner'})
    ai_repository_owner: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Repository Owner'})
    repository_name: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Repository Name'})
    ai_repository_name: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Repository Name'})
    workflow_file_name: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Workflow File Name'})
    ai_workflow_file_name: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Workflow File Name'})
    reference: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Reference'})
    ai_reference: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Reference'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    run_attempt_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Run Attempt ID'})
    ai_run_attempt_id: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Run Attempt ID'})
    job_id: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Job ID'})
    ai_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Job ID'})
    get_workflow_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Get Workflow Logs'})
    ai_get_workflow_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Get Workflow Logs'})
    p_r_title: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'PR Title'})
    ai_p_r_title: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-PR Title'})
    p_r_head: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'PR Head'})
    ai_p_r_head: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-PR Head'})
    p_r_base: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'PR Base'})
    ai_p_r_base: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-PR Base'})
    p_r_body: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'PR Body'})
    ai_p_r_body: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-PR Body'})
    draft: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Draft'})
    ai_draft: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Draft'})
    maintainer_can_modify: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Maintainer Can Modify'})
    ai_maintainer_can_modify: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Maintainer Can Modify'})
    p_r_id: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'PR ID'})
    ai_p_r_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-PR ID'})
    commit_title: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Commit Title'})
    ai_commit_title: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Commit Title'})
    commit_message: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Commit Message'})
    ai_commit_message: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Commit Message'})
    commit_s_h_a: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Commit SHA'})
    ai_commit_s_h_a: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Commit SHA'})
    merge_method: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Merge Method'})
    ai_merge_method: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Merge Method'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobAwsECS(Job):




    _type: str=attrs.field(init=False, default='Job:AWS ECS', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS ECS'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    ecs_cluster_name: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ECS Cluster Name'})
    ai_ecs_cluster_name: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ECS Cluster Name'})
    ecs_task_definition: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'ECS Task Definition'})
    ai_ecs_task_definition: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-ECS Task Definition'})
    task_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Task ARN'})
    ai_task_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Task ARN'})
    stop_reason: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Stop Reason'})
    ai_stop_reason: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Stop Reason'})
    launch_type: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Launch Type'})
    ai_launch_type: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Launch Type'})
    assign_public_ip: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Assign Public IP'})
    ai_assign_public_ip: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Assign Public IP'})
    network_security_groups: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Network Security Groups'})
    ai_network_security_groups: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Network Security Groups'})
    network_subnets: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Network Subnets'})
    ai_network_subnets: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Network Subnets'})
    overrides: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Overrides'})
    ai_overrides: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Overrides'})
    override_container: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Override Container'})
    ai_override_container: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Override Container'})
    override_command: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Override Command'})
    ai_override_command: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Override Command'})
    environment_variables: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Environment Variables'})
    ai_environment_variables: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Environment Variables'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    get_logs: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Get Logs'})
    ai_get_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Get Logs'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobAutomationAnywhere(Job):




    _type: str=attrs.field(init=False, default='Job:Automation Anywhere', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Automation Anywhere'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    automation_type: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Automation Type'})
    ai_automation_type: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Automation Type'})
    bot_to_run: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Bot to run'})
    ai_bot_to_run: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Bot to run'})
    process_uri_path: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Process Uri path'})
    ai_process_uri_path: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Process Uri path'})
    process_to_run: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Process to run'})
    ai_process_to_run: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Process to run'})
    bot_input_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Bot input parameters'})
    ai_bot_input_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Bot input parameters'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    connection_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Connection timeout'})
    ai_connection_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Connection timeout'})


@ attrs.define
class JobLangGraph(Job):




    _type: str=attrs.field(init=False, default='Job:LangGraph', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:LangGraph'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Project ID'})
    ai_project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Project ID'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    deployment_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Deployment Parameters'})
    ai_deployment_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Deployment Parameters'})
    deployment_id: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Deployment ID'})
    ai_deployment_id: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Deployment ID'})
    revision_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Revision ID'})
    ai_revision_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Revision ID'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobRabbitMQ(Job):




    _type: str=attrs.field(init=False, default='Job:RabbitMQ', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:RabbitMQ'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    vhost: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Vhost'})
    ai_vhost: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Vhost'})
    exchange: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Exchange'})
    ai_exchange: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Exchange'})
    routing_key: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Routing Key'})
    ai_routing_key: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Routing Key'})
    message_to_publish: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Message to Publish'})
    ai_message_to_publish: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Message to Publish'})
    message_encoding: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Message Encoding'})
    ai_message_encoding: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Message Encoding'})
    properties: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Properties'})
    ai_properties: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Properties'})
    queue: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Queue'})
    ai_queue: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Queue'})


@ attrs.define
class JobJenkins(Job):




    _type: str=attrs.field(init=False, default='Job:Jenkins', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Jenkins'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    pipeline_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Pipeline Name'})
    ai_pipeline_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Pipeline Name'})
    add_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Add Parameters'})
    ai_add_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Add Parameters'})
    parameters: typing.List[str]=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Parameters'})
    ai_parameters: typing.List[str]=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Parameters'})
    add_branch_name: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Add Branch Name'})
    ai_add_branch_name: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Add Branch Name'})
    branch_name: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Branch Name'})
    ai_branch_name: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Branch Name'})
    fetch_console_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Fetch Console Logs'})
    ai_fetch_console_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Fetch Console Logs'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobAwsBedrockAgentCore(Job):




    _type: str=attrs.field(init=False, default='Job:AWS Bedrock AgentCore', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Bedrock AgentCore'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    agent_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Agent ARN'})
    ai_agent_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Agent ARN'})
    qualifier: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Qualifier'})
    ai_qualifier: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Qualifier'})
    content_type_input: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Content-Type Input'})
    ai_content_type_input: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Content-Type Input'})
    agent_core_runtime_session_id: str=attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'AgentCore Runtime Session ID'})
    ai_agent_core_runtime_session_id: str=attrs.field(kw_only=True, default=None, metadata={
                                                       '_aapi_repr_': 'AI-AgentCore Runtime Session ID'})
    input: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Input'})
    ai_input: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Input'})


@ attrs.define
class JobMicrosoftFabric(Job):




    _type: str=attrs.field(init=False, default='Job:Microsoft Fabric', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Microsoft Fabric'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    workspace_id: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Workspace ID'})
    ai_workspace_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Workspace ID'})
    job_type: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Job Type'})
    ai_job_type: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Job Type'})
    item_id: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Item ID'})
    ai_item_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Item ID'})
    execution_data_body: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Execution Data Body'})
    ai_execution_data_body: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Execution Data Body'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_iempty: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'AI-empty'})


@ attrs.define
class JobVeeamBackup(Job):




    _type: str=attrs.field(init=False, default='Job:Veeam Backup', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Veeam Backup'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    backup_u_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Backup UID'})
    ai_backup_u_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Backup UID'})
    retry: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Retry'})
    ai_retry: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Retry'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobAwsRedshift(Job):




    _type: str=attrs.field(init=False, default='Job:AWS Redshift', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Redshift'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    actions: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Actions'})
    ai_actions: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Actions'})
    workgroup_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Workgroup Name'})
    ai_workgroup_name: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Workgroup Name'})
    secret_manager_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Secret Manager ARN'})
    ai_secret_manager_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Secret Manager ARN'})
    database: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Database'})
    ai_database: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Database'})
    table_name: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Table Name'})
    ai_table_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Table Name'})
    load_redshift_sql_statement: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Load Redshift SQL Statement'})
    ai_load_redshift_sql_statement: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'AI-Load Redshift SQL Statement'})
    procedure_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Procedure Name'})
    ai_procedure_name: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Procedure Name'})
    procedure_arguments: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Procedure Arguments'})
    ai_procedure_arguments: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Procedure Arguments'})
    s3_bucket_uri: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'S3 Bucket URI'})
    ai_s3_bucket_uri: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-S3 Bucket URI'})
    file_format: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'File Format'})
    ai_file_format: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-File Format'})
    use_iam_role_for_s3_access: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Use IAM Role For S3 Access'})
    ai_use_iam_role_for_s3_access: str=attrs.field(kw_only=True, default=None, metadata={
                                                      '_aapi_repr_': 'AI-Use IAM Role For S3 Access'})
    iam_role_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'IAM Role ARN'})
    ai_iam_role_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-IAM Role ARN'})
    show_statement_results: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Show Statement Results'})
    ai_show_statement_results: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Show Statement Results'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Tolerance'})
    ai_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Tolerance'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})


@ attrs.define
class JobMicrosoftPowerBI(Job):




    _type: str=attrs.field(init=False, default='Job:Microsoft Power BI', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Microsoft Power BI'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    dataset_refresh_pipeline_deployment: str=attrs.field(kw_only=True, default=None, metadata={
                                                         '_aapi_repr_': 'Dataset Refresh/ Pipeline Deployment'})
    ai_dataset_refresh_pipeline_deployment: str=attrs.field(kw_only=True, default=None, metadata={
                                                             '_aapi_repr_': 'AI-Dataset Refresh/ Pipeline Deployment'})
    workspace_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Workspace Name'})
    ai_workspace_name: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Workspace Name'})
    workspace_id: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Workspace ID'})
    ai_workspace_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Workspace ID'})
    dataset_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Dataset ID'})
    ai_dataset_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Dataset ID'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    connection_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Connection Timeout'})
    ai_connection_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Connection Timeout'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    pipeline_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Pipeline ID'})
    ai_pipeline_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Pipeline ID'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})


@ attrs.define
class JobAzureBackup(Job):




    _type: str=attrs.field(init=False, default='Job:Azure Backup', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Backup'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    vault_resource_group: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Vault Resource Group'})
    ai_vault_resource_group: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Vault Resource Group'})
    vault_name: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Vault Name'})
    ai_vault_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Vault Name'})
    vm_resource_group: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'VM Resource Group'})
    ai_vm_resource_group: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-VM Resource Group'})
    vm_name: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'VM Name'})
    ai_vm_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-VM Name'})
    policy_name: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Policy Name'})
    ai_policy_name: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Policy Name'})
    include_or_exclude_disks: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Include Or Exclude Disks'})
    ai_include_or_exclude_disks: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Include Or Exclude Disks'})
    disk_list: str=attrs.field(kw_only=True, default=None, metadata={
                               '_abstract_aapi_container_': True})
    ai_disk_list: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_abstract_aapi_container_': True})
    restore_to_latest_recovery_point: str=attrs.field(kw_only=True, default=None, metadata={
                                                      '_aapi_repr_': 'Restore to Latest Recovery Point'})
    ai_restore_to_latest_recovery_point: str=attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'AI-Restore to Latest Recovery Point'})
    recovery_point_name: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Recovery Point Name'})
    ai_recovery_point_name: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Recovery Point Name'})
    a_iopen: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'AI-open'})
    a_iclose: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'AI-close'})
    storage_account_name: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Storage Account Name'})
    ai_storage_account_name: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Storage Account Name'})
    restore_region: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Restore Region'})
    ai_restore_region: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Restore Region'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance_: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Failure Tolerance '})
    ai_failure_tolerance_: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Failure Tolerance '})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})


@ attrs.define
class JobSnowflake(Job):




    _type: str=attrs.field(init=False, default='Job:Snowflake', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Snowflake'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    database: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Database'})
    ai_database: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Database'})
    schema: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Schema'})
    ai_schema: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Schema'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    snowflake_sql_statement: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Snowflake SQL Statement'})
    ai_snowflake_sql_statement: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Snowflake SQL Statement'})
    query_to_location: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Query to Location'})
    ai_query_to_location: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Query to Location'})
    query_input: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Query Input'})
    ai_query_input: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Query Input'})
    storage_integration: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Storage Integration'})
    ai_storage_integration: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Storage Integration'})
    overwrite: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Overwrite'})
    ai_overwrite: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Overwrite'})
    file_format: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'File Format'})
    ai_file_format: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-File Format'})
    create_table_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Create Table Name'})
    ai_create_table_name: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Create Table Name'})
    query: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Query'})
    ai_query: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Query'})
    add_condition: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Add Condition'})
    ai_add_condition: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Add Condition'})
    stored_procedure_name: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Stored Procedure Name'})
    ai_stored_procedure_name: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Stored Procedure Name'})
    procedure_argument: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Procedure Argument'})
    ai_procedure_argument: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Procedure Argument'})
    activity_options: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Activity Options'})
    ai_activity_options: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Activity Options'})
    table_name: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Table Name'})
    ai_table_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Table Name'})
    from_location: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'From Location'})
    ai_from_location: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-From Location'})
    stage_name: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Stage Name'})
    ai_stage_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Stage Name'})
    from_storage_integration: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'From Storage Integration'})
    ai_from_storage_integration: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-From Storage Integration'})
    stage_url: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Stage URL'})
    ai_stage_url: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Stage URL'})
    copy_destination: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Copy Destination'})
    ai_copy_destination: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Copy Destination'})
    from_table: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'From Table'})
    ai_from_table: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-From Table'})
    snowpipe_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Snowpipe Name'})
    ai_snowpipe_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Snowpipe Name'})
    start_or_pause_snowpipe: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Start or Pause Snowpipe'})
    ai_start_or_pause_snowpipe: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Start or Pause Snowpipe'})
    stage_location: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Stage Location'})
    ai_stage_location: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Stage Location'})
    days_back: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Days Back'})
    ai_days_back: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Days Back'})
    status_file_cloud_location_path: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'Status File Cloud Location Path'})
    ai_status_file_cloud_location_path: str=attrs.field(kw_only=True, default=None, metadata={
                                                         '_aapi_repr_': 'AI-Status File Cloud Location Path'})
    stoarge_integration_for_location: str=attrs.field(kw_only=True, default=None, metadata={
                                                      '_aapi_repr_': 'Stoarge Integration for Location'})
    ai_stoarge_integration_for_location: str=attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'AI-Stoarge Integration for Location'})
    load_sql_file: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Load SQL File'})
    ai_load_sql_file: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Load SQL File'})
    statement_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Statement Timeout'})
    ai_statement_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Statement Timeout'})
    show_more_options: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Show More Options'})
    ai_show_more_options: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Show More Options'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    role: str=attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'Role'})
    ai_role: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'AI-Role'})
    bindings: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Bindings'})
    ai_bindings: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Bindings'})
    warehouse: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Warehouse'})
    ai_warehouse: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Warehouse'})
    show_output: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Show Output'})
    ai_show_output: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Show Output'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})


@ attrs.define
class JobMicrosoftPowerBISP(Job):




    _type: str=attrs.field(init=False, default='Job:Microsoft Power BI SP', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Microsoft Power BI SP'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    workspace_id: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Workspace ID'})
    ai_workspace_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Workspace ID'})
    dataset_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Dataset ID'})
    ai_dataset_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Dataset ID'})
    dataflow_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Dataflow ID'})
    ai_dataflow_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Dataflow ID'})
    workspace_id__s_p: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Workspace ID - SP'})
    ai_workspace_id__s_p: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Workspace ID - SP'})
    dataset_id__s_p: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Dataset ID - SP'})
    ai_dataset_id__s_p: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Dataset ID - SP'})
    dataflow_id__s_p: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Dataflow ID - SP'})
    ai_dataflow_id__s_p: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Dataflow ID - SP'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    parameters_enhanced: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Parameters Enhanced'})
    ai_parameters_enhanced: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Parameters Enhanced'})
    pipeline_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Pipeline ID'})
    ai_pipeline_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Pipeline ID'})
    pipeline_id__s_p: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Pipeline ID - SP'})
    ai_pipeline_id__s_p: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Pipeline ID - SP'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobAwsDatabaseMigrationService(Job):




    _type: str=attrs.field(init=False, default='Job:AWS Database Migration Service', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Database Migration Service'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    data_migration_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Data Migration ARN'})
    ai_data_migration_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Data Migration ARN'})
    start_type: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Start Type'})
    ai_start_type: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Start Type'})
    database_migration_task_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Database Migration Task ARN'})
    ai_database_migration_task_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                                       '_aapi_repr_': 'AI-Database Migration Task ARN'})
    output_job_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Output Job Logs'})
    ai_output_job_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Output Job Logs'})
    failure_tolerance_: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Failure Tolerance  '})
    ai_failure_tolerance_: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Failure Tolerance  '})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})


@ attrs.define
class JobMicroFocusWindows(Job):




    _type: str=attrs.field(init=False, default='Job:Micro Focus Windows', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Micro Focus Windows'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    jcl_filename: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'JCL Filename'})
    ai_jcl_filename: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-JCL Filename'})
    pds: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'PDS'})
    ai_pds: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-PDS'})
    enable_jcl_variables: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Enable JCL Variables'})
    ai_enable_jcl_variables: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Enable JCL Variables'})
    additional_variables: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Additional Variables'})
    ai_additional_variables: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Additional Variables'})
    restart_on_rerun: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Restart on Rerun'})
    ai_restart_on_rerun: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Restart on Rerun'})
    from_step_proc: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'From Step/Proc'})
    ai_from_step_proc: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-From Step/Proc'})
    to_step_proc: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'To Step/Proc'})
    ai_to_step_proc: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-To Step/Proc'})
    recapture_abend_codes: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Recapture ABEND Codes'})
    ai_recapture_abend_codes: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Recapture ABEND Codes'})
    recapture_cond_codes: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Recapture COND Codes'})
    ai_recapture_cond_codes: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Recapture COND Codes'})
    auto_adjust_restart: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Auto Adjust Restart'})
    ai_auto_adjust_restart: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Auto Adjust Restart'})
    step_specific_condition_codes: str=attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Step-Specific Condition Codes'})
    ai_step_specific_condition_codes: str=attrs.field(kw_only=True, default=None, metadata={
                                                       '_aapi_repr_': 'AI-Step-Specific Condition Codes'})
    set_mf_ucc11: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Set MF_UCC11'})
    ai_set_mf_ucc11: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Set MF_UCC11'})
    advanced_restart_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Advanced Restart Parameters'})
    ai_advanced_restart_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'AI-Advanced Restart Parameters'})
    rerun_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Rerun Job ID'})
    ai_rerun_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Rerun Job ID'})
    restart_with_modified_jcl: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Restart with Modified JCL'})
    ai_restart_with_modified_jcl: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'AI-Restart with Modified JCL'})
    modified_jcl_path_and_filename: str=attrs.field(kw_only=True, default=None, metadata={
                                                      '_aapi_repr_': 'Modified JCL Path and Filename'})
    ai_modified_jcl_path_and_filename: str=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Modified JCL Path and Filename'})
    a_iempty_attribute: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-empty attribute'})


@ attrs.define
class JobGCPManagedInstanceGroups(Job):




    _type: str=attrs.field(init=False, default='Job:GCP Managed Instance Groups', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Managed Instance Groups'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Project ID'})
    ai_project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Project ID'})
    zone: str=attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'Zone'})
    ai_zone: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'AI-Zone'})
    instance_group_name: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Instance Group Name'})
    ai_instance_group_name: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Instance Group Name'})
    instance_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Instance Name'})
    ai_instance_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Instance Name'})
    minimal_action: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Minimal Action'})
    ai_minimal_action: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Minimal Action'})
    most_disruptive_allowed_action: str=attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'Most Disruptive Allowed Action'})
    ai_most_disruptive_allowed_action: str=attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'AI-Most Disruptive Allowed Action'})
    json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'JSON Format'})
    ai_json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-JSON Format'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})


@ attrs.define
class JobOCIDataTransforms(Job):




    _type: str=attrs.field(init=False, default='Job:OCI Data Transforms', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OCI Data Transforms'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    task_type: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Task Type'})
    ai_task_type: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Task Type'})
    object_id: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Object Id'})
    ai_object_id: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Object Id'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobAzureAIFoundry(Job):




    _type: str=attrs.field(init=False, default='Job:Azure AI Foundry', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure AI Foundry'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    project_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project Name'})
    ai_project_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Project Name'})
    application_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Application Name'})
    ai_application_name: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Application Name'})
    input: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Input'})
    ai_input: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Input'})


@ attrs.define
class JobIBMDataStageLinux(Job):




    _type: str=attrs.field(init=False, default='Job:IBM DataStage Linux', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:IBM DataStage Linux'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    project: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Project'})
    ai_project: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Project'})
    datastage_job: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Datastage Job'})
    ai_datastage_job: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Datastage Job'})
    job_invocation_id__optional: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Job Invocation ID (Optional)'})
    ai_job_invocation_id__optional: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'AI-Job Invocation ID (Optional)'})
    parameters_type: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Parameters Type'})
    ai_parameters_type: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Parameters Type'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    parameter_file: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Parameter File'})
    ai_parameter_file: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Parameter File'})
    stop_stages_after_number_of_rows: str=attrs.field(kw_only=True, default=None, metadata={
                                                      '_aapi_repr_': 'Stop Stages After Number Of Rows'})
    ai_stop_stages_after_number_of_rows: str=attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'AI-Stop Stages After Number Of Rows'})
    abort_job_after_number_of_warnings: str=attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'Abort Job After Number Of Warnings'})
    ai_abort_job_after_number_of_warnings: str=attrs.field(kw_only=True, default=None, metadata={
                                                            '_aapi_repr_': 'AI-Abort Job After Number Of Warnings'})
    append_log_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Append Log To Output'})
    ai_append_log_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Append Log To Output'})
    run_in_restart_mode: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Run In Restart Mode'})
    ai_run_in_restart_mode: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Run In Restart Mode'})
    reset_job_before_run: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Reset Job Before Run'})
    ai_reset_job_before_run: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Reset Job Before Run'})
    empty1: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Empty1'})
    ai_empty1: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Empty1'})


@ attrs.define
class JobApacheKafkaViaConfluent(Job):




    _type: str=attrs.field(init=False, default='Job:Apache Kafka via Confluent', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Apache Kafka via Confluent'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    topic_name: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Topic Name'})
    ai_topic_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Topic Name'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})


@ attrs.define
class JobAlibabaECS(Job):




    _type: str=attrs.field(init=False, default='Job:Alibaba ECS', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Alibaba ECS'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    instance_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Instance ID'})
    ai_instance_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Instance ID'})
    tag_name: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Tag Name'})
    ai_tag_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Tag Name'})
    tag_value: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Tag Value'})
    ai_tag_value: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Tag Value'})
    verification_poll_interval: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Verification Poll Interval'})
    ai_verification_poll_interval: str=attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Verification Poll Interval'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobSnowflakeCortexAI(Job):




    _type: str=attrs.field(init=False, default='Job:Snowflake Cortex AI', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Snowflake Cortex AI'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    database: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Database'})
    ai_database: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Database'})
    schema: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Schema'})
    ai_schema: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Schema'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    cortex_ai_agent_name: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Cortex AI Agent Name'})
    ai_cortex_ai_agent_name: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Cortex AI Agent Name'})
    input_text: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Input Text'})
    ai_input_text: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Input Text'})
    tool_names: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Tool Names'})
    ai_tool_names: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Tool Names'})
    fail_job_on_response_text: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Fail job on response text'})
    ai_fail_job_on_response_text: str=attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'AI-Fail job on response text'})
    m_c_p_server_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'MCP Server Name'})
    ai_m_c_p_server_name: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-MCP Server Name'})
    m_c_p_server_request_id: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'MCP Server Request ID'})
    ai_m_c_p_server_request_id: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-MCP Server Request ID'})
    m_c_p_server_tool_name: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'MCP Server Tool Name'})
    ai_m_c_p_server_tool_name: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-MCP Server Tool Name'})
    m_c_p_server_tool_arguments: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'MCP Server Tool Arguments'})
    ai_m_c_p_server_tool_arguments: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'AI-MCP Server Tool Arguments'})
    timeout: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Timeout'})
    ai_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Timeout'})


@ attrs.define
class JobAnsibleAWX(Job):




    _type: str=attrs.field(init=False, default='Job:Ansible AWX', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Ansible AWX'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    job_template_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Job Template Name'})
    ai_job_template_name: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Job Template Name'})
    job_template_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Job Template ID'})
    ai_job_template_id: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Job Template ID'})
    workflow_template_name: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Workflow Template Name'})
    ai_workflow_template_name: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Workflow Template Name'})
    workflow_template_id: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Workflow Template ID'})
    ai_workflow_template_id: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Workflow Template ID'})
    inventory: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Inventory'})
    ai_inventory: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Inventory'})
    inventory_source: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Inventory Source'})
    ai_inventory_source: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Inventory Source'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    project_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project Name'})
    ai_project_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Project Name'})
    project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Project ID'})
    ai_project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Project ID'})
    output_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Output Logs'})
    ai_output_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Output Logs'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobGCPBatch(Job):




    _type: str=attrs.field(init=False, default='Job:GCP Batch', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Batch'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    service_account__email_format: str=attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Service Account (Email Format)'})
    ai_service_account__email_format: str=attrs.field(kw_only=True, default=None, metadata={
                                                       '_aapi_repr_': 'AI-Service Account (Email Format)'})
    project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Project ID'})
    ai_project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Project ID'})
    region: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Region'})
    ai_region: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Region'})
    override_region: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Override Region'})
    ai_override_region: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Override Region'})
    allowed_locations: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Allowed Locations'})
    ai_allowed_locations: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Allowed Locations'})
    job_name: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Job Name'})
    ai_job_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Job Name'})
    priority: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Priority'})
    ai_priority: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Priority'})
    runnable_type: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Runnable Type'})
    ai_runnable_type: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Runnable Type'})
    task_script_text: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Task Script Text'})
    ai_task_script_text: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Task Script Text'})
    container_image_uri: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Container Image URI'})
    ai_container_image_uri: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Container Image URI'})
    entry_point: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Entry Point'})
    ai_entry_point: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Entry Point'})
    override_commands: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Override Commands'})
    ai_override_commands: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Override Commands'})
    commands: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Commands'})
    ai_commands: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Commands'})
    container_volumes: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Container Volumes'})
    ai_container_volumes: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Container Volumes'})
    a_iq: str=attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'AI-q'})
    cpu: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'CPU'})
    ai_cpu: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-CPU'})
    memory: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Memory'})
    ai_memory: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Memory'})
    maximum_retry_count: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Maximum Retry Count'})
    ai_maximum_retry_count: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Maximum Retry Count'})
    instance_policy: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Instance Policy'})
    ai_instance_policy: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Instance Policy'})
    machine_type: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Machine Type'})
    ai_machine_type: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Machine Type'})
    provisioning_model: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Provisioning Model'})
    ai_provisioning_model: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Provisioning Model'})
    machine_template: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Machine Template'})
    ai_machine_template: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Machine Template'})
    log_policy: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Log Policy'})
    ai_log_policy: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Log Policy'})
    use_advanced_json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Use Advanced JSON Format'})
    ai_use_advanced_json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Use Advanced JSON Format'})
    json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'JSON Format'})
    ai_json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-JSON Format'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    a_ib1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b1'})
    a_ib2: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b2'})


@ attrs.define
class JobAwsMainframeModernization(Job):




    _type: str=attrs.field(init=False, default='Job:AWS Mainframe Modernization', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Mainframe Modernization'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    application_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Application Name'})
    ai_application_name: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Application Name'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    jcl_name: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'JCL Name'})
    ai_jcl_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-JCL Name'})
    rerun_execution_id: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Rerun Execution ID'})
    ai_rerun_execution_id: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Rerun Execution ID'})
    secret_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Secret ARN'})
    ai_secret_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Secret ARN'})
    from_step: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'From Step'})
    ai_from_step: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-From Step'})
    from_proc_step: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'From Proc Step'})
    ai_from_proc_step: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-From Proc Step'})
    to_step: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'To Step'})
    ai_to_step: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-To Step'})
    to_proc_step: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'To Proc Step'})
    ai_to_proc_step: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-To Proc Step'})
    retrieve_cloud_watch_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Retrieve CloudWatch Logs'})
    ai_retrieve_cloud_watch_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'AI-Retrieve CloudWatch Logs'})
    delay_logs_retrieval_: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Delay Logs Retrieval '})
    ai_delay_logs_retrieval_: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Delay Logs Retrieval '})
    application_action: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Application Action'})
    ai_application_action: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Application Action'})
    client_token: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Client Token'})
    ai_client_token: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Client Token'})
    application_version: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Application Version'})
    ai_application_version: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Application Version'})
    environment_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Environment ID'})
    ai_environment_id: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Environment ID'})
    latest_application_version: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Latest Application Version'})
    ai_latest_application_version: str=attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Latest Application Version'})
    definition_s3_location: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Definition S3 Location'})
    ai_definition_s3_location: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Definition S3 Location'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})


@ attrs.define
class JobOCIGenerativeAIAgents(Job):




    _type: str=attrs.field(init=False, default='Job:OCI Generative AI Agents', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OCI Generative AI Agents'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    agent_endpoint_ocid: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Agent Endpoint OCID'})
    ai_agent_endpoint_ocid: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Agent Endpoint OCID'})
    input: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Input'})
    ai_input: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Input'})


@ attrs.define
class JobWebServicesREST(Job):


    @ attrs.define
    class WsRestBody(AAPIObject):




        request_definition: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'RequestDefinition'})
        body_request: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'BodyRequest'})
        file_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'FileName'})

    @ attrs.define
    class AIWsRestBody(AAPIObject):




        request_definition: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'RequestDefinition'})
        body_request: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'BodyRequest'})
        file_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'FileName'})



    _type: str=attrs.field(init=False, default='Job:Web Services REST', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Web Services REST'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    endpoint_url: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Endpoint URL'})
    ai_endpoint_url: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Endpoint URL'})
    method: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Method'})
    ai_method: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Method'})
    url_request_path: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'URL Request Path'})
    ai_url_request_path: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-URL Request Path'})
    ws_rest_body: WsRestBody=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'WsRestBody'})
    ai_ws_rest_body: AIWsRestBody=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-WsRestBody'})
    url_parameters: typing.List[str]=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'URL Parameters'})
    ai_url_parameters: typing.List[str]=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-URL Parameters'})
    http_headers: typing.List[str]=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'HTTP Headers'})
    ai_http_headers: typing.List[str]=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-HTTP Headers'})
    output_handling: typing.List[str]=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'OutputHandling'})
    ai_output_handling: typing.List[str]=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-OutputHandling'})
    connection_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Connection Timeout'})
    ai_connection_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Connection Timeout'})
    append_request: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Append Request'})
    ai_append_request: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Append Request'})
    append_response: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Append Response'})
    ai_append_response: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Append Response'})


@ attrs.define
class JobOCIDataFlow(Job):




    _type: str=attrs.field(init=False, default='Job:OCI Data Flow', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OCI Data Flow'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    run_name: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Run Name'})
    ai_run_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Run Name'})
    compartment_ocid: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Compartment OCID'})
    ai_compartment_ocid: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Compartment OCID'})
    application_ocid: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Application OCID'})
    ai_application_ocid: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Application OCID'})
    additional_run_details: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Additional Run Details'})
    ai_additional_run_details: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Additional Run Details'})
    run_details_configuration: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Run Details Configuration'})
    ai_run_details_configuration: str=attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'AI-Run Details Configuration'})
    get_run_information: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Get Run Information'})
    ai_get_run_information: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Get Run Information'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobTalendOAuth(Job):




    _type: str=attrs.field(init=False, default='Job:Talend OAuth', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Talend OAuth'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    task_executable: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Task Executable'})
    ai_task_executable: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Task Executable'})
    environment_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Environment ID'})
    ai_environment_id: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Environment ID'})
    task_name: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Task Name'})
    ai_task_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Task Name'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    log_level: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Log Level'})
    ai_log_level: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Log Level'})
    task_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Task Timeout'})
    ai_task_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Task Timeout'})
    append_task_logs_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Append Task Logs to Output'})
    ai_append_task_logs_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'AI-Append Task Logs to Output'})
    plan_executable: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Plan Executable'})
    ai_plan_executable: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Plan Executable'})
    append_failed_plan_logs_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                                       '_aapi_repr_': 'Append Failed Plan Logs to Output'})
    ai_append_failed_plan_logs_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                                           '_aapi_repr_': 'AI-Append Failed Plan Logs to Output'})
    rerun_only_failed_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Rerun Only Failed Tasks'})
    ai_rerun_only_failed_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Rerun Only Failed Tasks'})
    execution_plan_id: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Execution Plan ID'})
    ai_execution_plan_id: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Execution Plan ID'})
    step_id: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Step ID'})
    ai_step_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Step ID'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobAzureHDInsight(Job):




    _type: str=attrs.field(init=False, default='Job:Azure HDInsight', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure HDInsight'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    bring_job_logs_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Bring job logs to output'})
    ai_bring_job_logs_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Bring job logs to output'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobAwsQuickSight(Job):




    _type: str=attrs.field(init=False, default='Job:AWS QuickSight', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS QuickSight'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    aws_dataset_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AWS Dataset ID'})
    ai_aws_dataset_id: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-AWS Dataset ID'})
    refresh_type: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Refresh Type'})
    ai_refresh_type: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Refresh Type'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})


@ attrs.define
class JobAtlassianJira(Job):




    _type: str=attrs.field(init=False, default='Job:Atlassian Jira', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Atlassian Jira'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    issue_key: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Issue Key'})
    ai_issue_key: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Issue Key'})
    user_name: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'UserName'})
    ai_user_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-UserName'})
    issue_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Issue Parameters'})
    ai_issue_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Issue Parameters'})
    transition_id: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Transition ID'})
    ai_transition_id: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Transition ID'})
    comment: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Comment'})
    ai_comment: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Comment'})


@ attrs.define
class JobAzureAppServicesWebJobs(Job):




    _type: str=attrs.field(init=False, default='Job:Azure App Services WebJobs', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure App Services WebJobs'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    resource_group_name: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Resource Group Name'})
    ai_resource_group_name: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Resource Group Name'})
    web_app_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Web App Name'})
    ai_web_app_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Web App Name'})
    web_job_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Web Job Name'})
    ai_web_job_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Web Job Name'})
    slot: str=attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'Slot'})
    ai_slot: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'AI-Slot'})
    show_output: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Show Output'})
    ai_show_output: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Show Output'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_iempty: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'AI-empty'})


@ attrs.define
class JobCircleCI(Job):




    _type: str=attrs.field(init=False, default='Job:CircleCI', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:CircleCI'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    project_slug: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project Slug'})
    ai_project_slug: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Project Slug'})
    workflow_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Workflow ID'})
    ai_workflow_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Workflow ID'})
    pipeline_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Pipeline ID'})
    ai_pipeline_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Pipeline ID'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobOracleFusionCloudESS(Job):




    _type: str=attrs.field(init=False, default='Job:Oracle Fusion Cloud ESS', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Oracle Fusion Cloud ESS'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    job_definition_id: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Job Definition ID'})
    ai_job_definition_id: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Job Definition ID'})
    application_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Application Name'})
    ai_application_name: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Application Name'})
    request_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Request Parameters'})
    ai_request_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Request Parameters'})
    optional_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Optional Parameters'})
    ai_optional_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Optional Parameters'})
    product: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Product'})
    ai_product: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Product'})
    description: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Description'})
    ai_description: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Description'})
    callback_subscription: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Callback Subscription'})
    ai_callback_subscription: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Callback Subscription'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobAwsSageMaker(Job):




    _type: str=attrs.field(init=False, default='Job:AWS SageMaker', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS SageMaker'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    pipeline_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Pipeline Name'})
    ai_pipeline_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Pipeline Name'})
    idempotency_token: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Idempotency Token'})
    ai_idempotency_token: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Idempotency Token'})
    add_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Add Parameters'})
    ai_add_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Add Parameters'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    retry_pipeline_execution: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Retry Pipeline Execution'})
    ai_retry_pipeline_execution: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Retry Pipeline Execution'})
    pipeline_execution_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Pipeline Execution ARN'})
    ai_pipeline_execution_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Pipeline Execution ARN'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})


@ attrs.define
class JobAstronomer(Job):




    _type: str=attrs.field(init=False, default='Job:Astronomer', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Astronomer'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    d_a_g_name: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'DAG Name'})
    ai_d_a_g_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-DAG Name'})
    d_a_g_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'DAG Run ID'})
    ai_d_a_g_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-DAG Run ID'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    only_failed_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Only Failed Tasks'})
    ai_only_failed_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Only Failed Tasks'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobGCPAgentPlatform(Job):




    _type: str=attrs.field(init=False, default='Job:GCP Agent Platform', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Agent Platform'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    project_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project Name'})
    ai_project_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Project Name'})
    instance_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Instance Name'})
    ai_instance_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Instance Name'})
    pipeline_run_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Pipeline Run Name'})
    ai_pipeline_run_name: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Pipeline Run Name'})
    zone: str=attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'Zone'})
    ai_zone: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'AI-Zone'})
    service_account: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Service Account'})
    ai_service_account: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Service Account'})
    pipeline_specification: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Pipeline Specification'})
    ai_pipeline_specification: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Pipeline Specification'})
    gcs_output_directory: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'GCS Output Directory'})
    ai_gcs_output_directory: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-GCS Output Directory'})
    add_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Add Parameters'})
    ai_add_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Add Parameters'})
    pipeline_runtime_paramaters: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Pipeline Runtime Paramaters'})
    ai_pipeline_runtime_paramaters: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'AI-Pipeline Runtime Paramaters'})
    empty: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'EMPTY'})
    ai_e_m_p_t_y: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-EMPTY'})
    agent_name: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Agent Name'})
    ai_agent_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Agent Name'})
    base_agent: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Base Agent'})
    ai_base_agent: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Base Agent'})
    description: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Description'})
    ai_description: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Description'})
    agent_instructions: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Agent Instructions'})
    ai_agent_instructions: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Agent Instructions'})
    tools: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Tools'})
    ai_tools: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Tools'})
    base_environment_: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Base Environment '})
    ai_base_environment_: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Base Environment '})
    reasoning_engine_id: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Reasoning Engine ID'})
    ai_reasoning_engine_id: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Reasoning Engine ID'})
    input: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Input'})
    ai_input: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Input'})
    streamed_queries_: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Streamed Queries '})
    ai_streamed_queries_: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Streamed Queries '})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})


@ attrs.define
class JobKubernetes(Job):


    @ attrs.define
    class WsRestBody(AAPIObject):




        request_definition: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'RequestDefinition'})
        body_request: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'BodyRequest'})
        file_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'FileName'})

    @ attrs.define
    class AIWsRestBody(AAPIObject):




        request_definition: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'RequestDefinition'})
        body_request: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'BodyRequest'})
        file_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'FileName'})



    _type: str=attrs.field(init=False, default='Job:Kubernetes', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Kubernetes'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    job_spec_type: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Job Spec Type'})
    ai_job_spec_type: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Job Spec Type'})
    job_spec_yaml: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Job Spec Yaml'})
    ai_job_spec_yaml: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Job Spec Yaml'})
    job_spec_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Job Spec Parameters'})
    ai_job_spec_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Job Spec Parameters'})
    spec_request_path: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Spec Request Path'})
    ai_spec_request_path: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Spec Request Path'})
    spec_request_method: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Spec Request Method'})
    ai_spec_request_method: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Spec Request Method'})
    spec_request_parameters: typing.List[str]=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Spec Request Parameters'})
    ai_spec_request_parameters: typing.List[str]=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Spec Request Parameters'})
    spec_request_headers: typing.List[str]=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Spec Request Headers'})
    ai_spec_request_headers: typing.List[str]=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Spec Request Headers'})
    ws_rest_body: WsRestBody=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'WsRestBody'})
    ai_ws_rest_body: AIWsRestBody=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-WsRestBody'})
    get_pod_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Get Pod Logs'})
    ai_get_pod_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Get Pod Logs'})
    os_exit_code: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'OS Exit Code'})
    ai_os_exit_code: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-OS Exit Code'})
    job_cleanup: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Job Cleanup'})
    ai_job_cleanup: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Job Cleanup'})
    job_status_polling_interval: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Job Status Polling Interval'})
    ai_job_status_polling_interval: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'AI-Job Status Polling Interval'})


@ attrs.define
class JobAwsSNS(Job):




    _type: str=attrs.field(init=False, default='Job:AWS SNS', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS SNS'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    message_type: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Message Type'})
    ai_message_type: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Message Type'})
    topic_type: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Topic Type'})
    ai_topic_type: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Topic Type'})
    individual_type: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Individual Type'})
    ai_individual_type: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Individual Type'})
    target_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Target ARN'})
    ai_target_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Target ARN'})
    phone_number: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Phone Number'})
    ai_phone_number: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Phone Number'})
    json_message_structure: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Json Message Structure'})
    ai_json_message_structure: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Json Message Structure'})
    subject: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Subject'})
    ai_subject: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Subject'})
    message: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Message'})
    ai_message: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Message'})
    message_deduplication_id: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Message Deduplication ID'})
    ai_message_deduplication_id: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Message Deduplication ID'})
    message_group_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Message Group ID'})
    ai_message_group_id: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Message Group ID'})
    attributes: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Attributes'})
    ai_attributes: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Attributes'})
    attribute1_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.1 Name'})
    ai_attribute1_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Attribute.1 Name'})
    attribute1_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.1 Value'})
    ai_attribute1_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Attribute.1 Value'})
    attribute2_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.2 Name'})
    ai_attribute2_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Attribute.2 Name'})
    attribute2_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.2 Value'})
    ai_attribute2_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Attribute.2 Value'})
    attribute3_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.3 Name'})
    ai_attribute3_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Attribute.3 Name'})
    attribute3_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.3 Value'})
    ai_attribute3_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Attribute.3 Value'})
    sms_attributes: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'SMS Attributes'})
    ai_sms_attributes: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-SMS Attributes'})
    sender_identifier: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Sender Identifier'})
    ai_sender_identifier: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Sender Identifier'})
    sender_id: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Sender ID'})
    ai_sender_id: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Sender ID'})
    origination_number: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Origination Number'})
    ai_origination_number: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Origination Number'})
    max_price: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Max Price'})
    ai_max_price: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Max Price'})
    sms_type: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'SMS Type'})
    ai_sms_type: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-SMS Type'})
    push_notifications_attributes: str=attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Push Notifications Attributes'})
    ai_push_notifications_attributes: str=attrs.field(kw_only=True, default=None, metadata={
                                                       '_aapi_repr_': 'AI-Push Notifications Attributes'})
    push_attribute1_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.1 Name'})
    ai_push_attribute1_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-PushAttribute.1 Name'})
    push_attribute1_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.1 Value'})
    ai_push_attribute1_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-PushAttribute.1 Value'})
    push_attribute2_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.2 Name'})
    ai_push_attribute2_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-PushAttribute.2 Name'})
    push_attribute2_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.2 Value'})
    ai_push_attribute2_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-PushAttribute.2 Value'})
    push_attribute3_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.3 Name'})
    ai_push_attribute3_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-PushAttribute.3 Name'})
    push_attribute3_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.3 Value'})
    ai_push_attribute3_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-PushAttribute.3 Value'})
    push_attribute4_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.4 Name'})
    ai_push_attribute4_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-PushAttribute.4 Name'})
    push_attribute4_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.4 Value'})
    ai_push_attribute4_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-PushAttribute.4 Value'})
    push_attribute5_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.5 Name'})
    ai_push_attribute5_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-PushAttribute.5 Name'})
    push_attribute5_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'PushAttribute.5 Value'})
    ai_push_attribute5_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-PushAttribute.5 Value'})


@ attrs.define
class JobAwsLambda(Job):




    _type: str=attrs.field(init=False, default='Job:AWS Lambda', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Lambda'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    function_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Function Name'})
    ai_function_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Function Name'})
    function_version: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Function Version'})
    ai_function_version: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Function Version'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    append_log_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Append Log to Output'})
    ai_append_log_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Append Log to Output'})


@ attrs.define
class JobAlteryxTrifacta(Job):




    _type: str=attrs.field(init=False, default='Job:Alteryx Trifacta', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Alteryx Trifacta'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    flow_name: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Flow Name'})
    ai_flow_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Flow Name'})
    rerun_with_new_idempotency_token: str=attrs.field(kw_only=True, default=None, metadata={
                                                      '_aapi_repr_': 'Rerun With New Idempotency Token'})
    ai_rerun_with_new_idempotency_token: str=attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'AI-Rerun With New Idempotency Token'})
    idempotent_token: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Idempotent Token'})
    ai_idempotent_token: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Idempotent Token'})
    retrack_job_status: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Retrack Job Status'})
    ai_retrack_job_status: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Retrack Job Status'})
    run_id: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Run-ID'})
    ai_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Run-ID'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})


@ attrs.define
class JobSnowflakeIdP(Job):




    _type: str=attrs.field(init=False, default='Job:Snowflake IdP', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Snowflake IdP'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    database: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Database'})
    ai_database: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Database'})
    schema: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Schema'})
    ai_schema: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Schema'})
    actions: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Actions'})
    ai_actions: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Actions'})
    snowflake_sql_statement: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Snowflake SQL Statement'})
    ai_snowflake_sql_statement: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Snowflake SQL Statement'})
    query_to_location: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Query To Location'})
    ai_query_to_location: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Query To Location'})
    query_input: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Query Input'})
    ai_query_input: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Query Input'})
    storage_integration: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Storage Integration'})
    ai_storage_integration: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Storage Integration'})
    overwrite: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Overwrite'})
    ai_overwrite: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Overwrite'})
    file_format: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'File Format'})
    ai_file_format: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-File Format'})
    create_table_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Create Table Name'})
    ai_create_table_name: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Create Table Name'})
    query: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Query'})
    ai_query: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Query'})
    add_condition: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Add Condition'})
    ai_add_condition: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Add Condition'})
    stored_procedure_name: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Stored Procedure Name'})
    ai_stored_procedure_name: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Stored Procedure Name'})
    procedure_argument: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Procedure Argument'})
    ai_procedure_argument: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Procedure Argument'})
    activity_options: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Activity Options'})
    ai_activity_options: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Activity Options'})
    table_name: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Table Name'})
    ai_table_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Table Name'})
    from_location: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'From Location'})
    ai_from_location: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-From Location'})
    stage_name: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Stage Name'})
    ai_stage_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Stage Name'})
    from_storage_integration: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'From Storage Integration'})
    ai_from_storage_integration: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-From Storage Integration'})
    stage_url: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Stage URL'})
    ai_stage_url: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Stage URL'})
    copy_destination: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Copy Destination'})
    ai_copy_destination: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Copy Destination'})
    from_table: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'From Table'})
    ai_from_table: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-From Table'})
    pipe_name: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Pipe Name'})
    ai_pipe_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Pipe Name'})
    start_or_pause_pipe: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Start Or Pause Pipe'})
    ai_start_or_pause_pipe: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Start Or Pause Pipe'})
    stage_location: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Stage Location'})
    ai_stage_location: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Stage Location'})
    snowpipe_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Snowpipe Name'})
    ai_snowpipe_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Snowpipe Name'})
    days_back: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Days Back'})
    ai_days_back: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Days Back'})
    status_file_cloud_location_path: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'Status File Cloud Location Path'})
    ai_status_file_cloud_location_path: str=attrs.field(kw_only=True, default=None, metadata={
                                                         '_aapi_repr_': 'AI-Status File Cloud Location Path'})
    stoarge_integration_for_location: str=attrs.field(kw_only=True, default=None, metadata={
                                                      '_aapi_repr_': 'Stoarge Integration For Location'})
    ai_stoarge_integration_for_location: str=attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'AI-Stoarge Integration For Location'})
    load_sql_file: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Load SQL File'})
    ai_load_sql_file: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Load SQL File'})
    statement_timeout__sec: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Statement Timeout (Sec)'})
    ai_statement_timeout__sec: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Statement Timeout (Sec)'})
    show_more_options: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Show More Options'})
    ai_show_more_options: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Show More Options'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    role: str=attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'Role'})
    ai_role: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'AI-Role'})
    bindings: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Bindings'})
    ai_bindings: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Bindings'})
    warehouse: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Warehouse'})
    ai_warehouse: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Warehouse'})
    show_output: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Show Output'})
    ai_show_output: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Show Output'})
    polling_interval__sec: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Polling Interval (Sec)'})
    ai_polling_interval__sec: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Polling Interval (Sec)'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})


@ attrs.define
class JobAwsSQS(Job):




    _type: str=attrs.field(init=False, default='Job:AWS SQS', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS SQS'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action_type: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Action Type'})
    ai_action_type: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Action Type'})
    queue_type: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Queue Type'})
    ai_queue_type: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Queue Type'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    queue_url: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Queue URL'})
    ai_queue_url: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Queue URL'})
    message_body: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Message Body'})
    ai_message_body: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Message Body'})
    delay_seconds: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Delay Seconds'})
    ai_delay_seconds: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Delay Seconds'})
    message_deduplication_id: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Message Deduplication ID'})
    ai_message_deduplication_id: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Message Deduplication ID'})
    message_group_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Message Group ID'})
    ai_message_group_id: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Message Group ID'})
    message_attributes: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Message Attributes'})
    ai_message_attributes: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Message Attributes'})
    attribute1_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.1 Name'})
    ai_attribute1_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Attribute.1 Name'})
    attribute1_data_type: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.1 DataType'})
    ai_attribute1_data_type: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Attribute.1 DataType'})
    attribute1_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.1 Value'})
    ai_attribute1_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Attribute.1 Value'})
    attribute2_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.2 Name'})
    ai_attribute2_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Attribute.2 Name'})
    attribute2_data_type: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.2 DataType'})
    ai_attribute2_data_type: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Attribute.2 DataType'})
    attribute2_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.2 Value'})
    ai_attribute2_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Attribute.2 Value'})
    attribute3_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.3 Name'})
    ai_attribute3_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Attribute.3 Name'})
    attribute3_data_type: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.3 DataType'})
    ai_attribute3_data_type: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Attribute.3 DataType'})
    attribute3_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'Attribute.3 Value'})
    ai_attribute3_value: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Attribute.3 Value'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})


@ attrs.define
class JobIBMDataStageWindows(Job):




    _type: str=attrs.field(init=False, default='Job:IBM DataStage Windows', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:IBM DataStage Windows'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    project: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Project'})
    ai_project: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Project'})
    datastage_job: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Datastage Job'})
    ai_datastage_job: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Datastage Job'})
    job_invocation_id__optional: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Job Invocation ID (Optional)'})
    ai_job_invocation_id__optional: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'AI-Job Invocation ID (Optional)'})
    parameters_type: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Parameters Type'})
    ai_parameters_type: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Parameters Type'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    parameter_file: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Parameter File'})
    ai_parameter_file: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Parameter File'})
    stop_stages_after_number_of_rows: str=attrs.field(kw_only=True, default=None, metadata={
                                                      '_aapi_repr_': 'Stop Stages After Number Of Rows'})
    ai_stop_stages_after_number_of_rows: str=attrs.field(kw_only=True, default=None, metadata={
                                                          '_aapi_repr_': 'AI-Stop Stages After Number Of Rows'})
    abort_job_after_number_of_warnings: str=attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'Abort Job After Number Of Warnings'})
    ai_abort_job_after_number_of_warnings: str=attrs.field(kw_only=True, default=None, metadata={
                                                            '_aapi_repr_': 'AI-Abort Job After Number Of Warnings'})
    append_log_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Append Log To Output'})
    ai_append_log_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Append Log To Output'})
    run_in_restart_mode: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Run In Restart Mode'})
    ai_run_in_restart_mode: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Run In Restart Mode'})
    reset_job_before_run: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Reset Job Before Run'})
    ai_reset_job_before_run: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Reset Job Before Run'})
    empty1: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Empty1'})
    ai_empty1: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Empty1'})


@ attrs.define
class JobGCPDataprep(Job):




    _type: str=attrs.field(init=False, default='Job:GCP Dataprep', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Dataprep'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    flow_name: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Flow Name'})
    ai_flow_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Flow Name'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    execute_job_with_idempotency_token: str=attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'Execute Job with Idempotency Token'})
    ai_execute_job_with_idempotency_token: str=attrs.field(kw_only=True, default=None, metadata={
                                                            '_aapi_repr_': 'AI-Execute Job with Idempotency Token'})
    idempotency_token: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Idempotency Token'})
    ai_idempotency_token: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Idempotency Token'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobAwsGlueDataBrew(Job):




    _type: str=attrs.field(init=False, default='Job:AWS Glue DataBrew', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Glue DataBrew'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    job_name: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Job Name'})
    ai_job_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Job Name'})
    output_job_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Output Job Logs'})
    ai_output_job_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Output Job Logs'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})


@ attrs.define
class JobDatabricks(Job):




    _type: str=attrs.field(init=False, default='Job:Databricks', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Databricks'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    authentication_type: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Authentication Type'})
    ai_authentication_type: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Authentication Type'})
    databricks_job_name: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Databricks Job Name'})
    ai_databricks_job_name: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Databricks Job Name'})
    databricks_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Databricks Job ID'})
    ai_databricks_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Databricks Job ID'})
    databricks_job_id_o_auth_o_id_c: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'Databricks Job ID OAuth OIDC'})
    ai_databricks_job_id_o_auth_o_id_c: str=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Databricks Job ID OAuth OIDC'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    idempotency_token: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Idempotency Token'})
    ai_idempotency_token: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Idempotency Token'})
    show_tasks_output: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Show Tasks Output'})
    ai_show_tasks_output: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Show Tasks Output'})
    repair_on_rerun: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Repair on Rerun'})
    ai_repair_on_rerun: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Repair on Rerun'})
    reference_job_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Reference Job Run ID'})
    ai_reference_job_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Reference Job Run ID'})
    latest_repair_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Latest Repair ID'})
    ai_latest_repair_id: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Latest Repair ID'})
    rerun_all_failed_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Rerun all Failed Tasks'})
    ai_rerun_all_failed_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Rerun all Failed Tasks'})
    rerun_dependent_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Rerun Dependent Tasks'})
    ai_rerun_dependent_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Rerun Dependent Tasks'})
    rerun_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Rerun Tasks'})
    ai_rerun_tasks: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Rerun Tasks'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobAwsAthena(Job):




    _type: str=attrs.field(init=False, default='Job:AWS Athena', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Athena'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    athena_client_request_token: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Athena Client Request Token'})
    ai_athena_client_request_token: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'AI-Athena Client Request Token'})
    db_catalog_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'DB Catalog Name'})
    ai_db_catalog_name: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-DB Catalog Name'})
    database_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Database Name'})
    ai_database_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Database Name'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    query: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Query'})
    ai_query: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Query'})
    table_name: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Table Name'})
    ai_table_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Table Name'})
    prepared_query_name: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Prepared Query Name'})
    ai_prepared_query_name: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Prepared Query Name'})
    unload_file_type: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Unload File Type'})
    ai_unload_file_type: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Unload File Type'})
    output_location: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Output Location'})
    ai_output_location: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Output Location'})
    workgroup: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Workgroup'})
    ai_workgroup: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Workgroup'})
    add_configurations: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Add Configurations'})
    ai_add_configurations: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Add Configurations'})
    s3_acl_option: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'S3 ACL Option'})
    ai_s3_acl_option: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-S3 ACL Option'})
    encryption_options: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Encryption Options'})
    ai_encryption_options: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Encryption Options'})
    kms_key: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'KMS Key'})
    ai_kms_key: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-KMS Key'})
    bucket_owner: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Bucket Owner'})
    ai_bucket_owner: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Bucket Owner'})
    show_json_output: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Show JSON Output'})
    ai_show_json_output: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Show JSON Output'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Tolerance'})
    ai_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Tolerance'})
    a_itoken_prefix: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-token prefix'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})
    no_perm: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'NoPerm'})
    ai_no_perm: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-NoPerm'})


@ attrs.define
class JobDBT(Job):




    _type: str=attrs.field(init=False, default='Job:DBT', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:DBT'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    dbt_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'DBT Job Id'})
    ai_dbt_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-DBT Job Id'})
    run_comment: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Run Comment'})
    ai_run_comment: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Run Comment'})
    override_job_commands: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Override Job Commands'})
    ai_override_job_commands: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Override Job Commands'})
    define_commands: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Define Commands'})
    ai_define_commands: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Define Commands'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})


@ attrs.define
class JobAzureServiceBus(Job):




    _type: str=attrs.field(init=False, default='Job:Azure Service Bus', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Service Bus'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    service_bus_namespace: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Service Bus Namespace'})
    ai_service_bus_namespace: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Service Bus Namespace'})
    queue_topic_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'QueueTopic Name'})
    ai_queue_topic_name: str=attrs.field(kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-QueueTopic Name'})
    message_format: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Message Format'})
    ai_message_format: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Message Format'})
    message_body: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Message Body'})
    ai_message_body: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Message Body'})
    use_inline_payload: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Use Inline Payload'})
    ai_use_inline_payload: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Use Inline Payload'})
    message_payload: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Message Payload'})
    ai_message_payload: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Message Payload'})


@ attrs.define
class JobFivetran(Job):




    _type: str=attrs.field(init=False, default='Job:Fivetran', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Fivetran'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    job_type: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Job Type'})
    ai_job_type: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Job Type'})
    connection_id: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Connection ID'})
    ai_connection_id: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Connection ID'})
    connection_name: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Connection Name'})
    ai_connection_name: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Connection Name'})
    force_incremental_sync: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Force Incremental Sync'})
    ai_force_incremental_sync: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Force Incremental Sync'})
    transformation_id: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Transformation ID'})
    ai_transformation_id: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Transformation ID'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobWorkato(Job):




    _type: str=attrs.field(init=False, default='Job:Workato', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Workato'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    reciepe_actions: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Reciepe Actions'})
    ai_reciepe_actions: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Reciepe Actions'})
    reciepe_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Reciepe ID'})
    ai_reciepe_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Reciepe ID'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobAwsBatch(Job):




    _type: str=attrs.field(init=False, default='Job:AWS Batch', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Batch'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    use_advanced_json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Use Advanced JSON Format'})
    ai_use_advanced_json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Use Advanced JSON Format'})
    job_name: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Job Name'})
    ai_job_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Job Name'})
    job_definition_and_revision: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Job Definition and Revision'})
    ai_job_definition_and_revision: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'AI-Job Definition and Revision'})
    job_queue: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Job Queue'})
    ai_job_queue: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Job Queue'})
    container_overrides_command: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Container Overrides Command'})
    ai_container_overrides_command: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'AI-Container Overrides Command'})
    job_attempts: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Job Attempts'})
    ai_job_attempts: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Job Attempts'})
    execution_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Execution Timeout'})
    ai_execution_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Execution Timeout'})
    json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'JSON Format'})
    ai_json_format: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-JSON Format'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})


@ attrs.define
class JobNetBackup(Job):




    _type: str=attrs.field(init=False, default='Job:NetBackup', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:NetBackup'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    json_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'JSON Parameters'})
    ai_json_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-JSON Parameters'})
    policy_name: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Policy Name'})
    ai_policy_name: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Policy Name'})
    schedule_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Schedule Name'})
    ai_schedule_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Schedule Name'})
    client_name: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Client Name'})
    ai_client_name: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Client Name'})
    keyword: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Keyword'})
    ai_keyword: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Keyword'})
    instance_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Instance Name'})
    ai_instance_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Instance Name'})
    database_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Database Name'})
    ai_database_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Database Name'})
    db_unique_name: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'DB Unique Name'})
    ai_db_unique_name: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-DB Unique Name'})
    db_id: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'DB ID'})
    ai_db_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-DB ID'})
    trial_backup: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Trial Backup'})
    ai_trial_backup: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Trial Backup'})
    output__management: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Output  Management'})
    ai_output__management: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Output  Management'})
    restart_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Restart Job ID'})
    ai_restart_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Restart Job ID'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobGCPWorkflows(Job):




    _type: str=attrs.field(init=False, default='Job:GCP Workflows', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Workflows'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Project ID'})
    ai_project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Project ID'})
    location: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Location'})
    ai_location: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Location'})
    workflow_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Workflow Name'})
    ai_workflow_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Workflow Name'})
    parameters_json_input: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Parameters JSON Input'})
    ai_parameters_json_input: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Parameters JSON Input'})
    execution_label: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Execution Label'})
    ai_execution_label: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Execution Label'})
    show_workflow_results: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Show Workflow Results'})
    ai_show_workflow_results: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Show Workflow Results'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})
    a_iq2: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q2'})
    a_iq2body: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-q2body'})


@ attrs.define
class JobGCPBigQuery(Job):




    _type: str=attrs.field(init=False, default='Job:GCP BigQuery', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP BigQuery'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Project Id'})
    ai_project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Project Id'})
    dataset_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Dataset Name'})
    ai_dataset_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Dataset Name'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    run_select_query_and_copy_to_table: str=attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'Run Select Query and Copy to Table'})
    ai_run_select_query_and_copy_to_table: str=attrs.field(kw_only=True, default=None, metadata={
                                                            '_aapi_repr_': 'AI-Run Select Query and Copy to Table'})
    table_name: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Table Name'})
    ai_table_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Table Name'})
    query_type: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Query Type'})
    ai_query_type: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Query Type'})
    sql_statement: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'SQL Statement'})
    ai_sql_statement: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-SQL Statement'})
    load_query_from_file: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Load Query From File'})
    ai_load_query_from_file: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Load Query From File'})
    query_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Query Parameters'})
    ai_query_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Query Parameters'})
    routine: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Routine'})
    ai_routine: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Routine'})
    extract_as: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Extract As'})
    ai_extract_as: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Extract As'})
    copy_operation_type: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Copy Operation Type'})
    ai_copy_operation_type: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Copy Operation Type'})
    source_tables_properties: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Source Tables Properties'})
    ai_source_tables_properties: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Source Tables Properties'})
    destination_source_bucket_uris: str=attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'Destination/Source Bucket URIs'})
    ai_destination_source_bucket_uris: str=attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'AI-Destination/Source Bucket URIs'})
    destination_table_properties: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Destination Table Properties'})
    ai_destination_table_properties: str=attrs.field(kw_only=True, default=None, metadata={
                                                      '_aapi_repr_': 'AI-Destination Table Properties'})
    show_load_options: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Show Load Options'})
    ai_show_load_options: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Show Load Options'})
    load_options: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Load Options'})
    ai_load_options: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Load Options'})
    print_header: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Print Header'})
    ai_print_header: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Print Header'})
    field_delimiter: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Field Delimiter'})
    ai_field_delimiter: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Field Delimiter'})
    job_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Job Timeout'})
    ai_job_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Job Timeout'})
    connection_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Connection Timeout'})
    ai_connection_timeout: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Connection Timeout'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})
    empty: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Empty'})
    ai_empty: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Empty'})


@ attrs.define
class JobPagerDuty(Job):




    _type: str=attrs.field(init=False, default='Job:PagerDuty', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:PagerDuty'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    incident_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Incident ID'})
    ai_incident_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Incident ID'})
    email_address: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Email Address'})
    ai_email_address: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Email Address'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    duration: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Duration'})
    ai_duration: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Duration'})
    title: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Title'})
    ai_title: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Title'})
    service_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Service ID'})
    ai_service_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Service ID'})
    urgency: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Urgency'})
    ai_urgency: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Urgency'})
    incident_key: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Incident Key'})
    ai_incident_key: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Incident Key'})
    incident_body: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Incident Body'})
    ai_incident_body: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Incident Body'})


@ attrs.define
class JobTalendDataManagement(Job):




    _type: str=attrs.field(init=False, default='Job:Talend Data Management', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Talend Data Management'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    task_plan_execution: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Task/Plan Execution'})
    ai_task_plan_execution: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Task/Plan Execution'})
    task_name: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Task Name'})
    ai_task_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Task Name'})
    environment_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Environment ID'})
    ai_environment_id: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Environment ID'})
    workspace_id: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Workspace ID'})
    ai_workspace_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Workspace ID'})
    task_id: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Task ID'})
    ai_task_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Task ID'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    log_level: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Log Level'})
    ai_log_level: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Log Level'})
    bring_logs_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Bring logs to output'})
    ai_bring_logs_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Bring logs to output'})
    task_polling_intervals: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Task Polling Intervals'})
    ai_task_polling_intervals: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Task Polling Intervals'})
    plan_name: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Plan Name'})
    ai_plan_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Plan Name'})
    plan_body_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Plan Body Parameters'})
    ai_plan_body_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Plan Body Parameters'})
    save_failed_plan_log: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Save Failed Plan Log'})
    ai_save_failed_plan_log: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Save Failed Plan Log'})
    plan_polling_intervals: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Plan Polling Intervals'})
    ai_plan_polling_intervals: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Plan Polling Intervals'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})


@ attrs.define
class JobMicroFocusLinux(Job):




    _type: str=attrs.field(init=False, default='Job:Micro Focus Linux', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Micro Focus Linux'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    jcl_filename: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'JCL Filename'})
    ai_jcl_filename: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-JCL Filename'})
    pds: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'PDS'})
    ai_pds: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-PDS'})
    enable_jcl_variables: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Enable JCL Variables'})
    ai_enable_jcl_variables: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Enable JCL Variables'})
    additional_variables: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Additional Variables'})
    ai_additional_variables: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Additional Variables'})
    restart_on_rerun: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Restart on Rerun'})
    ai_restart_on_rerun: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Restart on Rerun'})
    from_step_proc: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'From Step/Proc'})
    ai_from_step_proc: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-From Step/Proc'})
    to_step_proc: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'To Step/Proc'})
    ai_to_step_proc: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-To Step/Proc'})
    recapture_abend_codes: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Recapture ABEND Codes'})
    ai_recapture_abend_codes: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Recapture ABEND Codes'})
    recapture_cond_codes: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Recapture COND Codes'})
    ai_recapture_cond_codes: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Recapture COND Codes'})
    auto_adjust_restart: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Auto Adjust Restart'})
    ai_auto_adjust_restart: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Auto Adjust Restart'})
    step_specific_condition_codes: str=attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Step-Specific Condition Codes'})
    ai_step_specific_condition_codes: str=attrs.field(kw_only=True, default=None, metadata={
                                                       '_aapi_repr_': 'AI-Step-Specific Condition Codes'})
    set_mf_ucc11: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Set MF_UCC11'})
    ai_set_mf_ucc11: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Set MF_UCC11'})
    advanced_restart_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Advanced Restart Parameters'})
    ai_advanced_restart_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'AI-Advanced Restart Parameters'})
    rerun_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Rerun Job ID'})
    ai_rerun_job_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Rerun Job ID'})
    restart_with_modified_jcl: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Restart with Modified JCL'})
    ai_restart_with_modified_jcl: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'AI-Restart with Modified JCL'})
    modified_jcl_path_and_filename: str=attrs.field(kw_only=True, default=None, metadata={
                                                      '_aapi_repr_': 'Modified JCL Path and Filename'})
    ai_modified_jcl_path_and_filename: str=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-Modified JCL Path and Filename'})
    a_iregion: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-region'})
    a_iempty_attribute: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-empty attribute'})


@ attrs.define
class JobCrewAI(Job):




    _type: str=attrs.field(init=False, default='Job:CrewAI', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:CrewAI'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    crew_inputs: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Crew Inputs'})
    ai_crew_inputs: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Crew Inputs'})
    additional_parameters_: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Additional Parameters  '})
    ai_additional_parameters_: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Additional Parameters  '})
    training_file_name: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Training File Name'})
    ai_training_file_name: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Training File Name'})
    generate_artifact: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Generate Artifact'})
    ai_generate_artifact: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Generate Artifact'})
    task_webhook_url: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Task Webhook URL'})
    ai_task_webhook_url: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Task Webhook URL'})
    step_webhook_url: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Step Webhook URL'})
    ai_step_webhook_url: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Step Webhook URL'})
    crew_webhook_url: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Crew Webhook URL'})
    ai_crew_webhook_url: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Crew Webhook URL'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})


@ attrs.define
class JobAzureResourceManager(Job):




    _type: str=attrs.field(init=False, default='Job:Azure Resource Manager', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Resource Manager'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    resource_group_name: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Resource Group Name'})
    ai_resource_group_name: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Resource Group Name'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    deployment_name: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Deployment Name'})
    ai_deployment_name: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Deployment Name'})
    deployment_properties: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Deployment Properties'})
    ai_deployment_properties: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Deployment Properties'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})


@ attrs.define
class JobAwsStepFunctions(Job):




    _type: str=attrs.field(init=False, default='Job:AWS Step Functions', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Step Functions'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    execution_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Execution Name'})
    ai_execution_name: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Execution Name'})
    state_machine_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'State Machine ARN'})
    ai_state_machine_arn: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-State Machine ARN'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    show_execution_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Show Execution Logs'})
    ai_show_execution_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Show Execution Logs'})
    express_state_machine_execution: str=attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'Express State Machine Execution'})
    ai_express_state_machine_execution: str=attrs.field(kw_only=True, default=None, metadata={
                                                         '_aapi_repr_': 'AI-Express State Machine Execution'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})
    a_ib1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b1'})
    a_ib2: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b2'})


@ attrs.define
class JobInformaticaCS(Job):




    _type: str=attrs.field(init=False, default='Job:Informatica CS', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Informatica CS'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    task_type: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Task Type'})
    ai_task_type: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Task Type'})
    use_federation_id: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Use Federation ID'})
    ai_use_federation_id: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Use Federation ID'})
    task_name: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Task Name'})
    ai_task_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Task Name'})
    folder_path: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Folder Path'})
    ai_folder_path: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Folder Path'})
    taskflow_job_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Taskflow Job Name'})
    ai_taskflow_job_name: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Taskflow Job Name'})
    task_flow_url: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'TaskFlow URL'})
    ai_task_flow_url: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-TaskFlow URL'})
    rerun_suspended_taskflow: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Rerun Suspended Taskflow'})
    ai_rerun_suspended_taskflow: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Rerun Suspended Taskflow'})
    rerun_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Rerun Run ID'})
    ai_rerun_run_id: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Rerun Run ID'})
    process_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Process Name'})
    ai_process_name: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Process Name'})
    input_fields: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Input Fields'})
    ai_input_fields: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AI-Input Fields'})
    call_back_url: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Call Back URL'})
    ai_call_back_url: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Call Back URL'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    a_ipre1: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'AI-pre1'})
    a_ipre2: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'AI-pre2'})
    a_iend1: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'AI-end1'})
    a_iexec11: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-exec11'})
    a_iexec12: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-exec12'})
    a_iexec13: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-exec13'})
    a_iexec21: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-exec21'})
    a_iexec22: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-exec22'})
    a_iend2: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'AI-end2'})
    a_iexec31: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-exec31'})
    a_iexec32: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-exec32'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobTerraform(Job):




    _type: str=attrs.field(init=False, default='Job:Terraform', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Terraform'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    a_iworkspacebody1: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-workspacebody1'})
    a_iworkspacebody3: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-workspacebody3'})
    a_iworkspacebody2: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-workspacebody2'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    workspace_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Workspace Name'})
    ai_workspace_name: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Workspace Name'})
    run_name: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Run Name'})
    ai_run_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Run Name'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    workspace_params: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Workspace Params'})
    ai_workspace_params: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Workspace Params'})
    variable: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Variable'})
    ai_variable: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Variable'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobApplicationIntegratorAISimplePlugin(Job):




    _type: str=attrs.field(init=False, default='Job:ApplicationIntegrator:AI Simple Plugin', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:ApplicationIntegrator:AI Simple Plugin'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    ai_user: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'AI-User'})
    ai_connection_type: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Connection Type'})


@ attrs.define
class JobAtlassianBitbucket(Job):




    _type: str=attrs.field(init=False, default='Job:Atlassian Bitbucket', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Atlassian Bitbucket'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    pull_request_action: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Pull Request Action'})
    ai_pull_request_action: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Pull Request Action'})
    pull_request_pipeline: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Pull Request Pipeline'})
    ai_pull_request_pipeline: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'AI-Pull Request Pipeline'})
    workspace: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Workspace'})
    ai_workspace: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Workspace'})
    repo_slug: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Repo Slug'})
    ai_repo_slug: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Repo Slug'})
    type_attribute: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Type Attribute'})
    ai_type_attribute: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Type Attribute'})
    source: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Source'})
    ai_source: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Source'})
    destination: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Destination'})
    ai_destination: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Destination'})
    destination_commit_hash: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Destination Commit Hash'})
    ai_destination_commit_hash: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Destination Commit Hash'})
    pull_request_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Pull Request ID'})
    ai_pull_request_id: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Pull Request ID'})
    ref_type: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Ref Type'})
    ai_ref_type: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Ref Type'})
    ref_name: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Ref Name'})
    ai_ref_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Ref Name'})
    commit: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Commit'})
    ai_commit: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Commit'})
    hash: str=attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'Hash'})
    ai_hash: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'AI-Hash'})
    commit_hash: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Commit Hash'})
    ai_commit_hash: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Commit Hash'})
    selector: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Selector'})
    ai_selector: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Selector'})
    selector_type: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Selector Type'})
    ai_selector_type: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Selector Type'})
    pattern: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Pattern'})
    ai_pattern: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Pattern'})
    variables: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Variables'})
    ai_variables: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Variables'})
    get_pipeline_steps_log: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Get Pipeline Steps Log'})
    ai_get_pipeline_steps_log: str=attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AI-Get Pipeline Steps Log'})
    title: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Title'})
    ai_title: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-Title'})
    repository_full_name: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Repository Full Name'})
    ai_repository_full_name: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AI-Repository Full Name'})
    pull_request_source: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Pull Request Source'})
    ai_pull_request_source: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Pull Request Source'})
    pull_request_destination: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Pull Request Destination'})
    ai_pull_request_destination: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Pull Request Destination'})
    reviewers: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Reviewers'})
    ai_reviewers: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Reviewers'})
    message: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Message'})
    ai_message: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Message'})
    close_source_branch: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Close Source Branch'})
    ai_close_source_branch: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Close Source Branch'})
    merge_strategy: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Merge Strategy'})
    ai_merge_strategy: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Merge Strategy'})
    url_path: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'URL Path'})
    ai_url_path: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-URL Path'})
    manual_json: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Manual JSON'})
    ai_manual_json: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Manual JSON'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})


@ attrs.define
class JobGCPFunctions(Job):




    _type: str=attrs.field(init=False, default='Job:GCP Functions', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Functions'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Project ID'})
    ai_project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Project ID'})
    location: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Location'})
    ai_location: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Location'})
    function_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Function Name'})
    ai_function_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Function Name'})
    function_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Function Parameters'})
    ai_function_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Function Parameters'})
    url_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'URL Parameters'})
    ai_url_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-URL Parameters'})
    body: str=attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'Body'})
    ai_body: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'AI-Body'})
    api_version: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'API Version'})
    ai_api_version: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-API Version'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    get_logs: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Get Logs'})
    ai_get_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Get Logs'})
    a_ibodydata: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-bodydata'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})
    a_iq2: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q2'})
    a_iq2body: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'AI-q2body'})
    a_iatt1: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'AI-att1'})
    a_iendatt1: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-endatt1'})
    a_iatt2: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'AI-att2'})
    a_iendatt2: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-endatt2'})
    a_iatt3: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'AI-att3'})


@ attrs.define
class JobAzureLogicApps(Job):




    _type: str=attrs.field(init=False, default='Job:Azure Logic Apps', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Logic Apps'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    plan: str=attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'Plan'})
    ai_plan: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'AI-Plan'})
    logic_app_name: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Logic App Name'})
    ai_logic_app_name: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'AI-Logic App Name'})
    workflow: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Workflow'})
    ai_workflow: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Workflow'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    get_logs: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Get Logs'})
    ai_get_logs: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Get Logs'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    a_ib1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b1'})
    a_ib2: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b2'})
    resubmit_action: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Resubmit Action'})
    ai_resubmit_action: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Resubmit Action'})
    failed_action_to_resubmit: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Failed Action to Resubmit'})
    ai_failed_action_to_resubmit: str=attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'AI-Failed Action to Resubmit'})
    t_r_a_c_k_i_n_g_r_u_n_id_r_e_r_u_n: str=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'TRACKING RUNID RERUN'})
    ai_t_r_a_c_k_i_n_g_r_u_n_id_r_e_r_u_n: str=attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AI-TRACKING RUNID RERUN'})


@ attrs.define
class JobQlikCloud(Job):




    _type: str=attrs.field(init=False, default='Job:Qlik Cloud', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Qlik Cloud'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    reload_type: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Reload Type'})
    ai_reload_type: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Reload Type'})
    app_id: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'App ID'})
    ai_app_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-App ID'})
    print_log_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Print Log to Output'})
    ai_print_log_to_output: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'AI-Print Log to Output'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Tolerance'})
    ai_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AI-Tolerance'})


@ attrs.define
class JobOCIVM(Job):




    _type: str=attrs.field(init=False, default='Job:OCI VM', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OCI VM'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    instance_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Instance ID'})
    ai_instance_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Instance ID'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_ib1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b1'})
    a_ib2: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b2'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})


@ attrs.define
class JobAwsDataPipeline(Job):




    _type: str=attrs.field(init=False, default='Job:AWS Data Pipeline', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Data Pipeline'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    action: str=attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Action'})
    ai_action: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'AI-Action'})
    pipeline_id: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Pipeline ID'})
    ai_pipeline_id: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AI-Pipeline ID'})
    pipeline_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Pipeline Name'})
    ai_pipeline_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Pipeline Name'})
    pipeline_unique_id: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Pipeline Unique ID'})
    ai_pipeline_unique_id: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-Pipeline Unique ID'})
    parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Parameters'})
    ai_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Parameters'})
    trigger_created_pipeline: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Trigger Created Pipeline'})
    ai_trigger_created_pipeline: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Trigger Created Pipeline'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})


@ attrs.define
class JobOCIDataIntegration(Job):




    _type: str=attrs.field(init=False, default='Job:OCI Data Integration', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OCI Data Integration'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    actions: str=attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Actions'})
    ai_actions: str=attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'AI-Actions'})
    workspace_ocid: str=attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Workspace OCID'})
    ai_workspace_ocid: str=attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'AI-Workspace OCID'})
    application_key: str=attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Application Key'})
    ai_application_key: str=attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AI-Application Key'})
    task_key: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Task Key'})
    ai_task_key: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Task Key'})
    task_run_name: str=attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Task Run Name'})
    ai_task_run_name: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AI-Task Run Name'})
    task_run_input_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Task Run Input Parameters'})
    ai_task_run_input_parameters: str=attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'AI-Task Run Input Parameters'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
    failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Failure Tolerance'})
    ai_failure_tolerance: str=attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AI-Failure Tolerance'})
    a_ib1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b1'})
    a_ib2: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-b2'})
    a_iq1: str=attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'AI-q1'})


@ attrs.define
class JobGCPCloudRun(Job):




    _type: str=attrs.field(init=False, default='Job:GCP Cloud Run', metadata={
                           '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Cloud Run'})
    object_name: str=attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ConnectionProfile'})
    ai_connection_profile: str=attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AI-ConnectionProfile'})
    project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Project ID'})
    ai_project_id: str=attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'AI-Project ID'})
    location: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Location'})
    ai_location: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Location'})
    job_name: str=attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Job Name'})
    ai_job_name: str=attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'AI-Job Name'})
    overrides_specification: str=attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Overrides Specification'})
    ai_overrides_specification: str=attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'AI-Overrides Specification'})
    status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Status Polling Frequency'})
    ai_status_polling_frequency: str=attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'AI-Status Polling Frequency'})
