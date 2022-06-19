
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class AddEvents(AAPIObject):

    _type: str = attrs.field(init=False, default='AddEvents', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'AddEvents'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    events: typing.List[ConditionOutAdd] = attrs.field(
        metadata={'_aapi_repr_': 'Events'})
