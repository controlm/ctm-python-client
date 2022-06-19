
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class CalendarFields(AAPIObject):

    _type: str = attrs.field(init=False, default='CalendarFields', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'CalendarFields'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class CalendarFieldsRegular(CalendarFields):

    _type: str = attrs.field(init=False, default='CalendarFields:Regular', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'CalendarFields:Regular'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class CalendarFieldsPeriodic(CalendarFields):

    _type: str = attrs.field(init=False, default='CalendarFields:Periodic', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'CalendarFields:Periodic'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class CalendarFieldsRuleBased(CalendarFields):

    _type: str = attrs.field(init=False, default='CalendarFields:RuleBased', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'CalendarFields:RuleBased'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
