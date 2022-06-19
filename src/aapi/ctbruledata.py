
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class ActionControlMAnalyzerRule(AAPIObject):

    _type: str = attrs.field(init=False, default='Action:ControlMAnalyzerRule', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Action:ControlMAnalyzerRule'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    name: str = attrs.field(metadata={'_aapi_repr_': 'Name'})
    arg: str = attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Arg'})
