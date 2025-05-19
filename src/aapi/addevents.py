
from __future__ import annotations
import attrs
import typing
import enum
import random
import string

from aapi.bases import AAPIObject
from aapi.event import EventOutAdd

@attrs.define
class AddEvents(AAPIObject):

    _type: str = attrs.field(init=False, default='AddEvents', metadata={
        '_aapi_repr_': 'Type', '_type_aapi_': 'AddEvents'})
    object_name: str = attrs.field(init=False, default='eventsToAdd', metadata={
        '_aapi_name_': True})
    events: typing.List[EventOutAdd] = attrs.field(
        metadata={'_aapi_repr_': 'Events'})

    def __attrs_post_init__(self):
        if self.object_name == attrs.fields_dict(self.__class__)['object_name'].default:
            random_attr = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            self.object_name = f'{self.object_name}_{random_attr}'
