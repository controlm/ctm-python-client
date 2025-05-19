
from __future__ import annotations
import attrs
from aapi.bases import AAPIObject

@attrs.define
class Date(AAPIObject):

    _type: str = attrs.field(init=False, default='Date', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Date'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
