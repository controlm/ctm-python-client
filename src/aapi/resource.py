
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class Resource(AAPIObject):

    _type: str = attrs.field(init=False, default='Resource', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Resource'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class ResourcePool(Resource):

    class IfFail(enum.Enum):

        Keep = "Keep"
        Release = "Release"

    class IfOk(enum.Enum):

        Discard = "Discard"
        Release = "Release"

    _type: str = attrs.field(init=False, default='Resource:Pool', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Resource:Pool'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    quantity: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Quantity'})
    if_fail: IfFail = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IfFail'})
    if_ok: IfOk = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'IfOk'})


@attrs.define
class ResourceLock(Resource):

    class LockType(enum.Enum):

        Shared = "Shared"
        Exclusive = "Exclusive"

    class IfFail(enum.Enum):

        Keep = "Keep"
        Release = "Release"

    _type: str = attrs.field(init=False, default='Resource:Lock', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Resource:Lock'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    lock_type: LockType = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'LockType'})
    if_fail: IfFail = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'IfFail'})
