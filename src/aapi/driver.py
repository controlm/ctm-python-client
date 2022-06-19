
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class DriverJdbcDatabase(AAPIObject):

    _type: str = attrs.field(init=False, default='Driver:Jdbc:Database', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Driver:Jdbc:Database'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    target_ctm: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'TargetCTM'})
    target_agent: str = attrs.field(metadata={'_aapi_repr_': 'TargetAgent'})
    string_template: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'StringTemplate'})
    driver_jars_folder: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'DriverJarsFolder'})
    class_name: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'ClassName'})
    line_comment: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'LineComment'})
    statement_separator: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'StatementSeparator'})
