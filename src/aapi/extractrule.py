
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class ExtractRule(AAPIObject):

    rule_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'RuleName'})
    work_flow_name: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'WorkFlowName'})
    work_flow_user_name: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'WorkFlowUserName'})
    folder_name: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'FolderName'})
    job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'JobName'})
