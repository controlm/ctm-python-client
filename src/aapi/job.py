
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class Job(AAPIObject, AAPIJob):

    @attrs.define
    class PathElement(AAPIObject):

        folder: str = attrs.field(metadata={'_aapi_repr_': 'Folder'})
        server: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Server'})
        library: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Library'})

    @attrs.define
    class DocumentationFile(AAPIObject):

        path: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Path'})
        file_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'FileName'})

    @attrs.define
    class DocumentationUrl(AAPIObject):

        url: str = attrs.field(kw_only=True, default=None,
                               metadata={'_aapi_repr_': 'Url'})
        file_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'FileName'})

    @attrs.define
    class RerunLimit(AAPIObject):

        class From(enum.Enum):

            Start = "Start"
            End = "End"
            Target = "Target"

        class Units(enum.Enum):

            Minutes = "Minutes"
            Hours = "Hours"
            Days = "Days"

        times: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Times'})
        every: int = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Every'})
        from_: From = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'From'})
        units: Units = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Units'})
        rerun_member: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'RerunMember'})

    @attrs.define
    class Rerun(AAPIObject):

        class From(enum.Enum):

            Start = "Start"
            End = "End"
            Target = "Target"

        class Units(enum.Enum):

            Minutes = "Minutes"
            Hours = "Hours"
            Days = "Days"

        times: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Times'})
        every: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Every'})
        from_: From = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'From'})
        units: Units = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Units'})

    @attrs.define
    class RerunIntervals(AAPIObject):

        class From(enum.Enum):

            Start = "Start"
            End = "End"
            Target = "Target"

        times: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Times'})
        intervals: typing.List[str] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'Intervals'})
        from_: From = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'From'})

    @attrs.define
    class RerunSpecificTimes(AAPIObject):

        times: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Times'})
        at: typing.List[str] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'At'})
        tolerance: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Tolerance'})

    @attrs.define
    class When(AAPIObject):

        @attrs.define
        class RuleBasedCalendars(AAPIObject):

            class Relationship(enum.Enum):

                AND = "AND"
                OR = "OR"

            relationship: Relationship = attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'Relationship'})
            included: typing.List[JobTag] = attrs.field(
                kw_only=True, default=None, metadata={'_aapi_repr_': 'Included'})
            excluded: typing.List[JobTag] = attrs.field(
                kw_only=True, default=None, metadata={'_aapi_repr_': 'Excluded'})

        @attrs.define
        class ConfirmationCalendars(AAPIObject):

            class ExceptionPolicy(enum.Enum):

                DoNotOrder = "DoNotOrder"
                OrderOnNextConfirmedDay = "OrderOnNextConfirmedDay"
                OrderOnPreviousConfirmedDay = "OrderOnPreviousConfirmedDay"
                OrderAnyway = "OrderAnyway"

            calendar: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Calendar'})
            shift_by: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ShiftBy'})
            exception_policy: ExceptionPolicy = attrs.field(
                kw_only=True, default=None, metadata={'_aapi_repr_': 'ExceptionPolicy'})

        class DaysRelation(enum.Enum):

            AND = "AND"
            OR = "OR"

        schedule: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Schedule'})
        month_days: typing.List[str] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'MonthDays'})
        months: typing.List[str] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'Months'})
        week_days: typing.List[str] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'WeekDays'})
        week_days_calendar: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'WeekDaysCalendar'})
        month_days_calendar: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'MonthDaysCalendar'})
        days_relation: DaysRelation = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'DaysRelation'})
        specific_dates: typing.List[str] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'SpecificDates'})
        from_time: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'FromTime'})
        days: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Days'})
        to_time: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'ToTime'})
        start_date: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'StartDate'})
        end_date: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'EndDate'})
        active_period: bool = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ActivePeriod'})
        rule_based_calendars: RuleBasedCalendars = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'RuleBasedCalendars'})
        confirmation_calendars: ConfirmationCalendars = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'ConfirmationCalendars'})

    @attrs.define
    class Output(AAPIObject):

        class Operation(enum.Enum):

            Copy = "Copy"
            Move = "Move"
            Print = "Print"
            Delete = "Delete"

        operation: Operation = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Operation'})
        destination: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Destination'})

    class Priority(enum.Enum):

        Very_High = "Very_High"
        High = "High"
        Medium = "Medium"
        Low = "Low"
        Very_Low = "Very_Low"

    class DaysKeepActive(enum.Enum):

        Forever = "Forever"

    _type: str = attrs.field(init=False, default='Job', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    path_element: PathElement = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'PathElement'})
    file_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'FileName'})
    file_path: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'FilePath'})
    host: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Host'})
    application: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Application'})
    priority: Priority = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Priority'})
    critical: bool = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Critical'})
    confirm: bool = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Confirm'})
    days_keep_active: DaysKeepActive = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DaysKeepActive'})
    description: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Description'})
    documentation_file: DocumentationFile = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DocumentationFile'})
    documentation_url: DocumentationUrl = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DocumentationUrl'})
    rerun_limit: RerunLimit = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'RerunLimit'})
    rerun: Rerun = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Rerun'})
    rerun_intervals: RerunIntervals = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'RerunIntervals'})
    rerun_specific_times: RerunSpecificTimes = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'RerunSpecificTimes'})
    post_command: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'PostCommand'})
    pre_command: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'PreCommand'})
    run_as: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'RunAs'})
    sub_application: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'SubApplication'})
    time_zone: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'TimeZone'})
    variables: typing.List[typing.Dict[str, str]] = attrs.field(
        kw_only=True, factory=list, metadata={'_aapi_repr_': 'Variables'})
    when: When = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'When'})
    run_on_all_agents_in_group: bool = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'RunOnAllAgentsInGroup'})
    output: Output = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Output'})
    run_as_dummy: bool = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'RunAsDummy'})
    retroactive_order: bool = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'RetroactiveOrder'})
    end_folder: bool = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'EndFolder'})
    created_by: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'CreatedBy'})
    if_list: typing.List[IfBase] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    event_list: typing.List[Event] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    resource_list: typing.List[Resource] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    wait_for_events: typing.List[WaitForEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    events_to_add: typing.List[AddEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    events_to_delete: typing.List[DeleteEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    notify_list: typing.List[Notify] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    job_tag_list: typing.List[JobTag] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    action_capture_output_list: typing.List[ActionCaptureOutput] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
# support backward compatibility
    wait_for_events_list: typing.List[WaitForEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    add_events_list: typing.List[AddEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    delete_events_list: typing.List[DeleteEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    condition_list: typing.List[Condition] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})

@attrs.define
class JobCommand(Job):

    _type: str = attrs.field(init=False, default='Job:Command', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Command'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    command: str = attrs.field(metadata={'_aapi_repr_': 'Command'})
    override_path: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'OverridePath'})
    run_as_dummy: bool = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'RunAsDummy'})


@attrs.define
class JobDummy(Job):

    _type: str = attrs.field(init=False, default='Job:Dummy', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Dummy'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobEmbeddedScript(Job):

    _type: str = attrs.field(init=False, default='Job:EmbeddedScript', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:EmbeddedScript'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    script: str = attrs.field(metadata={'_aapi_repr_': 'Script'})
    file_name: str = attrs.field(metadata={'_aapi_repr_': 'FileName'})
    override_path: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'OverridePath'})
    run_as_dummy: bool = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'RunAsDummy'})


@attrs.define
class JobScript(Job):

    _type: str = attrs.field(init=False, default='Job:Script', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Script'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    arguments: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Arguments'})
    file_name: str = attrs.field(metadata={'_aapi_repr_': 'FileName'})
    file_path: str = attrs.field(metadata={'_aapi_repr_': 'FilePath'})
    override_path: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'OverridePath'})
    run_as_dummy: bool = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'RunAsDummy'})


@attrs.define
class JobFileWatcher(Job):

    _type: str = attrs.field(init=False, default='Job:FileWatcher', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:FileWatcher'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    path: str = attrs.field(metadata={'_aapi_repr_': 'Path'})
    search_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'SearchInterval'})
    time_limit: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'TimeLimit'})
    start_time: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'StartTime'})
    stop_time: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'StopTime'})


@attrs.define
class JobFileWatcherCreate(JobFileWatcher):

    _type: str = attrs.field(init=False, default='Job:FileWatcher:Create', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:FileWatcher:Create'})
    # object_name: str = attrs.field(metadata={'_aapi_name_': True})
    minimum_size: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'MinimumSize'})
    file_size_interval: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'FileSizeInterval'})
    wildcard: bool = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Wildcard'})
    iterations: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Iterations'})
    minimal_age: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'MinimalAge'})
    maximal_age: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'MaximalAge'})


