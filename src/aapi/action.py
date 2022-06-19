
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class Action(AAPIObject):
    _type: str = attrs.field(init=False, default='Action', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Action'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    action_field: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'ActionField'})


@attrs.define
class ActionRerun(Action):

    _type: str = attrs.field(init=False, default='Action:Rerun', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Action:Rerun'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class ActionSetToOK(Action):

    _type: str = attrs.field(init=False, default='Action:SetToOK', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Action:SetToOK'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class ActionSetToNotOK(Action):

    _type: str = attrs.field(init=False, default='Action:SetToNotOK', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Action:SetToNotOK'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class ActionStopCyclicRun(Action):

    _type: str = attrs.field(init=False, default='Action:StopCyclicRun', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Action:StopCyclicRun'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
