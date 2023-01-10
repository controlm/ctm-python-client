from __future__ import annotations

from aapi.job import Job
from aapi.connectionprofile import ConnectionProfile

import attrs


@attrs.define
class AIJob(Job):
    _type: str = attrs.field(init=False, default='Job:ApplicationIntegrator', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Job:ApplicationIntegrator'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_profile: str = attrs.field(
        metadata={'_aapi_repr_': 'ConnectionProfile'})

    @staticmethod
    def field_optional(name: str, default: str=None):
        if not name.startswith('AI-'):
            name = 'AI-'+name

        return attrs.field(metadata={'_aapi_repr_': name}, kw_only=True, default=default)

    @staticmethod
    def field(name: str):
        if not name.startswith('AI-'):
            name = 'AI-'+name

        return attrs.field(metadata={'_aapi_repr_': name})

    @staticmethod
    def type_field(name: str):
        name = 'Job:ApplicationIntegrator:AI '+name
        return attrs.field(init=False, default=name, metadata={
            '_aapi_repr_': 'Type', '_type_aapi_': name})


@attrs.define
class AIConnectionProfile(ConnectionProfile):
    _type: str = attrs.field(init=False, default='AI ConnectionProfile', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'AI ConnectionProfile'})

    object_name: str = attrs.field(metadata={'_aapi_name_': True})

    @staticmethod
    def type_field(name: str):
        name = 'ConnectionProfile:ApplicationIntegrator:AI '+name
        return attrs.field(init=False, default=name, metadata={
            '_aapi_repr_': 'Type', '_type_aapi_': name})


    @staticmethod
    def field_optional(name: str, default:str = None):
        if not name.startswith('AI-'):
            name = 'AI-'+name

        return attrs.field(metadata={'_aapi_repr_': name}, kw_only=True, default=default)

    @staticmethod
    def field(name: str):
        if not name.startswith('AI-'):
            name = 'AI-'+name
        return attrs.field(metadata={'_aapi_repr_': name})