@attrs.define
class JobFileWatcherDelete(JobFileWatcher):

    _type: str = attrs.field(init=False, default='Job:FileWatcher:Delete', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:FileWatcher:Delete'})
    # object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobAirflow(Job):

    class OutputDetails(enum.Enum):

        DoNotIncludeTaskLogs = "DoNotIncludeTaskLogs"
        IncludeOnlyFailedTasksLogs = "IncludeOnlyFailedTasksLogs"
        IncludeAllTasksLogs = "IncludeAllTasksLogs"

    _type: str = attrs.field(init=False, default='Job:Airflow', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Airflow'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(
        metadata={'_aapi_repr_': 'ConnectionProfile'})
    dag_id: str = attrs.field(metadata={'_aapi_repr_': 'DagId'})
    configuration_json: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConfigurationJson'})
    rerun_from_point_of_failure: bool = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'RerunFromPointOfFailure'})
    output_details: OutputDetails = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'OutputDetails'})


@attrs.define
class JobAWS(Job):

    _type: str = attrs.field(init=False, default='Job:AWS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    append_log: bool = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AppendLog'})


@attrs.define
class JobAWSLambda(JobAWS):

    _type: str = attrs.field(init=False, default='Job:AWS:Lambda', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS:Lambda'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    function_name: str = attrs.field(metadata={'_aapi_repr_': 'FunctionName'})
    version: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Version'})
    payload: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Payload'})
    client_context_json: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'ClientContextJson'})


@attrs.define
class JobAWSStepFunction(JobAWS):

    _type: str = attrs.field(init=False, default='Job:AWS:StepFunction', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS:StepFunction'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    state_machine: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'StateMachine'})
    execution_name: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'ExecutionName'})
    input: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Input'})


@attrs.define
class JobAWSBatch(JobAWS):

    @attrs.define
    class DependsOn(AAPIObject):

        class DependencyType(enum.Enum):

            N_to_N = "N_to_N"
            Standard = "Standard"
            Sequential = "Sequential"

        dependency_type: DependencyType = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'DependencyType'})
        job_depends_on: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'JobDependsOn'})

    class AwsJobType(enum.Enum):

        Array = "Array"
        Single = "Single"

    _type: str = attrs.field(init=False, default='Job:AWS:Batch', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:AWS:Batch'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    job_name: str = attrs.field(metadata={'_aapi_repr_': 'JobName'})
    job_definition: str = attrs.field(
        metadata={'_aapi_repr_': 'JobDefinition'})
    job_definition_revision: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'JobDefinitionRevision'})
    job_queue: str = attrs.field(metadata={'_aapi_repr_': 'JobQueue'})
    aws_job_type: AwsJobType = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'AWSJobType'})
    array_size: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'ArraySize'})
    environment: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Environment'})
    parameters: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Parameters'})
    depends_on: DependsOn = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'DependsOn'})
    v_cpus: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'vCPUs'})
    memory: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Memory'})
    job_attempts: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'JobAttempts'})
    execution_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'ExecutionTimeout'})
    command: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Command'})


@attrs.define
class JobAzure(Job):

    _type: str = attrs.field(init=False, default='Job:Azure', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    append_log: bool = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AppendLog'})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})


@attrs.define
class JobAzureFunction(JobAzure):

    _type: str = attrs.field(init=False, default='Job:Azure:Function', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure:Function'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    function: str = attrs.field(metadata={'_aapi_repr_': 'Function'})
    function_app: str = attrs.field(metadata={'_aapi_repr_': 'FunctionApp'})
    parameters: typing.List[typing.Dict[str, str]] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Parameters'})


@attrs.define
class JobAzureLogicApps(JobAzure):

    _type: str = attrs.field(init=False, default='Job:Azure:LogicApps', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure:LogicApps'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    logic_app_name: str = attrs.field(metadata={'_aapi_repr_': 'LogicAppName'})
    request_body: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'RequestBody'})


@attrs.define
class JobAzureBatchAccount(JobAzure):

    @attrs.define
    class Wallclock(AAPIObject):

        class Unit(enum.Enum):

            Seconds = "Seconds"
            Minutes = "Minutes"
            Hours = "Hours"
            Days = "Days"

        time: str = attrs.field(metadata={'_aapi_repr_': 'Time'})
        unit: Unit = attrs.field(metadata={'_aapi_repr_': 'Unit'})

    @attrs.define
    class MaxTries(AAPIObject):

        class Option(enum.Enum):

            Unlimited = "Unlimited"
            Custom = "Custom"

        option: Option = attrs.field(metadata={'_aapi_repr_': 'Option'})
        count: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Count'})

    @attrs.define
    class Retention(AAPIObject):

        class Unit(enum.Enum):

            Seconds = "Seconds"
            Minutes = "Minutes"
            Hours = "Hours"
            Days = "Days"

        time: str = attrs.field(metadata={'_aapi_repr_': 'Time'})
        unit: Unit = attrs.field(metadata={'_aapi_repr_': 'Unit'})

    _type: str = attrs.field(init=False, default='Job:Azure:BatchAccount', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Azure:BatchAccount'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    job_id: str = attrs.field(metadata={'_aapi_repr_': 'JobId'})
    command_line: str = attrs.field(metadata={'_aapi_repr_': 'CommandLine'})
    wallclock: Wallclock = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Wallclock'})
    max_tries: MaxTries = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'MaxTries'})
    retention: Retention = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Retention'})


@attrs.define
class JobDatabase(Job):

    _type: str = attrs.field(init=False, default='Job:Database', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Database'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    autocommit: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Autocommit'})
    output_execution_log: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'OutputExecutionLog'})
    output_sql_output: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'OutputSQLOutput'})
    sql_output_format: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'SQLOutputFormat'})


@attrs.define
class JobDatabaseSQLScript(JobDatabase):

    _type: str = attrs.field(init=False, default='Job:Database:SQLScript', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Database:SQLScript'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    sql_script: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'SQLScript'})
    parameters: typing.List[typing.Dict[str, str]] = attrs.field(
        kw_only=True, factory=list, metadata={'_aapi_repr_': 'Parameters'})


@attrs.define
class JobDatabaseEmbeddedQuery(JobDatabase):

    _type: str = attrs.field(init=False, default='Job:Database:EmbeddedQuery', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Database:EmbeddedQuery'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    query: str = attrs.field(metadata={'_aapi_repr_': 'Query'})


@attrs.define
class JobDatabaseStoredProcedure(JobDatabase):

    _type: str = attrs.field(init=False, default='Job:Database:StoredProcedure', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Database:StoredProcedure'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    schema: str = attrs.field(metadata={'_aapi_repr_': 'Schema'})
    package: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Package'})
    stored_procedure: str = attrs.field(
        metadata={'_aapi_repr_': 'StoredProcedure'})
    parameters: typing.List[typing.Any] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Parameters'})
    return_value: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'ReturnValue'})


@attrs.define
class JobDatabaseMSSQLAgentJob(JobDatabase):

    _type: str = attrs.field(init=False, default='Job:Database:MSSQL:AgentJob', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Database:MSSQL:AgentJob'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    job_name: str = attrs.field(metadata={'_aapi_repr_': 'JobName'})
    category: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Category'})


@attrs.define
class JobDatabaseMSSQL_SSIS(JobDatabase):

    class PackageSource(enum.Enum):

        SSIS_Catalog = "SSIS Catalog"
        File_System = "File System"
        SSIS_Package_Store = "SSIS Package Store"
        SQL_Server = "SQL Server"

    _type: str = attrs.field(init=False, default='Job:Database:MSSQL:SSIS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Database:MSSQL:SSIS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    package_source: PackageSource = attrs.field(
        metadata={'_aapi_repr_': 'PackageSource'})
    package_name: str = attrs.field(metadata={'_aapi_repr_': 'PackageName'})
    catalog_env: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'CatalogEnv'})
    config_files: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ConfigFiles'})
    properties: typing.List[typing.Dict[str, str]] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Properties'})


@attrs.define
class JobFileTransfer(Job):

    _type: str = attrs.field(init=False, default='Job:FileTransfer', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:FileTransfer'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile_src: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'ConnectionProfileSrc'})
    connection_profile_dest: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'ConnectionProfileDest'})
    connection_profile_dual_endpoint: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ConnectionProfileDualEndpoint'})
    file_transfers: typing.List[FileTransfer] = attrs.field(
        kw_only=True, factory=list, metadata={'_aapi_repr_': 'FileTransfers'})
    s3_bucket_name: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'S3BucketName'})
    s3_bucket_name_src: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'S3BucketNameSrc'})
    s3_bucket_name_dest: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'S3BucketNameDest'})
    gcs_bucket_name_src: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'GCSBucketNameSrc'})
    gcs_bucket_name_dest: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'GCSBucketNameDest'})
    azure_container_name_src: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'AzureContainerNameSrc'})
    azure_container_name_dest: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AzureContainerNameDest'})
    end_job_not_ok: bool = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'EndJobNOTOK'})
    rerun_from_point_of_failure: bool = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'RerunFromPointOfFailure'})
    number_of_retries: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'NumberOfRetries'})


