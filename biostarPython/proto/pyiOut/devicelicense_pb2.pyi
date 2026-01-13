from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceLicenseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPE_NONE: _ClassVar[DeviceLicenseType]
    TYPE_VISUAL_QR: _ClassVar[DeviceLicenseType]
    TYPE_UZ_WIRELESS_LOCK: _ClassVar[DeviceLicenseType]

class DeviceLicenseSubType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBTYPE_NONE: _ClassVar[DeviceLicenseSubType]
    SUBTYPE_VISUAL_QR_CODE_CORP: _ClassVar[DeviceLicenseSubType]

class DeviceLicenseStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOT_SUPPORTED: _ClassVar[DeviceLicenseStatus]
    DISABLE: _ClassVar[DeviceLicenseStatus]
    ENABLE: _ClassVar[DeviceLicenseStatus]
    EXPIRED: _ClassVar[DeviceLicenseStatus]
    NOT_EXIST: _ClassVar[DeviceLicenseStatus]
    ALREADY_ADD: _ClassVar[DeviceLicenseStatus]
TYPE_NONE: DeviceLicenseType
TYPE_VISUAL_QR: DeviceLicenseType
TYPE_UZ_WIRELESS_LOCK: DeviceLicenseType
SUBTYPE_NONE: DeviceLicenseSubType
SUBTYPE_VISUAL_QR_CODE_CORP: DeviceLicenseSubType
NOT_SUPPORTED: DeviceLicenseStatus
DISABLE: DeviceLicenseStatus
ENABLE: DeviceLicenseStatus
EXPIRED: DeviceLicenseStatus
NOT_EXIST: DeviceLicenseStatus
ALREADY_ADD: DeviceLicenseStatus

class DeviceLicenseInfo(_message.Message):
    __slots__ = ("index", "hasCapability", "enabled", "enableCount", "type", "subType", "enableTime", "expiredTime", "issueNumber", "name")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    HASCAPABILITY_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENABLECOUNT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLETIME_FIELD_NUMBER: _ClassVar[int]
    EXPIREDTIME_FIELD_NUMBER: _ClassVar[int]
    ISSUENUMBER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    index: int
    hasCapability: int
    enabled: bool
    enableCount: int
    type: DeviceLicenseType
    subType: DeviceLicenseSubType
    enableTime: int
    expiredTime: int
    issueNumber: int
    name: str
    def __init__(self, index: _Optional[int] = ..., hasCapability: _Optional[int] = ..., enabled: bool = ..., enableCount: _Optional[int] = ..., type: _Optional[_Union[DeviceLicenseType, str]] = ..., subType: _Optional[_Union[DeviceLicenseSubType, str]] = ..., enableTime: _Optional[int] = ..., expiredTime: _Optional[int] = ..., issueNumber: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class DeviceLicenseConfig(_message.Message):
    __slots__ = ("version", "licenseInfo")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LICENSEINFO_FIELD_NUMBER: _ClassVar[int]
    version: int
    licenseInfo: _containers.RepeatedCompositeFieldContainer[DeviceLicenseInfo]
    def __init__(self, version: _Optional[int] = ..., licenseInfo: _Optional[_Iterable[_Union[DeviceLicenseInfo, _Mapping]]] = ...) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: DeviceLicenseConfig
    def __init__(self, config: _Optional[_Union[DeviceLicenseConfig, _Mapping]] = ...) -> None: ...

class DeviceLicenseBlob(_message.Message):
    __slots__ = ("type", "deviceIDs", "data")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    type: DeviceLicenseType
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    data: bytes
    def __init__(self, type: _Optional[_Union[DeviceLicenseType, str]] = ..., deviceIDs: _Optional[_Iterable[int]] = ..., data: _Optional[bytes] = ...) -> None: ...

class DeviceLicenseResult(_message.Message):
    __slots__ = ("deviceID", "status")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    status: DeviceLicenseStatus
    def __init__(self, deviceID: _Optional[int] = ..., status: _Optional[_Union[DeviceLicenseStatus, str]] = ...) -> None: ...

class EnableRequest(_message.Message):
    __slots__ = ("deviceID", "licenseBlob")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    LICENSEBLOB_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    licenseBlob: DeviceLicenseBlob
    def __init__(self, deviceID: _Optional[int] = ..., licenseBlob: _Optional[_Union[DeviceLicenseBlob, _Mapping]] = ...) -> None: ...

class EnableResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[DeviceLicenseResult]
    def __init__(self, results: _Optional[_Iterable[_Union[DeviceLicenseResult, _Mapping]]] = ...) -> None: ...

class DisableRequest(_message.Message):
    __slots__ = ("deviceID", "licenseBlob")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    LICENSEBLOB_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    licenseBlob: DeviceLicenseBlob
    def __init__(self, deviceID: _Optional[int] = ..., licenseBlob: _Optional[_Union[DeviceLicenseBlob, _Mapping]] = ...) -> None: ...

class DisableResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[DeviceLicenseResult]
    def __init__(self, results: _Optional[_Iterable[_Union[DeviceLicenseResult, _Mapping]]] = ...) -> None: ...

class QueryRequest(_message.Message):
    __slots__ = ("deviceID", "type")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    type: DeviceLicenseType
    def __init__(self, deviceID: _Optional[int] = ..., type: _Optional[_Union[DeviceLicenseType, str]] = ...) -> None: ...

class QueryResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[DeviceLicenseResult]
    def __init__(self, results: _Optional[_Iterable[_Union[DeviceLicenseResult, _Mapping]]] = ...) -> None: ...
