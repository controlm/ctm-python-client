
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class IfZOS(If):

    _type: str = attrs.field(init=False, default='If:zOS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'If:zOS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class IfZOSAnyProgramStep(IfZOS):

    _type: str = attrs.field(init=False, default='If:zOS:AnyProgramStep', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'If:zOS:AnyProgramStep'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    procedure: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Procedure'})
    return_codes: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ReturnCodes'})


@attrs.define
class IfZOSEveryProgramStep(IfZOS):

    _type: str = attrs.field(init=False, default='If:zOS:EveryProgramStep', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'If:zOS:EveryProgramStep'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    procedure: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Procedure'})
    return_codes: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ReturnCodes'})


@attrs.define
class IfZOSSpecificProgramStep(IfZOS):

    _type: str = attrs.field(init=False, default='If:zOS:SpecificProgramStep', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'If:zOS:SpecificProgramStep'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    program: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Program'})
    procedure: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Procedure'})
    return_codes: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ReturnCodes'})


@attrs.define
class IfZOSSpecificRangeName(IfZOS):

    _type: str = attrs.field(init=False, default='If:zOS:SpecificRangeName', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'If:zOS:SpecificRangeName'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    program: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'Program'})
    procedure: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Procedure'})
    return_codes: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ReturnCodes'})


@attrs.define
class IfZOSJOBRCCodes(IfZOS):

    _type: str = attrs.field(init=False, default='If:zOS:JOBRCCodes', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'If:zOS:JOBRCCodes'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    procedure: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Procedure'})
    return_codes: typing.List[str] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ReturnCodes'})


@attrs.define
class IfZOSOutputPattern(IfZOS):

    _type: str = attrs.field(init=False, default='If:zOS:OutputPattern', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'If:zOS:OutputPattern'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    output_pattern: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'OutputPattern'})
    from_column: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'FromColumn'})
    to_column: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'ToColumn'})


@attrs.define
class IfZOSNumberOfFailures(IfZOS):

    class NumberOfFailures(enum.Enum):

        var_ = "var_"

    _type: str = attrs.field(init=False, default='If:zOS:NumberOfFailures', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'If:zOS:NumberOfFailures'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    number_of_failures: NumberOfFailures = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'NumberOfFailures'})
