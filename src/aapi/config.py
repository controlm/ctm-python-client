
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class Config(AAPIObject):

    _type: str = attrs.field(init=False, default='Config', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Config'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class ConfigHadoop(Config):

    _type: str = attrs.field(init=False, default='Config:Hadoop', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Config:Hadoop'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    agent_principal: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'AgentPrincipal'})
    agent_keytab_file_path: str = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'AgentKeytabFilePath'})
