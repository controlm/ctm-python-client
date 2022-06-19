
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class StepRange(AAPIObject):

    _type: str = attrs.field(init=False, default='StepRange', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'StepRange'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    from_program: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'FromProgram'})
    from_procedure: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'FromProcedure'})
    to_program: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'ToProgram'})
    to_procedure: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'ToProcedure'})
