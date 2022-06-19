
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class Condition(AAPIObject):

    class Date(enum.Enum):

        NoDate = "NoDate"
        AnyDate = "AnyDate"
        OrderDate = "OrderDate"
        PreviousOrderDate = "PreviousOrderDate"
        NextOrderDate = "NextOrderDate"

    _type: str = attrs.field(init=False, default='Condition', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Condition'})
    event: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Event'})
    date: Date = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'Date'})


@attrs.define
class ConditionIn(Condition):

    _type: str = attrs.field(init=False, default='Condition:In', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Condition:In'})


@attrs.define
class ConditionOut(Condition):

    _type: str = attrs.field(init=False, default='Condition:Out', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Condition:Out'})


@attrs.define
class ConditionOutDelete(ConditionOut):

    _type: str = attrs.field(init=False, default='Condition:Out:Delete', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Condition:Out:Delete'})


@attrs.define
class ConditionOutAdd(ConditionOut):

    _type: str = attrs.field(init=False, default='Condition:Out:Add', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Condition:Out:Add'})
