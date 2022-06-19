
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class SiteStandardRestriction(AAPIObject):

    _type: str = attrs.field(init=False, default='SiteStandardRestriction', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'SiteStandardRestriction'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class SiteStandardRestrictionNumeric(SiteStandardRestriction):

    _type: str = attrs.field(init=False, default='SiteStandardRestriction:Numeric', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'SiteStandardRestriction:Numeric'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class SiteStandardRestrictionText(SiteStandardRestriction):

    _type: str = attrs.field(init=False, default='SiteStandardRestriction:Text', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'SiteStandardRestriction:Text'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class SiteStandardRestrictionEnum(SiteStandardRestriction):

    _type: str = attrs.field(init=False, default='SiteStandardRestriction:Enum', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'SiteStandardRestriction:Enum'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class SiteStandardRestrictionOperatorValue(SiteStandardRestriction):

    _type: str = attrs.field(init=False, default='SiteStandardRestriction:OperatorValue', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'SiteStandardRestriction:OperatorValue'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    values: typing.List[SiteStandardOperatorValueOptions] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Values'})
