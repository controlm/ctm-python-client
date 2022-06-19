
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class CalendarKey(AAPIObject):

    _type: str = attrs.field(init=False, default='CalendarKey', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'CalendarKey'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class CalendarKeyRegular(CalendarKey):

    _type: str = attrs.field(init=False, default='CalendarKey:Regular', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'CalendarKey:Regular'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class CalendarKeyPeriodic(CalendarKey):

    _type: str = attrs.field(init=False, default='CalendarKey:Periodic', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'CalendarKey:Periodic'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class CalendarKeyRuleBased(CalendarKey):

    _type: str = attrs.field(init=False, default='CalendarKey:RuleBased', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'CalendarKey:RuleBased'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
