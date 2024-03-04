
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class Event(AAPIObject):

    class Date(enum.Enum):

        NoDate = "NoDate"
        AnyDate = "AnyDate"
        OrderDate = "OrderDate"
        PreviousOrderDate = "PreviousOrderDate"
        NextOrderDate = "NextOrderDate"

    _type: str = attrs.field(init=False, default='Event', metadata={
                            '_aapi_repr_': 'Type', '_type_aapi_': 'Event'})
    object_name: str = attrs.field(init=False, default='Event', metadata={
                            '_aapi_name_': True})
    event: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Event'})
    date: Date = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'Date'})


@attrs.define
class EventAdd(Event):

    _type: str = attrs.field(init=False, default='Event:Add', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Event:Add'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class EventDelete(Event):

    _type: str = attrs.field(init=False, default='Event:Delete', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Event:Delete'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})

@attrs.define
class EventIn(Event):

    _type: str = attrs.field(init=False, default='Event:In', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Event:In'})


@attrs.define
class EventOut(Event):

    _type: str = attrs.field(init=False, default='Event:Out', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Event:Out'})


@attrs.define
class EventOutDelete(EventOut):

    _type: str = attrs.field(init=False, default='Event:Out:Delete', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Event:Out:Delete'})


@attrs.define
class EventOutAdd(EventOut):

    _type: str = attrs.field(init=False, default='Event:Out:Add', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Event:Out:Add'})
