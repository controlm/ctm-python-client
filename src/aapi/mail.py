
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class ActionMail(AAPIObject):

    class Urgency(enum.Enum):

        Urgent = "Urgent"
        Regular = "Regular"
        VeryUrgent = "VeryUrgent"

    _type: str = attrs.field(init=False, default='Action:Mail', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Action:Mail'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    urgency: Urgency = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Urgency'})
    message: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Message'})
    to: str = attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'To'})
    subject: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Subject'})
    cc: str = attrs.field(kw_only=True, default=None,
                          metadata={'_aapi_repr_': 'CC'})
    attach_output: bool = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'AttachOutput'})