@attrs.define
class JobHadoop(Job):

    @attrs.define
    class PreCommands(AAPIObject):

        fail_job_on_command_failure: bool = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'FailJobOnCommandFailure'})
        commands: typing.List[str] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'Commands'})

    @attrs.define
    class PostCommands(AAPIObject):

        fail_job_on_command_failure: bool = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'FailJobOnCommandFailure'})
        commands: typing.List[str] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'Commands'})

    _type: str = attrs.field(init=False, default='Job:Hadoop', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Hadoop'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    pre_commands: PreCommands = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'PreCommands'})
    post_commands: PostCommands = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'PostCommands'})


@attrs.define
class JobHadoopSpark(JobHadoop):

    _type: str = attrs.field(init=False, default='Job:Hadoop:Spark', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Hadoop:Spark'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    arguments: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Arguments'})
    spark_options: typing.List[typing.Dict[str, str]] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'SparkOptions'})


@attrs.define
class JobHadoopSparkPython(JobHadoopSpark):

    _type: str = attrs.field(init=False, default='Job:Hadoop:Spark:Python', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Hadoop:Spark:Python'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    spark_script: str = attrs.field(metadata={'_aapi_repr_': 'SparkScript'})


@attrs.define
class JobHadoopSparkScalaJava(JobHadoopSpark):

    _type: str = attrs.field(init=False, default='Job:Hadoop:Spark:ScalaJava', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Hadoop:Spark:ScalaJava'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    program_jar: str = attrs.field(metadata={'_aapi_repr_': 'ProgramJar'})
    main_class: str = attrs.field(metadata={'_aapi_repr_': 'MainClass'})


@attrs.define
class JobHadoopMapReduce(JobHadoop):

    _type: str = attrs.field(init=False, default='Job:Hadoop:MapReduce', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Hadoop:MapReduce'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    program_jar: str = attrs.field(metadata={'_aapi_repr_': 'ProgramJar'})
    main_class: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'MainClass'})
    arguments: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Arguments'})


@attrs.define
class JobHadoopPig(JobHadoop):

    _type: str = attrs.field(init=False, default='Job:Hadoop:Pig', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Hadoop:Pig'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    pig_script: str = attrs.field(metadata={'_aapi_repr_': 'PigScript'})
    parameters: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Parameters'})


@attrs.define
class JobHadoopSqoop(JobHadoop):

    _type: str = attrs.field(init=False, default='Job:Hadoop:Sqoop', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Hadoop:Sqoop'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    sqoop_command: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'SqoopCommand'})
    sqoop_options: typing.List[typing.Dict[str, str]] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'SqoopOptions'})
    sqoop_archives: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'SqoopArchives'})
    sqoop_files: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'SqoopFiles'})


@attrs.define
class JobHadoopHive(JobHadoop):

    _type: str = attrs.field(init=False, default='Job:Hadoop:Hive', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Hadoop:Hive'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    hive_script: str = attrs.field(metadata={'_aapi_repr_': 'HiveScript'})
    parameters: typing.List[typing.Dict[str, str]] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Parameters'})
    hive_archives: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'HiveArchives'})
    hive_files: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'HiveFiles'})
    hive_options: typing.List[typing.Dict[str, str]] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'HiveOptions'})


@attrs.define
class JobHadoopDistCp(JobHadoop):

    _type: str = attrs.field(init=False, default='Job:Hadoop:DistCp', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Hadoop:DistCp'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    target_path: str = attrs.field(metadata={'_aapi_repr_': 'TargetPath'})
    source_paths: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'SourcePaths'})
    distcp_options: typing.List[typing.Dict[str, str]] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DistcpOptions'})


@attrs.define
class JobHadoopHDFSCommands(JobHadoop):

    _type: str = attrs.field(init=False, default='Job:Hadoop:HDFSCommands', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Hadoop:HDFSCommands'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    commands: typing.List[typing.Dict[str, str]] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Commands'})


@attrs.define
class JobHadoopOozie(JobHadoop):

    _type: str = attrs.field(init=False, default='Job:Hadoop:Oozie', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Hadoop:Oozie'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    job_properties_file: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'JobPropertiesFile'})
    oozie_options: typing.List[typing.Dict[str, str]] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'OozieOptions'})


@attrs.define
class JobHadoopMapredStreaming(JobHadoop):

    _type: str = attrs.field(init=False, default='Job:Hadoop:MapredStreaming', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Hadoop:MapredStreaming'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    input_path: str = attrs.field(metadata={'_aapi_repr_': 'InputPath'})
    output_path: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'OutputPath'})
    mapper_command: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'MapperCommand'})
    reducer_command: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'ReducerCommand'})
    steaming_options: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'SteamingOptions'})
    general_options: typing.List[typing.Dict[str, str]] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'GeneralOptions'})


@attrs.define
class JobHadoopHDFSFileWatcher(JobHadoop):

    _type: str = attrs.field(init=False, default='Job:Hadoop:HDFSFileWatcher', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Hadoop:HDFSFileWatcher'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    hdfs_file_path: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'HdfsFilePath'})
    min_detected_size: str = attrs.field(kw_only=True, default=None, metadata={
        '_aapi_repr_': 'MinDetecedSize'})
    max_wait_time: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'MaxWaitTime'})


@attrs.define
class JobHadoopTajo(JobHadoop):

    _type: str = attrs.field(init=False, default='Job:Hadoop:Tajo', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Hadoop:Tajo'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    arguments: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Arguments'})
    tajo_options: typing.List[typing.Dict[str, str]] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'TajoOptions'})


@attrs.define
class JobHadoopTajoInputFile(JobHadoopTajo):

    _type: str = attrs.field(init=False, default='Job:Hadoop:Tajo:InputFile', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Hadoop:Tajo:InputFile'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    full_file_path: str = attrs.field(metadata={'_aapi_repr_': 'FullFilePath'})


@attrs.define
class JobHadoopTajoQuery(JobHadoopTajo):

    _type: str = attrs.field(init=False, default='Job:Hadoop:Tajo:Query', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Hadoop:Tajo:Query'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    open_query: str = attrs.field(metadata={'_aapi_repr_': 'OpenQuery'})


@attrs.define
class JobIBMDataStage(Job):

    _type: str = attrs.field(init=False, default='Job:IBMDataStage', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:IBMDataStage'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(
        metadata={'_aapi_repr_': 'ConnectionProfile'})
    project: str = attrs.field(metadata={'_aapi_repr_': 'Project'})
    data_stage_job: str = attrs.field(metadata={'_aapi_repr_': 'DataStageJob'})


@attrs.define
class JobIBMCognos(Job):

    _type: str = attrs.field(init=False, default='Job:IBMCognos', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:IBMCognos'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(
        metadata={'_aapi_repr_': 'ConnectionProfile'})
    jobs: str = attrs.field(metadata={'_aapi_repr_': 'Jobs'})


@attrs.define
class JobInformatica(Job):

    class WorkflowExecutionMode(enum.Enum):

        RunWholeWorkflow = "RunWholeWorkflow"
        StartFromTask = "StartFromTask"
        RunSingleTask = "RunSingleTask"

    class WorkflowRestartMode(enum.Enum):

        Recover = "Recover"
        ForceRestart = "ForceRestart"
        ForceRestartFromSpecificTask = "ForceRestartFromSpecificTask"

    _type: str = attrs.field(init=False, default='Job:Informatica', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Informatica'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(
        metadata={'_aapi_repr_': 'ConnectionProfile'})
    repository_folder: str = attrs.field(
        metadata={'_aapi_repr_': 'RepositoryFolder'})
    workflow: str = attrs.field(metadata={'_aapi_repr_': 'Workflow'})
    instance_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'InstanceName'})
    os_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'OsProfile'})
    workflow_execution_mode: WorkflowExecutionMode = attrs.field(
        metadata={'_aapi_repr_': 'WorkflowExecutionMode'})
    start_from_task: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'StartFromTask'})
    run_single_task: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'RunSingleTask'})
    workflow_restart_mode: WorkflowRestartMode = attrs.field(
        metadata={'_aapi_repr_': 'WorkflowRestartMode'})
    restart_from_task: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'RestartFromTask'})
    depth: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Depth'})
    enable_error_details: bool = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'EnableErrorDetails'})
    enable_output: bool = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'EnableOutput'})
    workflow_parameters_file: str = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'WorkflowParametersFile'})


