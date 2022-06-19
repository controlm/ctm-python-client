
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class ItemInfo(AAPIObject):

    _type: str = attrs.field(init=False, default='ItemInfo', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'ItemInfo'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
