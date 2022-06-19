
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class WpPeriod(AAPIObject):

    _type: str = attrs.field(init=False, default='WPPeriod', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'WPPeriod'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
