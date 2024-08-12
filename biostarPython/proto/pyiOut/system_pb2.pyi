import err_pb2 as _err_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraFrequency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FREQ_NONE: _ClassVar[CameraFrequency]
    FREQ_50HZ: _ClassVar[CameraFrequency]
    FREQ_60HZ: _ClassVar[CameraFrequency]

class CardOperationMask(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CARD_OPERATION_MASK_NONE: _ClassVar[CardOperationMask]
    CARD_OPERATION_MASK_CUSTOM_DESFIRE_EV1: _ClassVar[CardOperationMask]
    CARD_OPERATION_MASK_CUSTOM_CLASSIC_PLUS: _ClassVar[CardOperationMask]
    CARD_OPERATION_MASK_BLE: _ClassVar[CardOperationMask]
    CARD_OPERATION_MASK_NFC: _ClassVar[CardOperationMask]
    CARD_OPERATION_MASK_SEOS: _ClassVar[CardOperationMask]
    CARD_OPERATION_MASK_SR_SE: _ClassVar[CardOperationMask]
    CARD_OPERATION_MASK_DESFIRE_EV1: _ClassVar[CardOperationMask]
    CARD_OPERATION_MASK_CLASSIC_PLUS: _ClassVar[CardOperationMask]
    CARD_OPERATION_MASK_ICLASS: _ClassVar[CardOperationMask]
    CARD_OPERATION_MASK_MIFARE_FELICA: _ClassVar[CardOperationMask]
    CARD_OPERATION_MASK_HIDPROX: _ClassVar[CardOperationMask]
    CARD_OPERATION_MASK_EM: _ClassVar[CardOperationMask]
FREQ_NONE: CameraFrequency
FREQ_50HZ: CameraFrequency
FREQ_60HZ: CameraFrequency
CARD_OPERATION_MASK_NONE: CardOperationMask
CARD_OPERATION_MASK_CUSTOM_DESFIRE_EV1: CardOperationMask
CARD_OPERATION_MASK_CUSTOM_CLASSIC_PLUS: CardOperationMask
CARD_OPERATION_MASK_BLE: CardOperationMask
CARD_OPERATION_MASK_NFC: CardOperationMask
CARD_OPERATION_MASK_SEOS: CardOperationMask
CARD_OPERATION_MASK_SR_SE: CardOperationMask
CARD_OPERATION_MASK_DESFIRE_EV1: CardOperationMask
CARD_OPERATION_MASK_CLASSIC_PLUS: CardOperationMask
CARD_OPERATION_MASK_ICLASS: CardOperationMask
CARD_OPERATION_MASK_MIFARE_FELICA: CardOperationMask
CARD_OPERATION_MASK_HIDPROX: CardOperationMask
CARD_OPERATION_MASK_EM: CardOperationMask

class SystemConfig(_message.Message):
    __slots__ = ("timeZone", "syncTime", "isLocked", "useInterphone", "OSDPKeyEncrypted", "useJobCode", "useAlphanumericID", "cameraFrequency", "useSecureTamper", "useCardOperationMask")
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    SYNCTIME_FIELD_NUMBER: _ClassVar[int]
    ISLOCKED_FIELD_NUMBER: _ClassVar[int]
    USEINTERPHONE_FIELD_NUMBER: _ClassVar[int]
    OSDPKEYENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    USEJOBCODE_FIELD_NUMBER: _ClassVar[int]
    USEALPHANUMERICID_FIELD_NUMBER: _ClassVar[int]
    CAMERAFREQUENCY_FIELD_NUMBER: _ClassVar[int]
    USESECURETAMPER_FIELD_NUMBER: _ClassVar[int]
    USECARDOPERATIONMASK_FIELD_NUMBER: _ClassVar[int]
    timeZone: int
    syncTime: bool
    isLocked: bool
    useInterphone: bool
    OSDPKeyEncrypted: bool
    useJobCode: bool
    useAlphanumericID: bool
    cameraFrequency: CameraFrequency
    useSecureTamper: bool
    useCardOperationMask: int
    def __init__(self, timeZone: _Optional[int] = ..., syncTime: bool = ..., isLocked: bool = ..., useInterphone: bool = ..., OSDPKeyEncrypted: bool = ..., useJobCode: bool = ..., useAlphanumericID: bool = ..., cameraFrequency: _Optional[_Union[CameraFrequency, str]] = ..., useSecureTamper: bool = ..., useCardOperationMask: _Optional[int] = ...) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: SystemConfig
    def __init__(self, config: _Optional[_Union[SystemConfig, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: SystemConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[SystemConfig, _Mapping]] = ...) -> None: ...

class SetConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: SystemConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[SystemConfig, _Mapping]] = ...) -> None: ...

class SetConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...
