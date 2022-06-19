
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *

@attrs.define
class Calendar(AAPIObject):

    _type: str = attrs.field(init=False, default='Calendar', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Calendar'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})



@attrs.define
class CalendarRuleBased(Calendar):

    @attrs.define
    class When(AAPIObject):

        @attrs.define
        class ConfirmationCalendars(AAPIObject):

            class ExceptionPolicy(enum.Enum):

                DoNotOrder = "DoNotOrder"
                OrderOnNextConfirmedDay = "OrderOnNextConfirmedDay"
                OrderOnPreviousConfirmedDay = "OrderOnPreviousConfirmedDay"
                OrderAnyway = "OrderAnyway"

            calendar: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Calendar'})
            shift_by: int = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ShiftBy'})
            exception_policy: ExceptionPolicy = attrs.field(
                kw_only=True, default=None, metadata={'_aapi_repr_': 'ExceptionPolicy'})

        class DaysRelation(enum.Enum):

            AND = "AND"
            OR = "OR"

        class DaysKeepActive(enum.Enum):

            Forever = "Forever"

        specific_dates: typing.List[str] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'SpecificDates'})
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
        start_date: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'StartDate'})
        end_date: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'EndDate'})
        active_period: bool = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ActivePeriod'})
        days_keep_active: DaysKeepActive = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'DaysKeepActive'})
        confirmation_calendars: ConfirmationCalendars = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'ConfirmationCalendars'})

    _type: str = attrs.field(init=False, default='Calendar:RuleBased', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Calendar:RuleBased'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    when: When = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'When'})



@attrs.define
class CalendarRegular(Calendar):

    @attrs.define
    class When(AAPIObject):

        years: typing.List[Year] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'Years'})

    class Server(enum.Enum):

        Global = "Global"

    _type: str = attrs.field(init=False, default='Calendar:Regular', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Calendar:Regular'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    when: When = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'When'})
    server: Server = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Server'})
    alias: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Alias'})
    description: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Description'})


@attrs.define
class CalendarPeriodic(Calendar):

    @attrs.define
    class When(AAPIObject):

        periods: typing.List[Period] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'Periods'})

    class Server(enum.Enum):

        Global = "Global"

    _type: str = attrs.field(init=False, default='Calendar:Periodic', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Calendar:Periodic'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    when: When = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'When'})
    server: Server = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Server'})
    alias: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Alias'})
    description: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Description'})


@attrs.define
class CalendarRuleBasedCalendar(Calendar):

    @attrs.define
    class When(AAPIObject):

        @attrs.define
        class ConfirmationCalendars(AAPIObject):

            class ExceptionPolicy(enum.Enum):

                DoNotOrder = "DoNotOrder"
                OrderOnNextConfirmedDay = "OrderOnNextConfirmedDay"
                OrderOnPreviousConfirmedDay = "OrderOnPreviousConfirmedDay"
                OrderAnyway = "OrderAnyway"

            calendar: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'Calendar'})
            shift_by: int = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ShiftBy'})
            exception_policy: ExceptionPolicy = attrs.field(
                kw_only=True, default=None, metadata={'_aapi_repr_': 'ExceptionPolicy'})

        class DaysRelation(enum.Enum):

            AND = "AND"
            OR = "OR"

        class DaysKeepActive(enum.Enum):

            Forever = "Forever"

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
        start_date: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'StartDate'})
        end_date: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'EndDate'})
        active_period: bool = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ActivePeriod'})
        specific_dates: typing.List[str] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'SpecificDates'})
        days_keep_active: DaysKeepActive = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'DaysKeepActive'})
        confirmation_calendars: ConfirmationCalendars = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'ConfirmationCalendars'})

    class Server(enum.Enum):

        Global = "Global"

    _type: str = attrs.field(init=False, default='Calendar:RuleBasedCalendar', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Calendar:RuleBasedCalendar'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    when: When = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'When'})
    server: Server = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Server'})
    alias: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Alias'})