@attrs.define
class JobJava(Job):

    _type: str = attrs.field(init=False, default='Job:Java', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Java'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(
        metadata={'_aapi_repr_': 'ConnectionProfile'})
    object: str = attrs.field(metadata={'_aapi_repr_': 'Object'})
    method: str = attrs.field(metadata={'_aapi_repr_': 'Method'})
    java_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'JavaProfile'})


@attrs.define
class JobMessaging(Job):

    _type: str = attrs.field(init=False, default='Job:Messaging', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Messaging'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})


@attrs.define
class JobMessagingFreeText(JobMessaging):

    _type: str = attrs.field(init=False, default='Job:Messaging:FreeText', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Messaging:FreeText'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    use_free_text_message: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'UseFreeTextMessage'})


@attrs.define
class JobMessagingWaitForReply(JobMessaging):

    _type: str = attrs.field(init=False, default='Job:Messaging:WaitForReply', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Messaging:WaitForReply'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobMessagingPreDefined(JobMessaging):

    _type: str = attrs.field(init=False, default='Job:Messaging:PreDefined', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Messaging:PreDefined'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    use_free_text_message: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'UseFreeTextMessage'})


@attrs.define
class JobNetBackup(Job):

    _type: str = attrs.field(init=False, default='Job:NetBackup', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:NetBackup'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(
        metadata={'_aapi_repr_': 'ConnectionProfile'})
    policy_name: str = attrs.field(metadata={'_aapi_repr_': 'PolicyName'})


@attrs.define
class JobOEBS(Job):

    @attrs.define
    class SingleRequest(AAPIObject):

        program_name: str = attrs.field(
            metadata={'_aapi_repr_': 'ProgramName'})

    @attrs.define
    class RequestSet(AAPIObject):

        set: str = attrs.field(metadata={'_aapi_repr_': 'Set'})

    _type: str = attrs.field(init=False, default='Job:OEBS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OEBS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(
        metadata={'_aapi_repr_': 'ConnectionProfile'})
    user_name: str = attrs.field(metadata={'_aapi_repr_': 'UserName'})
    responsibility: str = attrs.field(
        metadata={'_aapi_repr_': 'Responsibility'})
    single_request: SingleRequest = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'SingleRequest'})
    request_set: RequestSet = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'RequestSet'})


@attrs.define
class JobOS400(Job):

    _type: str = attrs.field(init=False, default='Job:OS400', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OS400'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobOS400Program(JobOS400):

    class SpecialEnvironment(enum.Enum):

        S38 = "S38"
        QShell = "QShell"
        Native = "Native"

    _type: str = attrs.field(init=False, default='Job:OS400:Program', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OS400:Program'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    program: str = attrs.field(metadata={'_aapi_repr_': 'Program'})
    library: str = attrs.field(metadata={'_aapi_repr_': 'Library'})
    special_environment: SpecialEnvironment = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'SpecialEnvironment'})


@attrs.define
class JobOS400MultipleCommands(JobOS400):

    _type: str = attrs.field(init=False, default='Job:OS400:MultipleCommands', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OS400:MultipleCommands'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobOS400VirtualTerminal(JobOS400):

    @attrs.define
    class NativeScriptFileLocation(AAPIObject):

        v_t_script_file_native: str = attrs.field(
            metadata={'_aapi_repr_': 'VTScriptFileNative'})

    @attrs.define
    class IFSScriptFileLocation(AAPIObject):

        v_t_script_file_i_f_s: str = attrs.field(
            metadata={'_aapi_repr_': 'VTScriptFileIFS'})

    @attrs.define
    class EmbeddedScriptFileLocation(AAPIObject):

        v_t_script_file_embedded: str = attrs.field(
            metadata={'_aapi_repr_': 'VTScriptFileEmbedded'})
        script: str = attrs.field(metadata={'_aapi_repr_': 'Script'})
        use_instream_jcl: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'useInstreamJcl'})

    _type: str = attrs.field(init=False, default='Job:OS400:VirtualTerminal', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OS400:VirtualTerminal'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    native_script_file_location: NativeScriptFileLocation = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'NativeScriptFileLocation'})
    i_f_s_script_file_location: IFSScriptFileLocation = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'IFSScriptFileLocation'})
    embedded_script_file_location: EmbeddedScriptFileLocation = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'EmbeddedScriptFileLocation'})


@attrs.define
class JobOS400ExternalJob(JobOS400):

    class Status(enum.Enum):

        Active = "Active"
        All = "All"
        Queue = "Queue"
        OutputQueue = "OutputQueue"

    class DuplicateOption(enum.Enum):

        First = "First"
        Last = "Last"

    _type: str = attrs.field(init=False, default='Job:OS400:ExternalJob', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OS400:ExternalJob'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    status: Status = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Status'})
    duplicate_option: DuplicateOption = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DuplicateOption'})


@attrs.define
class JobOS400ExternalSubSystem(JobOS400):

    _type: str = attrs.field(init=False, default='Job:OS400:ExternalSubSystem', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OS400:ExternalSubSystem'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobOS400Full(JobOS400):

    _type: str = attrs.field(init=False, default='Job:OS400:Full', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OS400:Full'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobOS400FullScriptFile(JobOS400Full):

    @attrs.define
    class NativeScriptFileLocation(AAPIObject):

        v_t_script_file_native: str = attrs.field(
            metadata={'_aapi_repr_': 'VTScriptFileNative'})
        script: str = attrs.field(metadata={'_aapi_repr_': 'script'})
        use_instream_jcl: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'useInstreamJcl'})
        library: str = attrs.field(metadata={'_aapi_repr_': 'Library'})

    @attrs.define
    class IFSScriptFileLocation(AAPIObject):

        v_t_script_file_i_f_s: str = attrs.field(
            metadata={'_aapi_repr_': 'VTScriptFileIFS'})
        path: str = attrs.field(metadata={'_aapi_repr_': 'Path'})
        script: str = attrs.field(metadata={'_aapi_repr_': 'script'})

    @attrs.define
    class EmbeddedScriptFileLocation(AAPIObject):

        v_t_script_file_embedded: str = attrs.field(
            metadata={'_aapi_repr_': 'VTScriptFileEmbedded'})
        script: str = attrs.field(metadata={'_aapi_repr_': 'script'})
        use_instream_jcl: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'useInstreamJcl'})

    class SpecialEnvironment(enum.Enum):

        S38 = "S38"
        QShell = "QShell"
        Native = "Native"

    _type: str = attrs.field(init=False, default='Job:OS400:Full:ScriptFile', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OS400:Full:ScriptFile'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    special_environment: SpecialEnvironment = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'SpecialEnvironment'})
    native_script_file_location: NativeScriptFileLocation = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'NativeScriptFileLocation'})
    i_f_s_script_file_location: IFSScriptFileLocation = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'IFSScriptFileLocation'})
    embedded_script_file_location: EmbeddedScriptFileLocation = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'EmbeddedScriptFileLocation'})


@attrs.define
class JobOS400FullCommandLine(JobOS400Full):

    class SpecialEnvironment(enum.Enum):

        S38 = "S38"
        QShell = "QShell"
        Native = "Native"

    _type: str = attrs.field(init=False, default='Job:OS400:Full:CommandLine', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OS400:Full:CommandLine'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    command_line: str = attrs.field(metadata={'_aapi_repr_': 'CommandLine'})
    special_environment: SpecialEnvironment = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'SpecialEnvironment'})


@attrs.define
class JobOS400FullSubSystem(JobOS400Full):

    _type: str = attrs.field(init=False, default='Job:OS400:Full:SubSystem', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OS400:Full:SubSystem'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    library: str = attrs.field(metadata={'_aapi_repr_': 'Library'})
    sub_system: str = attrs.field(metadata={'_aapi_repr_': 'SubSystem'})


@attrs.define
class JobOS400FullDescriptionJob(JobOS400Full):

    _type: str = attrs.field(init=False, default='Job:OS400:Full:DescriptionJob', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OS400:Full:DescriptionJob'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    library: str = attrs.field(metadata={'_aapi_repr_': 'Library'})
    description: str = attrs.field(metadata={'_aapi_repr_': 'Description'})


@attrs.define
class JobOS400FullRestrictedStateAction(JobOS400Full):

    class Action(enum.Enum):

        SaveEntireSystem = "SaveEntireSystem"
        SaveOperationSystem = "SaveOperationSystem"
        RunReclaimStorage = "RunReclaimStorage"
        ExecuteCommand = "ExecuteCommand"

    _type: str = attrs.field(init=False, default='Job:OS400:Full:RestrictedStateAction', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OS400:Full:RestrictedStateAction'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    action: Action = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Action'})
    device: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Device'})
    batch_time_limit: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'BatchTimeLimit '})
    command: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'command '})


