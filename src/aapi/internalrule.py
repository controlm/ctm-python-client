
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class InternalRule(AAPIObject):

    @attrs.define
    class Include(AAPIObject):

        values: typing.List[SiteStandardPossibleValue] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'Values'})
        patterns: typing.List[str] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'Patterns'})

    @attrs.define
    class Characters(AAPIObject):

        @attrs.define
        class Any(AAPIObject):

            except_for_characters: str = attrs.field(kw_only=True, default=None, metadata={
                                                     '_aapi_repr_': 'ExceptForCharacters'})

        @attrs.define
        class Alphanumeric(AAPIObject):

            uppercase_letters: bool = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'UppercaseLetters'})
            lowercase_letters: bool = attrs.field(kw_only=True, default=None, metadata={
                                                  '_aapi_repr_': 'LowercaseLetters'})
            digits: bool = attrs.field(kw_only=True, default=None, metadata={
                                       '_aapi_repr_': 'Digits'})
            specific_characters: str = attrs.field(kw_only=True, default=None, metadata={
                                                   '_aapi_repr_': 'SpecificCharacters'})

        minimum_length: int = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'MinimumLength'})
        maximum_length: int = attrs.field(kw_only=True, default=None, metadata={
                                          '_aapi_repr_': 'MaximumLength'})
        any: Any = attrs.field(kw_only=True, default=None,
                               metadata={'_aapi_repr_': 'Any'})
        alphanumeric: Alphanumeric = attrs.field(kw_only=True, default=None, metadata={
                                                 '_aapi_repr_': 'Alphanumeric'})

    @attrs.define
    class Exclude(AAPIObject):

        values: typing.List[SiteStandardPossibleValue] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'Values'})
        patterns: typing.List[str] = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'Patterns'})

    _type: str = attrs.field(init=False, default='InternalRule', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'InternalRule'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    rule_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'RuleName'})
    include: Include = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Include'})
    characters: Characters = attrs.field(kw_only=True, default=None, metadata={
                                         '_aapi_repr_': 'Characters'})
    exclude: Exclude = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'Exclude'})
