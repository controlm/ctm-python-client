
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class SiteStandardOperatorValueOptions(AAPIObject):

    class Operator(enum.Enum):

        Equals = "Equals"
        DoesNotEqual = "DoesNotEqual"
        GreaterThan = "GreaterThan"
        LessThan = "LessThan"
        Even = "Even"
        Odd = "Odd"

    _type: str = attrs.field(init=False, default='SiteStandardOperatorValueOptions', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'SiteStandardOperatorValueOptions'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    operator: Operator = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Operator'})
    value: int = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Value'})
