
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class ActionRemedy(AAPIObject):

    class Urgency(enum.Enum):

        Low = "Low"
        Medium = "Medium"
        High = "High"
        Urgent = "Urgent"

    _type: str = attrs.field(init=False, default='Action:Remedy', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Action:Remedy'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    urgency: Urgency = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Urgency'})
    message: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Message'})
    summary: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Summary'})
