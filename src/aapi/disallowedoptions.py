
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class DisallowedOptions(AAPIObject):

    _type: str = attrs.field(init=False, default='DisallowedOptions', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'DisallowedOptions'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
