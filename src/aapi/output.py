
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class ActionOutput(AAPIObject):

    class Operation(enum.Enum):

        Copy = "Copy"
        Move = "Move"
        Print = "Print"
        Delete = "Delete"

    _type: str = attrs.field(init=False, default='Action:Output', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Action:Output'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    operation: Operation = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Operation'})
    destination: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Destination'})