@attrs.define
class JobOS400FullProgram(JobOS400Full):

    class SpecialEnvironment(enum.Enum):

        S38 = "S38"
        QShell = "QShell"
        Native = "Native"

    _type: str = attrs.field(init=False, default='Job:OS400:Full:Program', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OS400:Full:Program'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    program: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Program'})
    library: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Library'})
    special_environment: SpecialEnvironment = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'SpecialEnvironment'})


@attrs.define
class JobOS400FullMultipleCommands(JobOS400Full):

    _type: str = attrs.field(init=False, default='Job:OS400:Full:MultipleCommands', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OS400:Full:MultipleCommands'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobOS400FullVirtualTerminal(JobOS400Full):

    @attrs.define
    class NativeScriptFileLocation(AAPIObject):

        v_t_script_file_native: str = attrs.field(
            metadata={'_aapi_repr_': 'VTScriptFileNative'})

    @attrs.define
    class IFSScriptFileLocation(AAPIObject):

        v_t_script_file_i_f_s: str = attrs.field(
            metadata={'_aapi_repr_': 'VTScriptFileIFS'})

    @attrs.define
    class EmbeddedScriptFileLocation(AAPIObject):

        v_t_script_file_embedded: str = attrs.field(
            metadata={'_aapi_repr_': 'VTScriptFileEmbedded'})
        script: str = attrs.field(metadata={'_aapi_repr_': 'Script'})
        use_instream_jcl: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'useInstreamJcl'})

    _type: str = attrs.field(init=False, default='Job:OS400:Full:VirtualTerminal', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OS400:Full:VirtualTerminal'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    native_script_file_location: NativeScriptFileLocation = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'NativeScriptFileLocation'})
    i_f_s_script_file_location: IFSScriptFileLocation = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'IFSScriptFileLocation'})
    embedded_script_file_location: EmbeddedScriptFileLocation = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'EmbeddedScriptFileLocation'})


@attrs.define
class JobOS400FullExternalJob(JobOS400Full):

    class Status(enum.Enum):

        Active = "Active"
        All = "All"
        Queue = "Queue"
        OutputQueue = "OutputQueue"

    class DuplicateOption(enum.Enum):

        First = "First"
        Last = "Last"

    _type: str = attrs.field(init=False, default='Job:OS400:Full:ExternalJob', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OS400:Full:ExternalJob'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    status: Status = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Status'})
    duplicate_option: DuplicateOption = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DuplicateOption'})


@attrs.define
class JobOS400FullExternalSubSystem(JobOS400Full):

    _type: str = attrs.field(init=False, default='Job:OS400:Full:ExternalSubSystem', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:OS400:Full:ExternalSubSystem'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobPeopleSoft(Job):

    _type: str = attrs.field(init=False, default='Job:PeopleSoft', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:PeopleSoft'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    user: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'User'})
    control_id: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'ControlId'})
    server_name: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'ServerName'})
    process_type: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'ProcessType'})
    process_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'ProcessName'})
    append_to_output: bool = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AppendToOutput'})
    bind_variables: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'BindVariables'})


@attrs.define
class JobSAP(Job):

    _type: str = attrs.field(init=False, default='Job:SAP', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})


@attrs.define
class JobSAPR3(JobSAP):

    _type: str = attrs.field(init=False, default='Job:SAP:R3', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:R3'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    new_job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'NewJobName'})


@attrs.define
class JobSAPR3COPY(JobSAPR3):

    @attrs.define
    class PostJobAction(AAPIObject):

        class Spool(enum.Enum):

            CopyToOutput = "CopyToOutput"
            CopyToFile = "CopyToFile"
            Comment = "Comment"

        class JobLog(enum.Enum):

            DoNotCopy = "DoNotCopy"
            CopyToOutput = "CopyToOutput"
            CopyToFile = "CopyToFile"

        spool: Spool = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Spool'})
        spool_file: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'SpoolFile'})
        spool_save_to_p_d_f: bool = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'SpoolSaveToPDF'})
        job_log: JobLog = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'JobLog'})
        job_log_file: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'JobLogFile'})
        job_completion_status_will_depend_on_application_status: bool = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'JobCompletionStatusWillDependOnApplicationStatus'})

    @attrs.define
    class DetectSpawnedJob(AAPIObject):

        class DetectAndCreate(enum.Enum):

            CurrentJobDefinition = "CurrentJobDefinition"
            SpecificJobDefinition = "SpecificJobDefinition"
            Comment = "Comment"

        detect_and_create: DetectAndCreate = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'DetectAndCreate'})
        job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'JobName'})
        start_spawned_job: bool = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'StartSpawnedJob'})
        job_end_in_control_m_only_aftre_child_jobs_complete_on_sap: bool = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'JobEndInControlMOnlyAftreChildJobsCompleteOnSap'})
        job_completion_status_depends_on_child_jobs_status: bool = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'JobCompletionStatusDependsOnChildJobsStatus'})

    class Exec(enum.Enum):

        Group = "Group"
        Server = "Server"

    class JobCount(enum.Enum):

        FirstScheduled = "FirstScheduled"
        LastScheduled = "LastScheduled"
        First = "First"
        Last = "Last"
        SpecificJob = "SpecificJob"

    class StartCondition(enum.Enum):

        ASAP = "ASAP"
        Immediate = "Immediate"
        AfterEvent = "AfterEvent"

    _type: str = attrs.field(init=False, default='Job:SAP:R3:COPY', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:R3:COPY'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    sap_job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'SapJobName'})
    exec: Exec = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'Exec'})
    target: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Target'})
    job_count: JobCount = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'JobCount'})
    job_count_specific_name: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'JobCountSpecificName'})
    new_job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'NewJobName'})
    start_condition: StartCondition = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'StartCondition'})
    after_event: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AfterEvent'})
    after_event_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AfterEventParameters'})
    rerun_from_point_of_failure: bool = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'RerunFromPointOfFailure'})
    copy_from_step: int = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'CopyFromStep'})
    post_job_action: PostJobAction = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'PostJobAction'})
    detect_spawned_job: DetectSpawnedJob = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DetectSpawnedJob'})


@attrs.define
class JobSAPR3CREATE(JobSAPR3):

    @attrs.define
    class PostJobAction(AAPIObject):

        class Spool(enum.Enum):

            CopyToOutput = "CopyToOutput"
            CopyToFile = "CopyToFile"
            Comment = "Comment"

        class JobLog(enum.Enum):

            DoNotCopy = "DoNotCopy"
            CopyToOutput = "CopyToOutput"
            CopyToFile = "CopyToFile"

        spool: Spool = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Spool'})
        spool_file: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'SpoolFile'})
        spool_save_to_p_d_f: bool = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'SpoolSaveToPDF'})
        job_log: JobLog = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'JobLog'})
        job_log_file: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'JobLogFile'})
        job_completion_status_will_depend_on_application_status: bool = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'JobCompletionStatusWillDependOnApplicationStatus'})

    @attrs.define
    class DetectSpawnedJob(AAPIObject):

        class DetectAndCreate(enum.Enum):

            CurrentJobDefinition = "CurrentJobDefinition"
            SpecificJobDefinition = "SpecificJobDefinition"
            Comment = "Comment"

        detect_and_create: DetectAndCreate = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'DetectAndCreate'})
        job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'JobName'})
        start_spawned_job: bool = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'StartSpawnedJob'})
        job_end_in_control_m_only_aftre_child_jobs_complete_on_sap: bool = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'JobEndInControlMOnlyAftreChildJobsCompleteOnSap'})
        job_completion_status_depends_on_child_jobs_status: bool = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'JobCompletionStatusDependsOnChildJobsStatus'})

    @attrs.define
    class SpoolListRecipient(AAPIObject):

        class RecipientType(enum.Enum):

            ExternalAddress = "ExternalAddress"
            SapUserName = "SapUserName"
            SharedDistributionList = "SharedDistributionList"
            PrivateDistributionList = "PrivateDistributionList"
            FaxNumber = "FaxNumber"
            TelexNumber = "TelexNumber"
            InternetAddress = "InternetAddress"
            X400Address = "X400Address"
            RemoteMailAddress = "RemoteMailAddress"
            Comment = "Comment"

        recipient_type: RecipientType = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'RecipientType'})
        recipient_name: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'RecipientName'})
        recipient_copy: bool = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'RecipientCopy'})
        recipient_blind_copy: bool = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'RecipientBlindCopy'})
        recipient_express: bool = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'RecipientExpress'})
        recipt_no_forwarding: bool = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'ReciptNoForwarding'})

    class Exec(enum.Enum):

        Group = "Group"
        Server = "Server"

    class StartCondition(enum.Enum):

        ASAP = "ASAP"
        Immediate = "Immediate"
        AfterEvent = "AfterEvent"

    class JobClass(enum.Enum):

        A = "A"
        B = "B"
        C = "C"

    _type: str = attrs.field(init=False, default='Job:SAP:R3:CREATE', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:R3:CREATE'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    sap_job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'SapJobName'})
    exec: Exec = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'Exec'})
    target: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Target'})
    start_condition: StartCondition = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'StartCondition'})
    after_event: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AfterEvent'})
    after_event_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AfterEventParameters'})
    rerun_from_step: int = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'RerunFromStep'})
    job_class: JobClass = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'JobClass'})
    new_job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'NewJobName'})
    rerun_from_point_of_failure: bool = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'RerunFromPointOfFailure'})
    copy_from_step: int = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'CopyFromStep'})
    post_job_action: PostJobAction = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'PostJobAction'})
    detect_spawned_job: DetectSpawnedJob = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DetectSpawnedJob'})
    spool_list_recipient: SpoolListRecipient = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'SpoolListRecipient'})


