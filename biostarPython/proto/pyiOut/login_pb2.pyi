from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LoginRequest(_message.Message):
    __slots__ = ("tenantCert",)
    TENANTCERT_FIELD_NUMBER: _ClassVar[int]
    tenantCert: str
    def __init__(self, tenantCert: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("jwtToken",)
    JWTTOKEN_FIELD_NUMBER: _ClassVar[int]
    jwtToken: str
    def __init__(self, jwtToken: _Optional[str] = ...) -> None: ...

class LoginAdminRequest(_message.Message):
    __slots__ = ("adminTenantCert", "tenantID")
    ADMINTENANTCERT_FIELD_NUMBER: _ClassVar[int]
    TENANTID_FIELD_NUMBER: _ClassVar[int]
    adminTenantCert: str
    tenantID: str
    def __init__(self, adminTenantCert: _Optional[str] = ..., tenantID: _Optional[str] = ...) -> None: ...

class LoginAdminResponse(_message.Message):
    __slots__ = ("jwtToken",)
    JWTTOKEN_FIELD_NUMBER: _ClassVar[int]
    jwtToken: str
    def __init__(self, jwtToken: _Optional[str] = ...) -> None: ...

class LogoutRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LogoutResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
