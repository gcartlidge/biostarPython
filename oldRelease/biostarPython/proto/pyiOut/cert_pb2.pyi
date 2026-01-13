from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PKIName(_message.Message):
    __slots__ = ("country", "province", "city", "organization", "organizationUnit", "commonName")
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONUNIT_FIELD_NUMBER: _ClassVar[int]
    COMMONNAME_FIELD_NUMBER: _ClassVar[int]
    country: str
    province: str
    city: str
    organization: str
    organizationUnit: str
    commonName: str
    def __init__(self, country: _Optional[str] = ..., province: _Optional[str] = ..., city: _Optional[str] = ..., organization: _Optional[str] = ..., organizationUnit: _Optional[str] = ..., commonName: _Optional[str] = ...) -> None: ...

class CreateServerCertificateRequest(_message.Message):
    __slots__ = ("subject", "domainNames", "IPAddrs", "expireAfterYears")
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    DOMAINNAMES_FIELD_NUMBER: _ClassVar[int]
    IPADDRS_FIELD_NUMBER: _ClassVar[int]
    EXPIREAFTERYEARS_FIELD_NUMBER: _ClassVar[int]
    subject: PKIName
    domainNames: _containers.RepeatedScalarFieldContainer[str]
    IPAddrs: _containers.RepeatedScalarFieldContainer[str]
    expireAfterYears: int
    def __init__(self, subject: _Optional[_Union[PKIName, _Mapping]] = ..., domainNames: _Optional[_Iterable[str]] = ..., IPAddrs: _Optional[_Iterable[str]] = ..., expireAfterYears: _Optional[int] = ...) -> None: ...

class CreateServerCertificateResponse(_message.Message):
    __slots__ = ("serverCert", "serverKey")
    SERVERCERT_FIELD_NUMBER: _ClassVar[int]
    SERVERKEY_FIELD_NUMBER: _ClassVar[int]
    serverCert: str
    serverKey: str
    def __init__(self, serverCert: _Optional[str] = ..., serverKey: _Optional[str] = ...) -> None: ...

class SetServerCertificateRequest(_message.Message):
    __slots__ = ("serverCert", "serverKey")
    SERVERCERT_FIELD_NUMBER: _ClassVar[int]
    SERVERKEY_FIELD_NUMBER: _ClassVar[int]
    serverCert: str
    serverKey: str
    def __init__(self, serverCert: _Optional[str] = ..., serverKey: _Optional[str] = ...) -> None: ...

class SetServerCertificateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetGatewayCertificateRequest(_message.Message):
    __slots__ = ("gatewayCert", "gatewayKey")
    GATEWAYCERT_FIELD_NUMBER: _ClassVar[int]
    GATEWAYKEY_FIELD_NUMBER: _ClassVar[int]
    gatewayCert: str
    gatewayKey: str
    def __init__(self, gatewayCert: _Optional[str] = ..., gatewayKey: _Optional[str] = ...) -> None: ...

class SetGatewayCertificateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