@attrs.define
class JobSAPR3PredefinedSapJob(JobSAPR3):

    @attrs.define
    class PostJobAction(AAPIObject):

        class Spool(enum.Enum):

            CopyToOutput = "CopyToOutput"
            CopyToFile = "CopyToFile"
            Comment = "Comment"

        class JobLog(enum.Enum):

            DoNotCopy = "DoNotCopy"
            CopyToOutput = "CopyToOutput"
            CopyToFile = "CopyToFile"

        spool: Spool = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Spool'})
        spool_file: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'SpoolFile'})
        spool_save_to_p_d_f: bool = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'SpoolSaveToPDF'})
        job_log: JobLog = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'JobLog'})
        job_log_file: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'JobLogFile'})
        job_completion_status_will_depend_on_application_status: bool = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'JobCompletionStatusWillDependOnApplicationStatus'})

    @attrs.define
    class DetectSpawnedJob(AAPIObject):

        class DetectAndCreate(enum.Enum):

            CurrentJobDefinition = "CurrentJobDefinition"
            SpecificJobDefinition = "SpecificJobDefinition"
            Comment = "Comment"

        detect_and_create: DetectAndCreate = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'DetectAndCreate'})
        job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'JobName'})
        start_spawned_job: bool = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'StartSpawnedJob'})
        job_end_in_control_m_only_aftre_child_jobs_complete_on_sap: bool = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'JobEndInControlMOnlyAftreChildJobsCompleteOnSap'})
        job_completion_status_depends_on_child_jobs_status: bool = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'JobCompletionStatusDependsOnChildJobsStatus'})

    class Exec(enum.Enum):

        Group = "Group"
        Server = "Server"

    class StartCondition(enum.Enum):

        ASAP = "ASAP"
        Immediate = "Immediate"
        AfterEvent = "AfterEvent"

    class JobCount(enum.Enum):

        FirstScheduled = "FirstScheduled"
        LastScheduled = "LastScheduled"
        SpecificJob = "SpecificJob"

    _type: str = attrs.field(init=False, default='Job:SAP:R3:PredefinedSapJob', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:R3:PredefinedSapJob'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    sap_job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'SapJobName'})
    exec: Exec = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'Exec'})
    target: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Target'})
    start_condition: StartCondition = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'StartCondition'})
    after_event: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'AfterEvent'})
    after_event_parameters: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AfterEventParameters'})
    rerun_from_step: int = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'RerunFromStep'})
    job_count: JobCount = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'JobCount'})
    job_count_specific_name: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'JobCountSpecificName'})
    rerun_from_point_of_failure: bool = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'RerunFromPointOfFailure'})
    copy_from_step: int = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'CopyFromStep'})
    post_job_action: PostJobAction = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'PostJobAction'})
    detect_spawned_job: DetectSpawnedJob = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DetectSpawnedJob'})


@attrs.define
class JobSAPR3MonitorSapJob(JobSAPR3):

    @attrs.define
    class DetectSpawnedJob(AAPIObject):

        class DetectAndCreate(enum.Enum):

            CurrentJobDefinition = "CurrentJobDefinition"
            SpecificJobDefinition = "SpecificJobDefinition"
            Comment = "Comment"

        detect_and_create: DetectAndCreate = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'DetectAndCreate'})
        job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'JobName'})
        start_spawned_job: bool = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'StartSpawnedJob'})
        job_end_in_control_m_only_aftre_child_jobs_complete_on_sap: bool = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'JobEndInControlMOnlyAftreChildJobsCompleteOnSap'})
        job_completion_status_depends_on_child_jobs_status: bool = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'JobCompletionStatusDependsOnChildJobsStatus'})

    class JobCount(enum.Enum):

        SpecificJob = "SpecificJob"

    _type: str = attrs.field(init=False, default='Job:SAP:R3:MonitorSapJob', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:R3:MonitorSapJob'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    sap_job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'SapJobName'})
    job_count: JobCount = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'JobCount'})
    job_count_specific_name: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'JobCountSpecificName'})
    rerun_from_point_of_failure: bool = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'RerunFromPointOfFailure'})
    copy_from_step: int = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'CopyFromStep'})
    rerun_from_step: int = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'RerunFromStep'})
    detect_spawned_job: DetectSpawnedJob = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DetectSpawnedJob'})


@attrs.define
class JobSAPR3BatchInputSession(JobSAPR3):

    @attrs.define
    class Session(AAPIObject):

        name: str = attrs.field(metadata={'_aapi_repr_': 'Name'})

    @attrs.define
    class Pattern(AAPIObject):

        name: str = attrs.field(metadata={'_aapi_repr_': 'Name'})

    class Exec(enum.Enum):

        Server = "Server"

    _type: str = attrs.field(init=False, default='Job:SAP:R3:BatchInputSession', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:R3:BatchInputSession'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    exec: Exec = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'Exec'})
    target: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Target'})
    session: Session = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Session'})
    pattern: Pattern = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Pattern'})


@attrs.define
class JobSAPR3SapProfile(JobSAPR3):

    _type: str = attrs.field(init=False, default='Job:SAP:R3:SapProfile', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:R3:SapProfile'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobSAPR3SapProfileActivate(JobSAPR3SapProfile):

    @attrs.define
    class ProfileInformation(AAPIObject):

        profile_type: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ProfileType'})
        profile_id: str = attrs.field(metadata={'_aapi_repr_': 'ProfileID'})

    _type: str = attrs.field(init=False, default='Job:SAP:R3:SapProfile:Activate', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:R3:SapProfile:Activate'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    profile_information: ProfileInformation = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ProfileInformation'})


@attrs.define
class JobSAPR3SapProfileDeactivate(JobSAPR3SapProfile):

    @attrs.define
    class ProfileInformation(AAPIObject):

        profile_type: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ProfileType'})

    _type: str = attrs.field(init=False, default='Job:SAP:R3:SapProfile:Deactivate', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:R3:SapProfile:Deactivate'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    profile_information: ProfileInformation = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ProfileInformation'})


@attrs.define
class JobSAPR3TriggerSapEvent(JobSAPR3):

    _type: str = attrs.field(init=False, default='Job:SAP:R3:TriggerSapEvent', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:R3:TriggerSapEvent'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    event_id: str = attrs.field(metadata={'_aapi_repr_': 'EventId'})
    parameter: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Parameter'})


@attrs.define
class JobSAPR3WatchSapEvent(JobSAPR3):

    _type: str = attrs.field(init=False, default='Job:SAP:R3:WatchSapEvent', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:R3:WatchSapEvent'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    event_id: str = attrs.field(metadata={'_aapi_repr_': 'EventId'})
    parameter: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Parameter'})


@attrs.define
class JobSAPBW(JobSAP):

    @attrs.define
    class DetectSpawnedJob(AAPIObject):

        class DetectAndCreate(enum.Enum):

            CurrentJobDefinition = "CurrentJobDefinition"
            SpecificJobDefinition = "SpecificJobDefinition"
            Comment = "Comment"

        detect_and_create: DetectAndCreate = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'DetectAndCreate'})
        job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'JobName'})
        start_spawned_job: bool = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'StartSpawnedJob'})
        job_end_in_control_m_only_aftre_child_jobs_complete_on_sap: bool = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'JobEndInControlMOnlyAftreChildJobsCompleteOnSap'})
        job_completion_status_depends_on_child_jobs_status: bool = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'JobCompletionStatusDependsOnChildJobsStatus'})

    _type: str = attrs.field(init=False, default='Job:SAP:BW', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:BW'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    detect_spawned_job: DetectSpawnedJob = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DetectSpawnedJob'})


