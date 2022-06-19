
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class WorkloadPolicy(AAPIObject):

    @attrs.define
    class Filter(AAPIObject):

        job_name: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'JobName'})
        application: str = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Application'})
        sub_application: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'SubApplication'})
        job_type: str = attrs.field(kw_only=True, default=None, metadata={
                                    '_aapi_repr_': 'JobType'})
        folder: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Folder'})
        host: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Host'})
        server: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Server'})

    _type: str = attrs.field(init=False, default='WorkloadPolicy', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'WorkloadPolicy'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    filter: Filter = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Filter'})
    host_mappings: typing.List[HostMapping] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'HostMappings'})
    running_jobs: typing.List[RunningJobs] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'RunningJobs'})
    resource_pools: typing.List[ResourcePools] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ResourcePools'})
    description: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Description'})
