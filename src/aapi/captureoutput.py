
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class ActionCaptureOutput(AAPIObject):

    @attrs.define
    class ForwardBy(AAPIObject):

        class ColumnsOption(enum.Enum):

            Words = "Words"
            Characters = "Characters"

        class Delimiter(enum.Enum):

            WhiteSpace = "WhiteSpace"
            Space = "Space"
            Tab = "Tab"
            var_ = "var_"

        lines: int = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Lines'})
        columns: int = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Columns'})
        columns_option: ColumnsOption = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'ColumnsOption'})
        delimiter: Delimiter = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'Delimiter'})

    class VariableName(enum.Enum):

        var_ = "var_"

    class Capture(enum.Enum):

        UpToEndOfLine = "UpToEndOfLine"
        var_ = "var_"

    _type: str = attrs.field(init=False, default='Action:CaptureOutput', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Action:CaptureOutput'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    variable_name: VariableName = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'VariableName'})
    search: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Search'})
    forward_by: ForwardBy = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ForwardBy'})
    capture: Capture = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Capture'})
