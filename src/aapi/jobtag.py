
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class JobTag(AAPIObject):

    class TagName(enum.Enum):

        USE_PARENT = "USE_PARENT"

    _type: str = attrs.field(init=False, default='JobTag', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'JobTag'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    tag_name: TagName = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'TagName'})
