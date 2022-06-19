
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class Period(AAPIObject):

    class Period(enum.Enum):

        _0 = "_0"
        _1 = "_1"
        _2 = "_2"
        _3 = "_3"
        _4 = "_4"
        _5 = "_5"
        _6 = "_6"
        _7 = "_7"
        _8 = "_8"
        _9 = "_9"
        A = "A"
        B = "B"
        C = "C"
        D = "D"
        E = "E"
        F = "F"
        G = "G"
        H = "H"
        I = "I"
        J = "J"
        K = "K"
        L = "L"
        M = "M"
        O = "O"
        P = "P"
        Q = "Q"
        R = "R"
        S = "S"
        T = "T"
        U = "U"
        V = "V"
        W = "W"
        X = "X"
        Z = "Z"
        All = "All"

    _type: str = attrs.field(init=False, default='Period', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Period'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    period: Period = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'Period'})
    years: typing.List[Year] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'Years'})
