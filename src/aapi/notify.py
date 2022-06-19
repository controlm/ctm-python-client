
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class Notify(AAPIObject):

    class Destination(enum.Enum):

        Alerts = "Alerts"
        JobLog = "JobLog"
        Console = "Console"

    class Urgency(enum.Enum):

        Urgent = "Urgent"
        Regular = "Regular"
        VeryUrgent = "VeryUrgent"

    _type: str = attrs.field(init=False, default='Notify', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Notify'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})

    message: str = attrs.field(metadata={'_aapi_repr_': 'Message'})
    destination: Destination = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Destination'})
    urgency: Urgency = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Urgency'})


@attrs.define
class NotifyDoesNotStart(Notify):

    _type: str = attrs.field(init=False, default='Notify:DoesNotStart', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Notify:DoesNotStart'})
    by: str = attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'By'})
    days: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Days'})


@attrs.define
class NotifyDoesNotEnd(Notify):

    _type: str = attrs.field(init=False, default='Notify:DoesNotEnd', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Notify:DoesNotEnd'})
    by: str = attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'By'})


@attrs.define
class NotifyNotOK(Notify):

    _type: str = attrs.field(init=False, default='Notify:NotOK', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Notify:NotOK'})


@attrs.define
class NotifyOK(Notify):

    _type: str = attrs.field(init=False, default='Notify:OK', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Notify:OK'})


@attrs.define
class NotifyRerun(Notify):

    _type: str = attrs.field(init=False, default='Notify:Rerun', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Notify:Rerun'})


@attrs.define
class NotifyExecutionTime(Notify):

    class Criteria(enum.Enum):

        LessThan = "LessThan"
        GreaterThan = "GreaterThan"
        LessThanAverage = "LessThanAverage"
        GreaterThanAverage = "GreaterThanAverage"

    _type: str = attrs.field(init=False, default='Notify:ExecutionTime', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Notify:ExecutionTime'})
    value: str = attrs.field(metadata={'_aapi_repr_': 'Value'})
    criteria: Criteria = attrs.field(metadata={'_aapi_repr_': 'Criteria'})


@attrs.define
class NotifyLateCyclicSubmit(Notify):

    _type: str = attrs.field(init=False, default='Notify:LateCyclicSubmit', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Notify:LateCyclicSubmit'})
    by: str = attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'By'})
