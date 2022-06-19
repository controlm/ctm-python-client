
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class ActionNotify(AAPIObject):

    class Destination(enum.Enum):

        Alerts = "Alerts"
        JobLog = "JobLog"
        Console = "Console"

    class Urgency(enum.Enum):

        Urgent = "Urgent"
        Regular = "Regular"
        VeryUrgent = "VeryUrgent"

    _type: str = attrs.field(init=False, default='Action:Notify', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Action:Notify'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    destination: Destination = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Destination'})
    message: str = attrs.field(metadata={'_aapi_repr_': 'Message'})
    urgency: Urgency = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Urgency'})
