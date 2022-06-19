
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class Year(AAPIObject):

    _type: str = attrs.field(init=False, default='Year', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Year'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    year: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Year'})
    jan: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'JAN'})
    feb: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'FEB'})
    mar: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'MAR'})
    apr: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'APR'})
    may: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'MAY'})
    jun: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'JUN'})
    jul: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'JUL'})
    aug: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AUG'})
    sep: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'SEP'})
    oct: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'OCT'})
    nov: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'NOV'})
    dec: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'DEC'})
    description: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Description'})
