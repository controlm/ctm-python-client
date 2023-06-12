
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
    v_m_resource_group: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'VM Resource Group'})
    v_m_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'VM Name'})
    policy_name: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Policy Name'})
    include_or_exclude_disks: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Include or Exclude Disks'})
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
    launch_type: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Launch Type'})
    assign_public_ip: str = attrs.field(kw_only=True, default=None, metadata={
        '_aapi_repr_': 'Assign Public IP'})
    network_security_groups: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Network Security Groups'})
    network_subnets: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Network Subnets'})
    override_container: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Override Container'})
    override_command: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Override Command'})
    environment_variables: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'Environment Variables'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    output_job_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Output Job Logs'})
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
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
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
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Parameters'})
    bring_job_logs_to_output: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Bring job logs to output'})
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


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
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


@attrs.define
class JobGCPBatch(Job):

    _type: str = attrs.field(init=False, default='Job:GCP Batch', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:GCP Batch'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
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
    uniq_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'UniqName'})


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
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    glue_job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Glue Job Name'})
    glue_job_arguments: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'Glue Job Arguments'})
    arguments: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Arguments'})
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
    restart_with_modified_j_c_l: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'Restart with Modified JCL'})
    modified_jcl_path_and_filename: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Modified JCL Path and Filename'})


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
    snowpipe_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Snowpipe Name'})
    copy_into_table: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Copy into Table'})
    copy_data_from_stage: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'Copy Data from Stage'})
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
    start_or_pause_snowpipe: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'Start or Pause Snowpipe'})
    table_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Table Name'})
    stage_location: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'Stage Location'})
    days_back: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Days Back'})
    status_file_cloud_location_path: str = attrs.field(kw_only=True, default=None, metadata={
                                                       '_aapi_repr_': 'Status File Cloud Location Path'})
    stoarge_integration_for_location: str = attrs.field(kw_only=True, default=None, metadata={
                                                        '_aapi_repr_': 'Stoarge Integration for Location'})
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
    status_polling_frequency: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'Status Polling Frequency'})


@attrs.define
class JobAzureFunctions(Job):

    _type: str = attrs.field(init=False, default='Job:Azure Functions', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure Functions'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    function_app: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Function App'})
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
    input_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Input Parameters'})
    verification_poll_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'Verification Poll Interval'})
    delete_vm_os_disk: str = attrs.field(kw_only=True, default=None, metadata={
        '_aapi_repr_': 'Delete VM OS Disk'})
    tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Tolerance'})
    get_logs: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Get Logs'})


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
