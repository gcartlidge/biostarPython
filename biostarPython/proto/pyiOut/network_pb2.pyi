import err_pb2 as _err_pb2
import connect_pb2 as _connect_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIRST_ENUM_VALUE_MUST_BE_ZERO: _ClassVar[Enum]
    DEFAULT_TCP_DEVICE_PORT: _ClassVar[Enum]
    DEFAULT_TCP_SERVER_PORT: _ClassVar[Enum]
    DEFAULT_TCP_SSL_SERVER_PORT: _ClassVar[Enum]
    MIN_TCP_MTU_SIZE: _ClassVar[Enum]
    MAX_TCP_MTU_SIZE: _ClassVar[Enum]
    MAX_ESSID_LENGTH: _ClassVar[Enum]
    MAX_WLAN_KEY_LENGTH: _ClassVar[Enum]
    MAX_DNS_URL_LENGTH: _ClassVar[Enum]

class EthernetBaseband(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BASEBAND_10BASE_T: _ClassVar[EthernetBaseband]
    BASEBAND_100BASE_T: _ClassVar[EthernetBaseband]

class WLANOperationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WLAN_OPMODE_MANAGED: _ClassVar[WLANOperationMode]
    WLAN_OPMODE_ADHOC: _ClassVar[WLANOperationMode]

class WLANAuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WLAN_AUTH_OPEN: _ClassVar[WLANAuthType]
    WLAN_AUTH_SHARED: _ClassVar[WLANAuthType]
    WLAN_AUTH_WPA_PSK: _ClassVar[WLANAuthType]
    WLAN_AUTH_WPA2_PSK: _ClassVar[WLANAuthType]

class WLANEncryptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WLAN_ENC_NONE: _ClassVar[WLANEncryptionType]
    BS2_WLAN_ENC_WEP: _ClassVar[WLANEncryptionType]
    BS2_WLAN_ENC_TKIP_AES: _ClassVar[WLANEncryptionType]
    BS2_WLAN_ENC_AES: _ClassVar[WLANEncryptionType]
    BS2_WLAN_ENC_TKIP: _ClassVar[WLANEncryptionType]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
DEFAULT_TCP_DEVICE_PORT: Enum
DEFAULT_TCP_SERVER_PORT: Enum
DEFAULT_TCP_SSL_SERVER_PORT: Enum
MIN_TCP_MTU_SIZE: Enum
MAX_TCP_MTU_SIZE: Enum
MAX_ESSID_LENGTH: Enum
MAX_WLAN_KEY_LENGTH: Enum
MAX_DNS_URL_LENGTH: Enum
BASEBAND_10BASE_T: EthernetBaseband
BASEBAND_100BASE_T: EthernetBaseband
WLAN_OPMODE_MANAGED: WLANOperationMode
WLAN_OPMODE_ADHOC: WLANOperationMode
WLAN_AUTH_OPEN: WLANAuthType
WLAN_AUTH_SHARED: WLANAuthType
WLAN_AUTH_WPA_PSK: WLANAuthType
WLAN_AUTH_WPA2_PSK: WLANAuthType
WLAN_ENC_NONE: WLANEncryptionType
BS2_WLAN_ENC_WEP: WLANEncryptionType
BS2_WLAN_ENC_TKIP_AES: WLANEncryptionType
BS2_WLAN_ENC_AES: WLANEncryptionType
BS2_WLAN_ENC_TKIP: WLANEncryptionType

class GetIPConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetIPConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: IPConfig
    def __init__(self, config: _Optional[_Union[IPConfig, _Mapping]] = ...) -> None: ...

class SetIPConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: IPConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[IPConfig, _Mapping]] = ...) -> None: ...

class SetIPConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetIPConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: IPConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[IPConfig, _Mapping]] = ...) -> None: ...

class SetIPConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class IPConfig(_message.Message):
    __slots__ = ("useDHCP", "IPAddr", "gateway", "subnetMask", "port", "connectionMode", "serverAddr", "serverPort", "SSLServerPort", "useDNS", "DNSServer", "serverURL", "MTUSize", "baseband")
    USEDHCP_FIELD_NUMBER: _ClassVar[int]
    IPADDR_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    SUBNETMASK_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONMODE_FIELD_NUMBER: _ClassVar[int]
    SERVERADDR_FIELD_NUMBER: _ClassVar[int]
    SERVERPORT_FIELD_NUMBER: _ClassVar[int]
    SSLSERVERPORT_FIELD_NUMBER: _ClassVar[int]
    USEDNS_FIELD_NUMBER: _ClassVar[int]
    DNSSERVER_FIELD_NUMBER: _ClassVar[int]
    SERVERURL_FIELD_NUMBER: _ClassVar[int]
    MTUSIZE_FIELD_NUMBER: _ClassVar[int]
    BASEBAND_FIELD_NUMBER: _ClassVar[int]
    useDHCP: bool
    IPAddr: str
    gateway: str
    subnetMask: str
    port: int
    connectionMode: _connect_pb2.ConnectionMode
    serverAddr: str
    serverPort: int
    SSLServerPort: int
    useDNS: bool
    DNSServer: str
    serverURL: str
    MTUSize: int
    baseband: EthernetBaseband
    def __init__(self, useDHCP: bool = ..., IPAddr: _Optional[str] = ..., gateway: _Optional[str] = ..., subnetMask: _Optional[str] = ..., port: _Optional[int] = ..., connectionMode: _Optional[_Union[_connect_pb2.ConnectionMode, str]] = ..., serverAddr: _Optional[str] = ..., serverPort: _Optional[int] = ..., SSLServerPort: _Optional[int] = ..., useDNS: bool = ..., DNSServer: _Optional[str] = ..., serverURL: _Optional[str] = ..., MTUSize: _Optional[int] = ..., baseband: _Optional[_Union[EthernetBaseband, str]] = ...) -> None: ...

class GetWLANConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetWLANConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: WLANConfig
    def __init__(self, config: _Optional[_Union[WLANConfig, _Mapping]] = ...) -> None: ...

class SetWLANConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: WLANConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[WLANConfig, _Mapping]] = ...) -> None: ...

class SetWLANConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetWLANConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: WLANConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[WLANConfig, _Mapping]] = ...) -> None: ...

class SetWLANConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class WLANConfig(_message.Message):
    __slots__ = ("enabled", "opMode", "authType", "encType", "ESSID", "authKey")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    OPMODE_FIELD_NUMBER: _ClassVar[int]
    AUTHTYPE_FIELD_NUMBER: _ClassVar[int]
    ENCTYPE_FIELD_NUMBER: _ClassVar[int]
    ESSID_FIELD_NUMBER: _ClassVar[int]
    AUTHKEY_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    opMode: WLANOperationMode
    authType: WLANAuthType
    encType: WLANEncryptionType
    ESSID: str
    authKey: str
    def __init__(self, enabled: bool = ..., opMode: _Optional[_Union[WLANOperationMode, str]] = ..., authType: _Optional[_Union[WLANAuthType, str]] = ..., encType: _Optional[_Union[WLANEncryptionType, str]] = ..., ESSID: _Optional[str] = ..., authKey: _Optional[str] = ...) -> None: ...
