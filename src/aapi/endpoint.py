
from __future__ import annotations
import attrs
import typing
import enum
from aapi import *


@attrs.define
class Endpoint(AAPIObject):

    class OsType(enum.Enum):

        Tandem = "Tandem"

    _type: str = attrs.field(init=False, default='Endpoint', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Endpoint'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    user: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'User'})
    os_type: OsType = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'OsType'})
    port: str = attrs.field(kw_only=True, default=None,
                            metadata={'_aapi_repr_': 'Port'})
    home_directory: str = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'HomeDirectory'})
    host_name: str = attrs.field(kw_only=True, default=None, metadata={
                                 '_aapi_repr_': 'HostName'})
    password: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Password'})
    conntype: str = attrs.field(kw_only=True, default=None, metadata={
                                '_aapi_repr_': 'Conntype'})
    private_key_name: str = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'PrivateKeyName'})
    passphrase: str = attrs.field(kw_only=True, default=None, metadata={
                                  '_aapi_repr_': 'Passphrase'})
    additional_parameters: typing.List[PackageParams] = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'AdditionalParameters'})


@attrs.define
class EndpointSrc(Endpoint):

    _type: str = attrs.field(init=False, default='Endpoint:Src', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Endpoint:Src'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class EndpointDest(Endpoint):

    _type: str = attrs.field(init=False, default='Endpoint:Dest', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Endpoint:Dest'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class EndpointSrcSftp(EndpointSrc):

    _type: str = attrs.field(init=False, default='Endpoint:Src:SFTP', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Endpoint:Src:SFTP'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    ssh_compression: bool = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'SSHCompression'})


@attrs.define
class EndpointDestSftp(EndpointDest):

    _type: str = attrs.field(init=False, default='Endpoint:Dest:SFTP', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Endpoint:Dest:SFTP'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    ssh_compression: bool = attrs.field(kw_only=True, default=None, metadata={
                                        '_aapi_repr_': 'SSHCompression'})


@attrs.define
class EndpointSrcFtp(EndpointSrc):

    class ConnectionMode(enum.Enum):

        Active = "Active"
        Passive = "Passive"
        PassiveSubstituteIpAddress = "PassiveSubstituteIpAddress"
        EPSV = "EPSV"
        EPSVSubstituteIpAddress = "EPSVSubstituteIpAddress"
        off = "off"
        on = "on"
        noSubstituteIP = "noSubstituteIP"

    _type: str = attrs.field(init=False, default='Endpoint:Src:FTP', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Endpoint:Src:FTP'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_mode: ConnectionMode = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ConnectionMode'})


@attrs.define
class EndpointDestFtp(EndpointDest):

    class ConnectionMode(enum.Enum):

        Active = "Active"
        Passive = "Passive"
        PassiveSubstituteIpAddress = "PassiveSubstituteIpAddress"
        EPSV = "EPSV"
        EPSVSubstituteIpAddress = "EPSVSubstituteIpAddress"
        off = "off"
        on = "on"
        noSubstituteIP = "noSubstituteIP"

    _type: str = attrs.field(init=False, default='Endpoint:Dest:FTP', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Endpoint:Dest:FTP'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_mode: ConnectionMode = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ConnectionMode'})


@attrs.define
class EndpointSrcFtps(EndpointSrc):

    class ConnectionMode(enum.Enum):

        Active = "Active"
        Passive = "Passive"
        PassiveSubstituteIpAddress = "PassiveSubstituteIpAddress"
        EPSV = "EPSV"
        EPSVSubstituteIpAddress = "EPSVSubstituteIpAddress"
        off = "off"
        on = "on"
        noSubstituteIP = "noSubstituteIP"

    class SslLevel(enum.Enum):

        NoAuthentication = "NoAuthentication"
        ServerAuthentication = "ServerAuthentication"
        ClientServerAuthentication = "ClientServerAuthentication"

    _type: str = attrs.field(init=False, default='Endpoint:Src:FTPS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Endpoint:Src:FTPS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_mode: ConnectionMode = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ConnectionMode'})
    ssl_level: SslLevel = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'SSLLevel'})
    ssl_implicit: bool = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'SSLImplicit'})
    clear_data_channel: bool = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'ClearDataChannel'})
    clear_command_channel: bool = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'ClearCommandChannel'})


@attrs.define
class EndpointDestFtps(EndpointDest):

    class ConnectionMode(enum.Enum):

        Active = "Active"
        Passive = "Passive"
        PassiveSubstituteIpAddress = "PassiveSubstituteIpAddress"
        EPSV = "EPSV"
        EPSVSubstituteIpAddress = "EPSVSubstituteIpAddress"
        off = "off"
        on = "on"
        noSubstituteIP = "noSubstituteIP"

    class SslLevel(enum.Enum):

        NoAuthentication = "NoAuthentication"
        ServerAuthentication = "ServerAuthentication"
        ClientServerAuthentication = "ClientServerAuthentication"

    _type: str = attrs.field(init=False, default='Endpoint:Dest:FTPS', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Endpoint:Dest:FTPS'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
    connection_mode: ConnectionMode = attrs.field(
        kw_only=True, default=None, metadata={'_aapi_repr_': 'ConnectionMode'})
    ssl_level: SslLevel = attrs.field(kw_only=True, default=None, metadata={
                                      '_aapi_repr_': 'SSLLevel'})
    ssl_implicit: bool = attrs.field(kw_only=True, default=None, metadata={
                                     '_aapi_repr_': 'SSLImplicit'})
    clear_data_channel: bool = attrs.field(kw_only=True, default=None, metadata={
                                           '_aapi_repr_': 'ClearDataChannel'})
    clear_command_channel: bool = attrs.field(kw_only=True, default=None, metadata={
                                              '_aapi_repr_': 'ClearCommandChannel'})


@attrs.define
class EndpointSrcLocal(EndpointSrc):

    _type: str = attrs.field(init=False, default='Endpoint:Src:Local', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Endpoint:Src:Local'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})


@attrs.define
class EndpointDestLocal(EndpointDest):

    _type: str = attrs.field(init=False, default='Endpoint:Dest:Local', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'Endpoint:Dest:Local'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
