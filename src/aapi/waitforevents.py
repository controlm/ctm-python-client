
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class WaitForEvents(AAPIObject):

    _type: str = attrs.field(init=False, default='WaitForEvents', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'WaitForEvents'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    events: typing.List[ConditionIn] = attrs.field(
        metadata={'_aapi_repr_': 'Events'})
