
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class Tag(AAPIObject):

    _type: str = attrs.field(init=False, default='Tag', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Tag'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class TagFolder(Tag):

    _type: str = attrs.field(init=False, default='Tag:Folder', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Tag:Folder'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    active_from: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'active_from'})
    active_till: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'active_till'})
    max_wait: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'max_wait'})
    tag_relation_dc_wc: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'tag_relation_dc_wc'})
    week_days_calendar: str = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'WeekDaysCalendar'})
    month_days_calendar: str = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'MonthDaysCalendar'})
    exception_policy: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'ExceptionPolicy'})
    calendar: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Calendar'})


@attrs.define
class TagGlobal(Tag):

    _type: str = attrs.field(init=False, default='Tag:Global', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Tag:Global'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
