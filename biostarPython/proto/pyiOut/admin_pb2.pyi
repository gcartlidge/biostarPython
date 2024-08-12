from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetInfoRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetInfoResponse(_message.Message):
    __slots__ = ("version", "buildDate")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BUILDDATE_FIELD_NUMBER: _ClassVar[int]
    version: str
    buildDate: str
    def __init__(self, version: _Optional[str] = ..., buildDate: _Optional[str] = ...) -> None: ...
