
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class HostMapping(AAPIObject):

    class Server(enum.Enum):

        Global = "Global"

    _type: str = attrs.field(init=False, default='HostMapping', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'HostMapping'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    host: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Host'})
    map_to: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'MapTo'})
    server: Server = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Server'})
