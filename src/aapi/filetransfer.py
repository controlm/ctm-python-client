
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class FileTransfer(AAPIObject):

    @attrs.define
    class FileWatcherOptions(AAPIObject):

        class TimeLimitPolicy(enum.Enum):

            MinutesToWait = "MinutesToWait"
            WaitUntil = "WaitUntil"

        min_detected_size_in_bytes: str = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'MinDetectedSizeInBytes'})
        min_file_age: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'MinFileAge'})
        max_file_age: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'MaxFileAge'})
        assign_file_name_to_variable: str = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'AssignFileNameToVariable'})
        transfer_all_matching_files: bool = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'TransferAllMatchingFiles'})
        time_limit_policy: TimeLimitPolicy = attrs.field(
            kw_only=True, default=None, metadata={'_aapi_repr_': 'TimeLimitPolicy'})
        time_limit_value: str = attrs.field(kw_only=True, default=None, metadata={
                                            '_aapi_repr_': 'TimeLimitValue'})

    @attrs.define
    class PreCommandSrc(AAPIObject):

        action: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'action'})
        arg1: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'arg1'})
        arg2: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'arg2'})

    @attrs.define
    class PostCommandSrc(AAPIObject):

        action: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'action'})
        arg1: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'arg1'})
        arg2: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'arg2'})

    @attrs.define
    class PreCommandDest(AAPIObject):

        action: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'action'})
        arg1: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'arg1'})
        arg2: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'arg2'})

    @attrs.define
    class PostCommandDest(AAPIObject):

        action: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'action'})
        arg1: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'arg1'})
        arg2: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'arg2'})

    class TransferOption(enum.Enum):

        SrcToDest = "SrcToDest"
        DestToSrc = "DestToSrc"
        DestToSrcFileWatcher = "DestToSrcFileWatcher"
        SrcToDestFileWatcher = "SrcToDestFileWatcher"
        FileWatcher = "FileWatcher"
        DirectoryListing = "DirectoryListing"
        SyncSrcToDest = "SyncSrcToDest"
        SyncDestToSrc = "SyncDestToSrc"

    class TransferType(enum.Enum):

        Ascii = "Ascii"
        Binary = "Binary"

    # _type: str = attrs.field(init=False, default='FileTransfer', metadata={
    #                          '_aapi_repr_': 'Type', '_type_aapi_': 'FileTransfer'})
    # object_name: str = attrs.field(metadata={'_aapi_name_': True})
    src: str = attrs.field(kw_only=True, default=None,
                           metadata={'_aapi_repr_': 'Src'})
    dest: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Dest'})
    as2_subject: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'As2Subject'})
    as2_message: str = attrs.field(kw_only=True, default=None, metadata={
                                   '_aapi_repr_': 'As2Message'})
    transfer_option: TransferOption = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'TransferOption'})
    transfer_type: TransferType = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'TransferType'})
    file_watcher_options: FileWatcherOptions = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'FileWatcherOptions'})
    pre_command_src: PreCommandSrc = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'PreCommandSrc'})
    post_command_src: PostCommandSrc = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'PostCommandSrc'})
    pre_command_dest: PreCommandDest = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'PreCommandDest'})
    post_command_dest: PostCommandDest = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'PostCommandDest'})
    nullflds: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'NULLFLDS'})
    srcopt: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'SRCOPT'})
    vernum: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'VERNUM'})
    caseifs: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'CASEIFS'})
    trim: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'TRIM'})
    exclude_wildcard: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'EXCLUDE_WILDCARD'})
    if_exist: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'IF_EXIST'})
    unique: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'UNIQUE'})
    dstopt: str = attrs.field(kw_only=True, default=None, metadata={
                              '_aapi_repr_': 'DSTOPT'})
    abstime: str = attrs.field(kw_only=True, default=None, metadata={
                               '_aapi_repr_': 'ABSTIME'})
    timelimit: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'TIMELIMIT'})
    recursive: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'RECURSIVE'})
