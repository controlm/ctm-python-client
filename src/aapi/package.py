
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class Package(AAPIObject):

    class Source(enum.Enum):

        File_System = "File_System"
        SSIS_Package_Store = "SSIS_Package_Store"
        SQL_Server = "SQL_Server"

    _type: str = attrs.field(init=False, default='Package', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Package'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    source: Source = attrs.field(metadata={'_aapi_repr_': 'Source'})
    name: str = attrs.field(metadata={'_aapi_repr_': 'Name'})
    password: str = attrs.field(metadata={'_aapi_repr_': 'Password'})
