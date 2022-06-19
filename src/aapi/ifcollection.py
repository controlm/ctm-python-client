
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class IfCollection(AAPIObject):

    _type: str = attrs.field(init=False, default='IfCollection', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'IfCollection'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    ifs: typing.List[IfZOS] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Ifs'})
    do_list: typing.List[Do] = attrs.field(kw_only=True, factory=list, metadata={
                                           '_abstract_aapi_container_': True})


@attrs.define
class IfCollectionZOS(IfCollection):

    _type: str = attrs.field(init=False, default='IfCollection:zOS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'IfCollection:zOS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