@attrs.define
class JobSAPBWProcessChain(JobSAPBW):

    class RerunOption(enum.Enum):

        RestartFromFailiurePoint = "RestartFromFailiurePoint"
        RerunFromStart = "RerunFromStart"

    _type: str = attrs.field(init=False, default='Job:SAP:BW:ProcessChain', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:BW:ProcessChain'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    rerun_option: RerunOption = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'RerunOption'})
    process_chain_description: str = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'ProcessChainDescription'})
    id: str = attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'Id'})
    enable_peridoic_job: bool = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'EnablePeridoicJob'})
    consider_only_overall_chain_status: bool = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ConsiderOnlyOverallChainStatus'})
    retrieve_log: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'RetrieveLog'})


@attrs.define
class JobSAPBWInfoPackage(JobSAPBW):

    @attrs.define
    class InfoPackage(AAPIObject):

        description: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Description'})
        tech_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'TechName'})
        background_job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'BackgroundJobName'})

    _type: str = attrs.field(init=False, default='Job:SAP:BW:InfoPackage', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:BW:InfoPackage'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    info_package: InfoPackage = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'InfoPackage'})


@attrs.define
class JobSAPDataArchiving(JobSAP):

    class StartCondition(enum.Enum):

        ASAP = "ASAP"
        Immediate = "Immediate"
        AfterEvent = "AfterEvent"

    _type: str = attrs.field(init=False, default='Job:SAP:DataArchiving', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:DataArchiving'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    start_condition: StartCondition = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'StartCondition'})


@attrs.define
class JobSAPDataArchivingWrite(JobSAPDataArchiving):

    @attrs.define
    class Variant(AAPIObject):

        name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Name'})
        language: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'Language'})
        user: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'User'})

    @attrs.define
    class Validations(AAPIObject):

        check_sessions: bool = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'CheckSessions'})
        check_variants: bool = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'CheckVariants'})

    @attrs.define
    class DetectSpawnedJob(AAPIObject):

        class DetectAndCreate(enum.Enum):

            CurrentJobDefinition = "CurrentJobDefinition"
            SpecificJobDefinition = "SpecificJobDefinition"
            Comment = "Comment"

        detect_and_create: DetectAndCreate = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'DetectAndCreate'})
        job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'JobName'})
        start_spawned_job: bool = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'StartSpawnedJob'})

    class JobClass(enum.Enum):

        High = "High"
        Medium = "Medium"
        Low = "Low"

    _type: str = attrs.field(init=False, default='Job:SAP:DataArchiving:Write', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:DataArchiving:Write'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    job_name: str = attrs.field(metadata={'_aapi_repr_': 'JobName'})
    archiving_object: str = attrs.field(
        metadata={'_aapi_repr_': 'ArchivingObject'})
    target: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Target'})
    job_class: JobClass = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'JobClass'})
    copy_spool_file_to: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'CopySpoolFileTo'})
    variant: Variant = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Variant'})
    validations: Validations = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Validations'})
    detect_spawned_job: DetectSpawnedJob = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DetectSpawnedJob'})


@attrs.define
class JobSAPDataArchivingDelete(JobSAPDataArchiving):

    _type: str = attrs.field(init=False, default='Job:SAP:DataArchiving:Delete', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:DataArchiving:Delete'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    job_name: str = attrs.field(metadata={'_aapi_repr_': 'JobName'})
    archiving_object: str = attrs.field(
        metadata={'_aapi_repr_': 'ArchivingObject'})
    target: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Target'})
    session_number: int = attrs.field(
        metadata={'_aapi_repr_': 'SessionNumber'})
    copy_spool_file_to: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'CopySpoolFileTo'})


@attrs.define
class JobSAPDataArchivingStore(JobSAPDataArchiving):

    _type: str = attrs.field(init=False, default='Job:SAP:DataArchiving:Store', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SAP:DataArchiving:Store'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    job_name: str = attrs.field(metadata={'_aapi_repr_': 'JobName'})
    archiving_object: str = attrs.field(
        metadata={'_aapi_repr_': 'ArchivingObject'})
    target: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Target'})
    session_number: int = attrs.field(
        metadata={'_aapi_repr_': 'SessionNumber'})
    copy_spool_file_to: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'CopySpoolFileTo'})


@attrs.define
class JobSLAManagement(Job):

    @attrs.define
    class AverageRunTimeTolerance(AAPIObject):

        class Units(enum.Enum):

            Minutes = "Minutes"
            Percentage = "Percentage"

        average_run_time: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'AverageRunTime'})
        units: Units = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Units'})

    @attrs.define
    class CompleteBy(AAPIObject):

        time: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Time'})
        days: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Days'})

    @attrs.define
    class CompleteIn(AAPIObject):

        time: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Time'})

    _type: str = attrs.field(init=False, default='Job:SLAManagement', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:SLAManagement'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    run_as_dummy: bool = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'RunAsDummy'})
    service_name: str = attrs.field(metadata={'_aapi_repr_': 'ServiceName'})
    service_priority: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ServicePriority'})
    job_runs_deviations_tolerance: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'JobRunsDeviationsTolerance'})
    average_run_time_tolerance: AverageRunTimeTolerance = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AverageRunTimeTolerance'})
    complete_by: CompleteBy = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'CompleteBy'})
    complete_in: CompleteIn = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'CompleteIn'})


