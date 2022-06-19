
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class Flow_(AAPIObject):

    _type: str = attrs.field(init=False, default='Flow', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Flow'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    sequence: typing.List[str] = attrs.field(
        metadata={'_aapi_repr_': 'Sequence'})
