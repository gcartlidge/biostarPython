import card_pb2 as _card_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetectCardRequest(_message.Message):
    __slots__ = ("deviceID", "cardData")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CARDDATA_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    cardData: _card_pb2.CSNCardData
    def __init__(self, deviceID: _Optional[int] = ..., cardData: _Optional[_Union[_card_pb2.CSNCardData, _Mapping]] = ...) -> None: ...

class DetectCardResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DetectFaceRequest(_message.Message):
    __slots__ = ("deviceID", "faceTemplate")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    FACETEMPLATE_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    faceTemplate: bytes
    def __init__(self, deviceID: _Optional[int] = ..., faceTemplate: _Optional[bytes] = ...) -> None: ...

class DetectFaceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DetectFingerprintRequest(_message.Message):
    __slots__ = ("deviceID", "fingerprintTemplate")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINTTEMPLATE_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    fingerprintTemplate: bytes
    def __init__(self, deviceID: _Optional[int] = ..., fingerprintTemplate: _Optional[bytes] = ...) -> None: ...

class DetectFingerprintResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnterKeyRequest(_message.Message):
    __slots__ = ("deviceID", "input")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    input: str
    def __init__(self, deviceID: _Optional[int] = ..., input: _Optional[str] = ...) -> None: ...

class EnterKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