@attrs.define
class JobTandem(Job):

    _type: str = attrs.field(init=False, default='Job:Tandem', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Tandem'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    job_owner: str = attrs.field(metadata={'_aapi_repr_': 'JobOwner'})


@attrs.define
class JobTandemTACLScript(JobTandem):

    _type: str = attrs.field(init=False, default='Job:Tandem:TACLScript', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Tandem:TACLScript'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    t_a_c_l_script: str = attrs.field(metadata={'_aapi_repr_': 'TACLScript'})
    volume: str = attrs.field(metadata={'_aapi_repr_': 'Volume'})


@attrs.define
class JobTandemProgram(JobTandem):

    _type: str = attrs.field(init=False, default='Job:Tandem:Program', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Tandem:Program'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    program: str = attrs.field(metadata={'_aapi_repr_': 'Program'})
    volume: str = attrs.field(metadata={'_aapi_repr_': 'Volume'})


@attrs.define
class JobTandemCommand(JobTandem):

    _type: str = attrs.field(init=False, default='Job:Tandem:Command', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Tandem:Command'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    command_line: str = attrs.field(metadata={'_aapi_repr_': 'CommandLine'})


@attrs.define
class JobTandemEmbeddedTACLScript(JobTandem):

    _type: str = attrs.field(init=False, default='Job:Tandem:EmbeddedTACLScript', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Tandem:EmbeddedTACLScript'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    t_a_c_l_script: str = attrs.field(metadata={'_aapi_repr_': 'TACLScript'})
    script: str = attrs.field(metadata={'_aapi_repr_': 'Script'})


@attrs.define
class JobTandemExternalProcess(JobTandem):

    @attrs.define
    class ExternalProcessId(AAPIObject):

        id: str = attrs.field(metadata={'_aapi_repr_': 'ID'})

    @attrs.define
    class ExternalCPUPIN(AAPIObject):

        c_p_u_id: str = attrs.field(metadata={'_aapi_repr_': 'CPUId'})

    _type: str = attrs.field(init=False, default='Job:Tandem:ExternalProcess', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:Tandem:ExternalProcess'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    external_process_id: ExternalProcessId = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ExternalProcessID'})
    external_c_p_u_p_i_n: ExternalCPUPIN = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ExternalCPUPIN'})


@attrs.define
class JobVMware(Job):

    _type: str = attrs.field(init=False, default='Job:VMware', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(
        metadata={'_aapi_repr_': 'ConnectionProfile'})


@attrs.define
class JobVMwareSnapshot(JobVMware):

    _type: str = attrs.field(init=False, default='Job:VMware:Snapshot', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Snapshot'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobVMwareSnapshotTake(JobVMwareSnapshot):

    _type: str = attrs.field(init=False, default='Job:VMware:Snapshot:Take', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Snapshot:Take'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    snapshot_name: str = attrs.field(metadata={'_aapi_repr_': 'SnapshotName'})


@attrs.define
class JobVMwareSnapshotRevert(JobVMwareSnapshot):

    _type: str = attrs.field(init=False, default='Job:VMware:Snapshot:Revert', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Snapshot:Revert'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobVMwareSnapshotRevertToCurrent(JobVMwareSnapshot):

    _type: str = attrs.field(init=False, default='Job:VMware:Snapshot:RevertToCurrent', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Snapshot:RevertToCurrent'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobVMwareSnapshotRemove(JobVMwareSnapshot):

    _type: str = attrs.field(init=False, default='Job:VMware:Snapshot:Remove', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Snapshot:Remove'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobVMwareSnapshotRemoveAll(JobVMwareSnapshot):

    _type: str = attrs.field(init=False, default='Job:VMware:Snapshot:RemoveAll', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Snapshot:RemoveAll'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobVMwarePower(JobVMware):

    _type: str = attrs.field(init=False, default='Job:VMware:Power', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Power'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    virtual_machine_name: str = attrs.field(
        metadata={'_aapi_repr_': 'VirtualMachineName'})


@attrs.define
class JobVMwarePowerOn(JobVMwarePower):

    _type: str = attrs.field(init=False, default='Job:VMware:Power:On', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Power:On'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobVMwarePowerOff(JobVMwarePower):

    _type: str = attrs.field(init=False, default='Job:VMware:Power:Off', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Power:Off'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobVMwarePowerSuspend(JobVMwarePower):

    _type: str = attrs.field(init=False, default='Job:VMware:Power:Suspend', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Power:Suspend'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobVMwarePowerReset(JobVMwarePower):

    _type: str = attrs.field(init=False, default='Job:VMware:Power:Reset', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Power:Reset'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobVMwarePowerReboot(JobVMwarePower):

    _type: str = attrs.field(init=False, default='Job:VMware:Power:Reboot', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Power:Reboot'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobVMwarePowerShutdown(JobVMwarePower):

    _type: str = attrs.field(init=False, default='Job:VMware:Power:Shutdown', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Power:Shutdown'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobVMwarePowerStandby(JobVMwarePower):

    _type: str = attrs.field(init=False, default='Job:VMware:Power:Standby', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Power:Standby'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobVMwareConfiguration(JobVMware):

    _type: str = attrs.field(init=False, default='Job:VMware:Configuration', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Configuration'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobVMwareConfigurationCloneVirtualMachine(JobVMwareConfiguration):

    _type: str = attrs.field(init=False, default='Job:VMware:Configuration:CloneVirtualMachine', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Configuration:CloneVirtualMachine'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    new_virtual_machine_name: str = attrs.field(
        metadata={'_aapi_repr_': 'NewVirtualMachineName'})
    target_host: str = attrs.field(metadata={'_aapi_repr_': 'TargetHost'})
    datastore: str = attrs.field(metadata={'_aapi_repr_': 'Datastore'})


@attrs.define
class JobVMwareConfigurationDeployTemplate(JobVMwareConfiguration):

    _type: str = attrs.field(init=False, default='Job:VMware:Configuration:DeployTemplate', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Configuration:DeployTemplate'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobVMwareConfigurationReconfigureVirtualMachine(JobVMwareConfiguration):

    _type: str = attrs.field(init=False, default='Job:VMware:Configuration:ReconfigureVirtualMachine', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Configuration:ReconfigureVirtualMachine'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    number_of_c_p_us: str = attrs.field(
        metadata={'_aapi_repr_': 'NumberOfCPUs'})


@attrs.define
class JobVMwareConfigurationMigrateVirtualMachine(JobVMwareConfiguration):

    _type: str = attrs.field(init=False, default='Job:VMware:Configuration:MigrateVirtualMachine', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:VMware:Configuration:MigrateVirtualMachine'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class JobWebServices(Job):

    class RequestType(enum.Enum):

        FreeText = "FreeText"
        Parameter = "Parameter"
        InputFile = "InputFile"

    _type: str = attrs.field(init=False, default='Job:WebServices', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:WebServices'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ConnectionProfile'})
    location: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Location'})
    service: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Service'})
    operation: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Operation'})
    request_type: RequestType = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'RequestType'})
    input_file: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'InputFile'})
    soap_header_file: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'SoapHeaderFile'})
    override_url_endpoint: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'OverrideUrlEndpoint'})
    override_content_type: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'OverrideContentType'})
    http_connection_timeout: str = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'HttpConnectionTimeout'})
    preemptive_http_authentication: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'PreemptiveHttpAuthentication'})
    exclude_job_output: bool = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'ExcludeJobOutput'})
    include_title_in_output: bool = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'IncludeTitleInOutput'})
    soap_request: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'SoapRequest'})
    input_parameters: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'InputParameters'})
    output_parameters: typing.List[typing.Dict[str, str]] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'OutputParameters'})


@attrs.define
class JobZOS(Job):

    @attrs.define
    class TaskInformation(AAPIObject):

        emergency_job: bool = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'EmergencyJob'})
        run_as_started_task: bool = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'RunAsStartedTask'})

    @attrs.define
    class OutputHandling(AAPIObject):

        class Operation(enum.Enum):

            Copy = "Copy"
            Delete = "Delete"
            Move = "Move"
            Release = "Release"
            ChangeClass = "ChangeClass"

        operation: Operation = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Operation'})
        destination: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Destination'})
        from_class: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'FromClass'})

    @attrs.define
    class History(AAPIObject):

        retention_days: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'RetentionDays'})
        retention_generations: str = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'RetentionGenerations'})

    @attrs.define
    class Archiving(AAPIObject):

        archive_sys_data: bool = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'ArchiveSysData'})
        days_to_retain_data: int = attrs.field(kw_only=True, default=None, metadata={
                                               '_aapi_repr_': 'DaysToRetainData'})
        job_runs_to_retain_data: int = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'JobRunsToRetainData'})
        auto_archive: bool = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'AutoArchive'})

    @attrs.define
    class Scheduling(AAPIObject):

        partition_dataset: str = attrs.field(kw_only=True, default=None, metadata={
                                             '_aapi_repr_': 'PartitionDataset'})
        minimum_number_of_tracks: int = attrs.field(kw_only=True, default=None, metadata={
                                                    '_aapi_repr_': 'MinimumNumberOfTracks'})

    @attrs.define
    class MustEnd(AAPIObject):

        hours: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Hours'})
        minutes: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Minutes'})
        days: int = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Days'})

    class PreventNCT2(enum.Enum):

        Yes = "Yes"
        No = "No"
        Flush = "Flush"
        List = "List"

    class Sac(enum.Enum):

        Default = "Default"
        Prev = "Prev"
        Next = "Next"

    _type: str = attrs.field(init=False, default='Job:zOS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:zOS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    system_affinity: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'SystemAffinity'})
    scheduling_environment: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'SchedulingEnvironment'})
    request_n_j_e_node: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'RequestNJENode'})
    task_information: TaskInformation = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'TaskInformation'})
    control_d_category: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ControlDCategory'})
    prevent_n_c_t2: PreventNCT2 = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'PreventNCT2'})
    statistics_calendar: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'StatisticsCalendar'})
    sac: Sac = attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'SAC'})
    output_handling: OutputHandling = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'OutputHandling'})
    history: History = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'History'})
    archiving: Archiving = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Archiving'})
    scheduling: Scheduling = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Scheduling'})
    must_end: MustEnd = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'MustEnd'})
    if_collection_list: typing.List[IfCollection] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    event_list: typing.List[Event] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    resource_list: typing.List[Resource] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    wait_for_events: typing.List[WaitForEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    events_to_add: typing.List[AddEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    events_to_delete: typing.List[DeleteEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    notify_list: typing.List[Notify] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    job_tag_list: typing.List[JobTag] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    action_capture_output_list: typing.List[ActionCaptureOutput] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    step_range_list: typing.List[StepRange] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
# support backward compatibility
    condition_list: typing.List[Condition] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    wait_for_events_list: typing.List[WaitForEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    add_events_list: typing.List[AddEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    delete_events_list: typing.List[DeleteEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})


@attrs.define
class JobZOSInStreamJCL(JobZOS):

    _type: str = attrs.field(init=False, default='Job:zOS:InStreamJCL', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:zOS:InStreamJCL'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    member_library: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'MemberLibrary'})
    member: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Member'})
    jcl: str = attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'JCL'})


@attrs.define
class JobZOSMember(JobZOS):

    _type: str = attrs.field(init=False, default='Job:zOS:Member', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:zOS:Member'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    member_library: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'MemberLibrary'})
    member: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Member'})
