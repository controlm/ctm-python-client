
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class RunningJobs(AAPIObject):

    @attrs.define
    class PeriodicDays(AAPIObject):

        days_of_week: typing.List[str] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'DaysOfWeek'})

    @attrs.define
    class RangeDates(AAPIObject):

        from_date: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'FromDate'})
        to_date: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'ToDate'})

    @attrs.define
    class RangeDatesWithTimes(AAPIObject):

        from_date: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'FromDate'})
        to_date: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'ToDate'})
        from_time: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'FromTime'})
        to_time: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'ToTime'})

    @attrs.define
    class WeekDaysRange(AAPIObject):

        class FromDay(enum.Enum):

            Sun = "Sun"
            Mon = "Mon"
            Tue = "Tue"
            Wed = "Wed"
            Thu = "Thu"
            Fri = "Fri"
            Sat = "Sat"

        class ToDay(enum.Enum):

            Sun = "Sun"
            Mon = "Mon"
            Tue = "Tue"
            Wed = "Wed"
            Thu = "Thu"
            Fri = "Fri"
            Sat = "Sat"

        from_day: FromDay = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'FromDay'})
        to_day: ToDay = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'ToDay'})
        from_time: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'FromTime'})
        to_time: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'ToTime'})

    @attrs.define
    class DatesList(AAPIObject):

        dates: typing.List[str] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'Dates'})

    @attrs.define
    class Time(AAPIObject):

        class TimeType(enum.Enum):

            None_ = "None_"
            AllHours = "AllHours"
            BetweenHours = "BetweenHours"

        time_type: TimeType = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'TimeType'})

    @attrs.define
    class SpecificTime(AAPIObject):

        from_time: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'FromTime'})
        to_time: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'ToTime'})

    class Server(enum.Enum):

        Global = "Global"

    _type: str = attrs.field(init=False, default='RunningJobs', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'RunningJobs'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    quantity: int = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Quantity'})
    server: Server = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Server'})
    periodic_days: PeriodicDays = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'PeriodicDays'})
    range_dates: RangeDates = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'RangeDates'})
    range_dates_with_times: RangeDatesWithTimes = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'RangeDatesWithTimes'})
    week_days_range: WeekDaysRange = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'WeekDaysRange'})
    dates_list: DatesList = attrs.field(kw_only=True, default=None, metadata={
                                        '_abstract_aapi_container_': True})
    time: Time = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'Time'})
    specific_time: SpecificTime = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'SpecificTime'})
