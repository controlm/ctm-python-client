
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class ActionRun(AAPIObject):


    _type: str = attrs.field(init=False, default='Action:Run', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Action:Run'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    folder: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'Folder'})
    job: str = attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Job'})
    lib: str = attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Lib'})
    date: str = attrs.field(kw_only=True, default=None,
                             metadata={'_aapi_repr_': 'Date'})
    controlm_server: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'ControlmServer'})
    run_as_independent_flow: bool = attrs.field(kw_only=True, default=None, metadata={
                                                '_aapi_repr_': 'RunAsIndependentFlow'})
    variables: typing.List[typing.Dict[str,str]] = attrs.field(
        kw_only=True, factory=list, metadata={'_aapi_repr_': 'Variables'})
