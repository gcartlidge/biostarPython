import card_pb2 as _card_pb2
import finger_pb2 as _finger_pb2
import user_pb2 as _user_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_REQUEST: _ClassVar[RequestType]
    VERIFY_REQUEST: _ClassVar[RequestType]
    IDENTIFY_REQUEST: _ClassVar[RequestType]
    GLOBAL_APB_REQUEST: _ClassVar[RequestType]
    USER_PHRASE_REQUEST: _ClassVar[RequestType]

class ServerErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUCCESS: _ClassVar[ServerErrorCode]
    VERIFY_FAIL: _ClassVar[ServerErrorCode]
    IDENTIFY_FAIL: _ClassVar[ServerErrorCode]
    HARD_APB_VIOLATION: _ClassVar[ServerErrorCode]
    SOFT_APB_VIOLATION: _ClassVar[ServerErrorCode]
    CANNOT_FIND_USER: _ClassVar[ServerErrorCode]
NO_REQUEST: RequestType
VERIFY_REQUEST: RequestType
IDENTIFY_REQUEST: RequestType
GLOBAL_APB_REQUEST: RequestType
USER_PHRASE_REQUEST: RequestType
SUCCESS: ServerErrorCode
VERIFY_FAIL: ServerErrorCode
IDENTIFY_FAIL: ServerErrorCode
HARD_APB_VIOLATION: ServerErrorCode
SOFT_APB_VIOLATION: ServerErrorCode
CANNOT_FIND_USER: ServerErrorCode

class ServerRequest(_message.Message):
    __slots__ = ("reqType", "deviceID", "seqNO", "verifyReq", "identifyReq", "globalAPBReq", "userPhraseReq")
    REQTYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    VERIFYREQ_FIELD_NUMBER: _ClassVar[int]
    IDENTIFYREQ_FIELD_NUMBER: _ClassVar[int]
    GLOBALAPBREQ_FIELD_NUMBER: _ClassVar[int]
    USERPHRASEREQ_FIELD_NUMBER: _ClassVar[int]
    reqType: RequestType
    deviceID: int
    seqNO: int
    verifyReq: VerifyRequest
    identifyReq: IdentifyRequest
    globalAPBReq: GlobalAPBRequest
    userPhraseReq: UserPhraseRequest
    def __init__(self, reqType: _Optional[_Union[RequestType, str]] = ..., deviceID: _Optional[int] = ..., seqNO: _Optional[int] = ..., verifyReq: _Optional[_Union[VerifyRequest, _Mapping]] = ..., identifyReq: _Optional[_Union[IdentifyRequest, _Mapping]] = ..., globalAPBReq: _Optional[_Union[GlobalAPBRequest, _Mapping]] = ..., userPhraseReq: _Optional[_Union[UserPhraseRequest, _Mapping]] = ...) -> None: ...

class VerifyRequest(_message.Message):
    __slots__ = ("isCard", "cardType", "cardData", "userID")
    ISCARD_FIELD_NUMBER: _ClassVar[int]
    CARDTYPE_FIELD_NUMBER: _ClassVar[int]
    CARDDATA_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    isCard: bool
    cardType: _card_pb2.Type
    cardData: bytes
    userID: str
    def __init__(self, isCard: bool = ..., cardType: _Optional[_Union[_card_pb2.Type, str]] = ..., cardData: _Optional[bytes] = ..., userID: _Optional[str] = ...) -> None: ...

class IdentifyRequest(_message.Message):
    __slots__ = ("templateFormat", "templateData")
    TEMPLATEFORMAT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATEDATA_FIELD_NUMBER: _ClassVar[int]
    templateFormat: _finger_pb2.TemplateFormat
    templateData: bytes
    def __init__(self, templateFormat: _Optional[_Union[_finger_pb2.TemplateFormat, str]] = ..., templateData: _Optional[bytes] = ...) -> None: ...

class GlobalAPBRequest(_message.Message):
    __slots__ = ("userIDs",)
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    userIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, userIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class UserPhraseRequest(_message.Message):
    __slots__ = ("userID",)
    USERID_FIELD_NUMBER: _ClassVar[int]
    userID: str
    def __init__(self, userID: _Optional[str] = ...) -> None: ...

class SubscribeRequest(_message.Message):
    __slots__ = ("queueSize",)
    QUEUESIZE_FIELD_NUMBER: _ClassVar[int]
    queueSize: int
    def __init__(self, queueSize: _Optional[int] = ...) -> None: ...

class UnsubscribeRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnsubscribeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HandleVerifyRequest(_message.Message):
    __slots__ = ("deviceID", "seqNO", "errCode", "user")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    ERRCODE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    seqNO: int
    errCode: ServerErrorCode
    user: _user_pb2.UserInfo
    def __init__(self, deviceID: _Optional[int] = ..., seqNO: _Optional[int] = ..., errCode: _Optional[_Union[ServerErrorCode, str]] = ..., user: _Optional[_Union[_user_pb2.UserInfo, _Mapping]] = ...) -> None: ...

class HandleVerifyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HandleIdentifyRequest(_message.Message):
    __slots__ = ("deviceID", "seqNO", "errCode", "user")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    ERRCODE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    seqNO: int
    errCode: ServerErrorCode
    user: _user_pb2.UserInfo
    def __init__(self, deviceID: _Optional[int] = ..., seqNO: _Optional[int] = ..., errCode: _Optional[_Union[ServerErrorCode, str]] = ..., user: _Optional[_Union[_user_pb2.UserInfo, _Mapping]] = ...) -> None: ...

class HandleIdentifyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HandleGlobalAPBRequest(_message.Message):
    __slots__ = ("deviceID", "seqNO", "errCode", "zoneID")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    ERRCODE_FIELD_NUMBER: _ClassVar[int]
    ZONEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    seqNO: int
    errCode: ServerErrorCode
    zoneID: int
    def __init__(self, deviceID: _Optional[int] = ..., seqNO: _Optional[int] = ..., errCode: _Optional[_Union[ServerErrorCode, str]] = ..., zoneID: _Optional[int] = ...) -> None: ...

class HandleGlobalAPBResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HandleUserPhraseRequest(_message.Message):
    __slots__ = ("deviceID", "seqNO", "errCode", "userPhrase")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    ERRCODE_FIELD_NUMBER: _ClassVar[int]
    USERPHRASE_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    seqNO: int
    errCode: ServerErrorCode
    userPhrase: str
    def __init__(self, deviceID: _Optional[int] = ..., seqNO: _Optional[int] = ..., errCode: _Optional[_Union[ServerErrorCode, str]] = ..., userPhrase: _Optional[str] = ...) -> None: ...

class HandleUserPhraseResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
