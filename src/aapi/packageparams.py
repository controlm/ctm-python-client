
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class PackageParams(AAPIObject):

    # _type: str = attrs.field(init=False, default='PackageParams', metadata={
    #                          '_aapi_repr_': 'Type', '_type_aapi_': 'PackageParams'})
    name: str = attrs.field(metadata={'_aapi_repr_': 'Name'})
    value: str = attrs.field(metadata={'_aapi_repr_': 'Value'})
