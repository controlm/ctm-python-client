
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class SiteStandard(AAPIObject):

    _type: str = attrs.field(init=False, default='SiteStandard', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'SiteStandard'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    description: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Description'})
    event_format: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'EventFormat'})
    rules: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Rules'})
    internal_rules: typing.List[InternalRule] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'InternalRules'})
    business_parameters: typing.List[BusinessParameter] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'BusinessParameters'})
