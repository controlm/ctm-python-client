
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class PossibleOptions(AAPIObject):

    _type: str = attrs.field(init=False, default='PossibleOptions', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'PossibleOptions'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
