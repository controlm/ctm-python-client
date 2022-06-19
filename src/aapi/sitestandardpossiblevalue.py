
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class SiteStandardPossibleValue(AAPIObject):

    _type: str = attrs.field(init=False, default='SiteStandardPossibleValue', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'SiteStandardPossibleValue'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    value: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Value'})
    description: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Description'})
