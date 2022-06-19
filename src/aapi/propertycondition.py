
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class PropertyCondition(AAPIObject):

    class Property(enum.Enum):

        Name = "Name"
        Value = "Value"
        Calendar = "Calendar"
        MonthDaysCalendar = "MonthDaysCalendar"
        WeekDaysCalendar = "WeekDaysCalendar"
        DaysKeepActive = "DaysKeepActive"
        ConfirmationCalendar = "ConfirmationCalendar"
        ExceptionalPolicy = "ExceptionalPolicy"
        ActivePeriod = "ActivePeriod"
        Event = "Event"
        Remove = "Remove"
        PoolName = "PoolName"
        Quantity = "Quantity"
        FolderName = "FolderName"
        OnFail = "OnFail"
        OnOK = "OnOK"
        LockName = "LockName"
        LockType = "LockType"
        NotificationType = "NotificationType"
        Message = "Message"
        Urgency = "Urgency"
        Destination = "Destination"
        FromProgram = "FromProgram"
        FromProcedure = "FromProcedure"
        ToProgram = "ToProgram"
        ToProcedure = "ToProcedure"
        CaptureVariableName = "CaptureVariableName"

    class Operator(enum.Enum):

        Equals = "Equals"
        DoesNotEqual = "DoesNotEqual"
        GreaterThan = "GreaterThan"
        LessThan = "LessThan"
        Contains = "Contains"
        DoesNotContain = "DoesNotContain"
        IsEmpty = "IsEmpty"
        IsNotEmpty = "IsNotEmpty"
        StartsWith = "StartsWith"
        DoesNotStartsWith = "DoesNotStartsWith"
        EndsWith = "EndsWith"
        DoesNotEndsWith = "DoesNotEndsWith"

    _type: str = attrs.field(init=False, default='PropertyCondition', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'PropertyCondition'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    property: Property = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Property'})
    operator: Operator = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'Operator'})
    value: str = attrs.field(kw_only=True, default=None, metadata={
                             '_aapi_repr_': 'Value'})
