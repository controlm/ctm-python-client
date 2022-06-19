
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class IfBase(AAPIObject):

    _type: str = attrs.field(init=False, default='IfBase', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'IfBase'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    on_list: typing.List[On] = attrs.field(kw_only=True, factory=list, metadata={
                                           '_abstract_aapi_container_': True})
    do_list: typing.List[Do] = attrs.field(kw_only=True, factory=list, metadata={
                                           '_abstract_aapi_container_': True})


@attrs.define
class IfBaseFolder(IfBase):

    _type: str = attrs.field(init=False, default='IfBase:Folder', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'IfBase:Folder'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class IfOutput(IfBaseFolder):

    _type: str = attrs.field(init=False, default='If:Output', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'If:Output'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    code: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Code'})
    statement: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Statement'})


@attrs.define
class IfCompletionStatus(IfBaseFolder):


    _type: str = attrs.field(init=False, default='If:CompletionStatus', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'If:CompletionStatus'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    completion_status: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'CompletionStatus'})


@attrs.define
class IfNumberOfReruns(IfBaseFolder):

    _type: str = attrs.field(init=False, default='If:NumberOfReruns', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'If:NumberOfReruns'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    number_of_reruns: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'NumberOfReruns'})


@attrs.define
class IfNumberOfExecutions(IfBaseFolder):

    _type: str = attrs.field(init=False, default='If:NumberOfExecutions', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'If:NumberOfExecutions'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    number_of_executions: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'NumberOfExecutions'})


@attrs.define
class IfNumberOfFailures(IfBaseFolder):

    _type: str = attrs.field(init=False, default='If:NumberOfFailures', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'If:NumberOfFailures'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    number_of_failures: str = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'NumberOfFailures'})


@attrs.define
class IfJobNotSubmitted(IfBase):

    _type: str = attrs.field(init=False, default='If:JobNotSubmitted', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'If:JobNotSubmitted'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    job_not_submitted: str = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'JobNotSubmitted'})


@attrs.define
class IfJobOutputNotFound(IfBase):

    _type: str = attrs.field(init=False, default='If:JobOutputNotFound', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'If:JobOutputNotFound'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    job_output_not_found: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'JobOutputNotFound'})


@attrs.define
class IfVariableValue(IfBase):

    @attrs.define
    class RangeVariableValue(AAPIObject):

        min: str = attrs.field(kw_only=True, default=None,
                               metadata={'_aapi_repr_': 'Min'})
        max: str = attrs.field(kw_only=True, default=None,
                               metadata={'_aapi_repr_': 'Max'})

    class Operator(enum.Enum):

        NotEqualTo = "NotEqualTo"
        GreaterThanOrEqual = "GreaterThanOrEqual"
        LessThanOrEqual = "LessThanOrEqual"
        GreaterThan = "GreaterThan"
        LessThan = "LessThan"
        EqualTo = "EqualTo"
        InRange = "InRange"
        NotInRange = "NotInRange"
        Like = "Like"
        NotLike = "NotLike"
        IsExactly = "IsExactly"
        IsNotExactly = "IsNotExactly"
        StartsWith = "StartsWith"
        EndWith = "EndWith"
        Contains = "Contains"
        DoesNotContain = "DoesNotContain"
        IsEmpty = "IsEmpty"
        IsNotEmpty = "IsNotEmpty"

    _type: str = attrs.field(init=False, default='If:VariableValue', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'If:VariableValue'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    variable_name: str = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'VariableName'})
    range_variable_value: RangeVariableValue = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'RangeVariableValue'})
    variable_value: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'VariableValue'})
    operator: Operator = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Operator'})
