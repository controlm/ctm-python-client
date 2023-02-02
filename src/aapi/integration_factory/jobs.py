
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class JobAutomationAnywhere(Job):

    _type: str = attrs.field(init=False, default='Job:Automation Anywhere', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Automation Anywhere'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
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
class JobAwsGlueDataBrew(Job):

    _type: str = attrs.field(init=False, default='Job:AWS Glue DataBrew', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Glue DataBrew'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
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
class JobAzureDataFactory(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Data Factory', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Data Factory'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
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


@attrs.define
class JobAwsEC2(Job):

    _type: str = attrs.field(init=False, default='Job:AWS EC2', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS EC2'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
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
    idempotent_token: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Idempotent Token'})
    tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tolerance'})
    verification_poll_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Verification Poll Interval'})
    get_instances_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Get Instances logs'})


@attrs.define
class JobAwsEMR(Job):

    _type: str = attrs.field(init=False, default='Job:AWS EMR', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS EMR'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    cluster_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'ClusterId'})
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
class JobAzureHDInsight(Job):

    _type: str = attrs.field(init=False, default='Job:Azure HDInsight', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure HDInsight'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    bring_job_logs_to_output: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Bring job logs to output'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


@attrs.define
class JobAlteryxTrifacta(Job):

    _type: str = attrs.field(init=False, default='Job:Alteryx Trifacta', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Alteryx Trifacta'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
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
class JobBoomiAtomsphere(Job):

    _type: str = attrs.field(init=False, default='Job:Boomi Atomsphere', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Boomi Atomsphere'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
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
class JobDatabricks(Job):

    _type: str = attrs.field(init=False, default='Job:Databricks', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Databricks'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    databricks_job_id: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Databricks Job ID'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    idempotency_token: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Idempotency Token'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


@attrs.define
class JobGCPBigQuery(Job):

    _type: str = attrs.field(init=False, default='Job:GCP BigQuery', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP BigQuery'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
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
    sql_statement: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'SQL Statement'})
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
class JobGCPDataFlow(Job):

    _type: str = attrs.field(init=False, default='Job:GCP DataFlow', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP DataFlow'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
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
class JobGCPDataproc(Job):

    _type: str = attrs.field(init=False, default='Job:GCP Dataproc', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Dataproc'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    project_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project ID'})
    account_region: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Account Region'})
    dataproc_task_type: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Dataproc task type'})
    workflow_template: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Workflow Template'})
    parameters__json_format: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Parameters (JSON Format)'})
    verification_poll_interval_in_seconds: str = attrs.field(kw_only=True, default=None, metadata={
                                                             '_aapi_repr_': 'Verification Poll Interval (in seconds)'})
    tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tolerance'})


@attrs.define
class JobAwsGlue(Job):

    _type: str = attrs.field(init=False, default='Job:AWS Glue', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS Glue'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    glue_job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Glue Job Name'})
    glue_job_arguments: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Glue Job Arguments'})
    arguments: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Arguments'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


@attrs.define
class JobGCPVM(Job):

    _type: str = attrs.field(init=False, default='Job:GCP VM', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP VM'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    project_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Project ID'})
    zone: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Zone'})
    operation: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Operation'})
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
class JobInformaticaCS(Job):

    _type: str = attrs.field(init=False, default='Job:Informatica CS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Informatica CS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    task_type: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Task Type'})
    use_federation_id: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Use FederationID?'})
    task_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Task Name'})
    folder_path: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Folder Path'})
    task_flow_url: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'TaskFlow URL'})
    rerun_suspended_taskflow: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Rerun suspended Taskflow'})
    rerun_run_id: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Rerun Run ID'})
    input_fields: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Input Fields'})
    call_back_url: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Call Back URL'})
    verification_poll_interval_in_seconds: str = attrs.field(kw_only=True, default=None, metadata={
                                                             '_aapi_repr_': 'Verification Poll Interval (in seconds)'})


@attrs.define
class JobMicrosoftPowerBI(Job):

    _type: str = attrs.field(init=False, default='Job:Microsoft Power BI', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Microsoft Power BI'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
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
class JobQlikCloud(Job):

    _type: str = attrs.field(init=False, default='Job:Qlik Cloud', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Qlik Cloud'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
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
class JobSnowflake(Job):

    _type: str = attrs.field(init=False, default='Job:Snowflake', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Snowflake'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    database: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Database'})
    schema: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Schema'})
    select_operation: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Select Operation'})
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
    pipe_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Pipe Name'})
    copy_into_table: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Copy Into Table'})
    copy_data_from_stage: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Copy Data From Stage'})
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
    start_or_pause_pipe: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Start Or Pause Pipe'})
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
    polling_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Polling Interval'})


@attrs.define
class JobTalendDataManagement(Job):

    _type: str = attrs.field(init=False, default='Job:Talend Data Management', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Talend Data Management'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    task_plan_execution: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Task/Plan Execution'})
    task_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Task Name'})
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
    plan_polling_intervals: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'Plan Polling Intervals'})


@attrs.define
class JobUIPath(Job):

    _type: str = attrs.field(init=False, default='Job:UI Path', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:UI Path'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
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
class JobAzureBatchAccounts(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Batch Accounts', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Batch Accounts'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
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
class JobAzureDatabricks(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Databricks', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Databricks'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    databricks_job_id: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Databricks Job ID'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    idempotency_token: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Idempotency Token'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


@attrs.define
class JobAzureFunctions(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Functions', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Functions'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    function_app: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Function App'})
    function_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Function Name'})
    optional_input_parameters_json_format: str = attrs.field(kw_only=True, default=None, metadata={
                                                              '_aapi_repr_': 'Optional Input Parameters (JSON Format)'})
    function_type: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Function Type'})


@attrs.define
class JobAzureLogicApps(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Logic Apps', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Logic Apps'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
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
class JobAzureSynapse(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Synapse', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Synapse'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    pipeline_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Pipeline Name'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    status_polling_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Status polling interval'})


@attrs.define
class JobAzureVM(Job):

    _type: str = attrs.field(init=False, default='Job:Azure VM', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure VM'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field( metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    vm_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'VM Name'})
    operation: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Operation'})
    input_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Input Parameters'})
    verification_poll_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Verification Poll Interval'})
    delete_vmos_disk: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Delete VM OS Disk'})
    tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tolerance'})
    get_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Get Logs'})
