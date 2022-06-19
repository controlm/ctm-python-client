
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class SiteStandardPolicy(AAPIObject):

    @attrs.define
    class ApplyOn(AAPIObject):

        server: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Server'})
        folder: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Folder'})

    class Status(enum.Enum):

        Active = "Active"
        Not_Active = "Not_Active"

    class ErrorLevel(enum.Enum):

        Warning = "Warning"
        Error = "Error"
        Default = "Default"

    _type: str = attrs.field(init=False, default='SiteStandardPolicy', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'SiteStandardPolicy'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    description: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Description'})
    site_standard: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'SiteStandard'})
    business_fields: typing.List[BusinessField] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'BusinessFields'})
    status: Status = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Status'})
    error_level: ErrorLevel = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'ErrorLevel'})
    apply_on: ApplyOn = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'ApplyOn'})
