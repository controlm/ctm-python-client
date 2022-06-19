
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class ActionSet(AAPIObject):

    _type: str = attrs.field(init=False, default='Action:Set', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Action:Set'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    variable: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Variable'})
    value: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Value'})
