
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class SimpleFolder(AAPIObject):

    class OrderMethod(enum.Enum):

        Automatic = "Automatic"
        Manual = "Manual"

    _type: str = attrs.field(init=False, default='SimpleFolder', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'SimpleFolder'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    controlm_server: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'ControlmServer'})
    order_method: OrderMethod = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'OrderMethod'})
    folder_library: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'FolderLibrary'})
    site_standard: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'SiteStandard'})
    business_fields: typing.List[typing.Dict[str,str]] = attrs.field(
        kw_only=True, metadata={'_aapi_repr_': 'BusinessFields'}, factory=list)
    job_list: typing.List[Job] = attrs.field(kw_only=True, factory=list, metadata={
                                             '_abstract_aapi_container_': True})
    flow_list: typing.List[Flow] = attrs.field(kw_only=True, factory=list, metadata={
                                               '_abstract_aapi_container_': True})
    folder_client_data_list: typing.List[FolderClientData] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})


@attrs.define
class Folder(SimpleFolder, AAPIJob):

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
    class MustEnd(AAPIObject):

        hours: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Hours'})
        minutes: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Minutes'})
        days: int = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Days'})

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

            included: typing.List[TagGlobal] = attrs.field(
                kw_only=True, default=None, metadata={'_aapi_repr_': 'Included'})
            excluded: typing.List[TagGlobal] = attrs.field(
                kw_only=True, default=None, metadata={'_aapi_repr_': 'Excluded'})
            calendar_rule_based_list: typing.List[CalendarRuleBased] = attrs.field(
                kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})

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

    class Priority(enum.Enum):

        Very_High = "Very_High"
        High = "High"
        Medium = "Medium"
        Low = "Low"
        Very_Low = "Very_Low"

    class DaysKeepActive(enum.Enum):

        Forever = "Forever"

    class ActiveRetentionPolicy(enum.Enum):

        KeepAll = "KeepAll"
        CleanEndedOK = "CleanEndedOK"

    class Sac(enum.Enum):

        Default = "Default"
        Next = "Next"
        Prev = "Prev"
        SmartFolderPrev = "SmartFolderPrev"
        SmartFolderNext = "SmartFolderNext"

    class AdjustEvents(enum.Enum):

        Bridge = "Bridge"
        Dummy = "Dummy"
        Y = "Y"
        N = "N"

    _type: str = attrs.field(init=False, default='Folder', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Folder'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    priority: Priority = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Priority'})
    application: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Application'})
    created_by: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'CreatedBy'})
    confirm: bool = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Confirm'})
    days_keep_active: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DaysKeepActive'})
    description: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Description'})
    days_keep_active_if_not_ok: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DaysKeepActiveIfNotOk'})
    active_retention_policy: ActiveRetentionPolicy = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ActiveRetentionPolicy'})
    run_as: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'RunAs'})
    documentation_file: DocumentationFile = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DocumentationFile'})
    documentation_url: DocumentationUrl = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DocumentationUrl'})
    member_library: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'MemberLibrary'})
    statistics_calendar: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'StatisticsCalendar'})
    sac: Sac = attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'SAC'})
    must_end: MustEnd = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'MustEnd'})
    rerun_limit: RerunLimit = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'RerunLimit'})
    rerun: Rerun = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Rerun'})
    rerun_intervals: RerunIntervals = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'RerunIntervals'})
    rerun_specific_times: RerunSpecificTimes = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'RerunSpecificTimes'})
    sub_application: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'SubApplication'})
    time_zone: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'TimeZone'})
    variables: typing.List[typing.Dict[str,str]] = attrs.field(
        kw_only=True, factory=list, metadata={'_aapi_repr_': 'Variables'})
    adjust_events: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AdjustEvents'})
    when: When = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'When'})
    if_list: typing.List[IfBase] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    wait_for_events: typing.List[WaitForEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    events_to_add: typing.List[AddEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    events_to_delete: typing.List[DeleteEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    notify_list: typing.List[Notify] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    resource_lock_list: typing.List[ResourceLock] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    sub_folder_list: typing.List[SubFolder] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})

	# support backward compatibility
    wait_for_events_list: typing.List[WaitForEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    add_events_list: typing.List[AddEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    delete_events_list: typing.List[DeleteEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    