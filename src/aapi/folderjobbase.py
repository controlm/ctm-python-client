
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class FolderJobBase(AAPIObject):

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

    class Priority(enum.Enum):

        Very_High = "Very_High"
        High = "High"
        Medium = "Medium"
        Low = "Low"
        Very_Low = "Very_Low"

    _type: str = attrs.field(init=False, default='FolderJobBase', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'FolderJobBase'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    application: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Application'})
    sub_application: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'SubApplication'})
    description: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Description'})
    documentation_file: DocumentationFile = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DocumentationFile'})
    documentation_url: DocumentationUrl = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DocumentationUrl'})
    variables: typing.List[typing.Dict[str,str]] = attrs.field(
        kw_only=True, factory=list, metadata={'_aapi_repr_': 'Variables'})
    created_by: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'CreatedBy'})
    confirm: bool = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Confirm'})
    priority: Priority = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Priority'})


@attrs.define
class FolderJobBaseSmart(FolderJobBase):

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
        from_: From = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'From'})
        every: int = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Every'})
        units: Units = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Units'})

    _type: str = attrs.field(init=False, default='FolderJobBase:Smart', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'FolderJobBase:Smart'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    rerun_intervals: RerunIntervals = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'RerunIntervals'})
    rerun_specific_times: RerunSpecificTimes = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'RerunSpecificTimes'})
    rerun: Rerun = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Rerun'})
    tag_list: typing.List[Tag] = attrs.field(kw_only=True, factory=list, metadata={
                                             '_abstract_aapi_container_': True})
    tag_folder_list: typing.List[TagFolder] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})


@attrs.define
class SubFolder(FolderJobBase, AAPIJob):

    @attrs.define
    class PathElement(AAPIObject):

        folder: str = attrs.field(metadata={'_aapi_repr_': 'Folder'})
        server: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Server'})
        library: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Library'})

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

        class DaysRelation(enum.Enum):

            AND = "AND"
            OR = "OR"

        specific_dates: typing.List[str] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'SpecificDates'})
        from_time: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'FromTime'})
        days: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Days'})
        to_time: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'ToTime'})
        days_relation: DaysRelation = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'DaysRelation'})
        rule_based_calendars: RuleBasedCalendars = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'RuleBasedCalendars'})

    class ActiveRetentionPolicy(enum.Enum):

        KeepAll = "KeepAll"
        CleanEndedOK = "CleanEndedOK"

    class DaysKeepActive(enum.Enum):

        Forever = "Forever"

    class AdjustEvents(enum.Enum):

        Bridge = "Bridge"
        Dummy = "Dummy"
        Y = "Y"
        N = "N"

    _type: str = attrs.field(init=False, default='SubFolder', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'SubFolder'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    path_element: PathElement = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'PathElement'})
    active_retention_policy: ActiveRetentionPolicy = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ActiveRetentionPolicy'})
    days_keep_active: DaysKeepActive = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DaysKeepActive'})
    reference_path: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'ReferencePath'})
    run_as: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'RunAs'})
    time_zone: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'TimeZone'})
    adjust_events: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'AdjustEvents'})
    when: When = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'When'})
    job_list: typing.List[Job] = attrs.field(kw_only=True, factory=list, metadata={
                                             '_abstract_aapi_container_': True})
    sub_folder_list: typing.List[SubFolder] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    flow_list: typing.List[Flow] = attrs.field(kw_only=True, factory=list, metadata={
                                               '_abstract_aapi_container_': True})
    job_tag_list: typing.List[JobTag] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    resource_lock_list: typing.List[ResourceLock] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
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
# support backward compatibility
    wait_for_events_list: typing.List[WaitForEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    add_events_list: typing.List[AddEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
    delete_events_list: typing.List[DeleteEvents] = attrs.field(
        kw_only=True, factory=list, metadata={'_abstract_aapi_container_': True})
