import card_pb2 as _card_pb2
import finger_pb2 as _finger_pb2
import face_pb2 as _face_pb2
import tna_pb2 as _tna_pb2
import err_pb2 as _err_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIRST_ENUM_VALUE_MUST_BE_ZERO: _ClassVar[Enum]
    MAX_ACCESS_GROUPS: _ClassVar[Enum]
    MAX_JOB_CODES: _ClassVar[Enum]
    MAX_PIN_LENGTH: _ClassVar[Enum]
    MIN_PIN_LENGTH: _ClassVar[Enum]
    MAX_JOB_LABEL_LENGTH: _ClassVar[Enum]
    MAX_NAME_LENGTH: _ClassVar[Enum]

class UserFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_FLAG_NONE: _ClassVar[UserFlag]
    USER_FLAG_CREATED: _ClassVar[UserFlag]
    USER_FLAG_UPDATED: _ClassVar[UserFlag]
    USER_FLAG_DELETED: _ClassVar[UserFlag]
    USER_FLAG_DISABLED: _ClassVar[UserFlag]
    USER_FLAG_ALL: _ClassVar[UserFlag]

class UpdateMask(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEEP_NONE: _ClassVar[UpdateMask]
    KEEP_USER_PHRASE: _ClassVar[UpdateMask]
    KEEP_USER_JOB_CODE: _ClassVar[UpdateMask]
    KEEP_USER_NAME: _ClassVar[UpdateMask]
    KEEP_USER_PHOTO: _ClassVar[UpdateMask]
    KEEP_USER_PIN: _ClassVar[UpdateMask]
    KEEP_USER_CARD: _ClassVar[UpdateMask]
    KEEP_USER_FINGER: _ClassVar[UpdateMask]
    KEEP_USER_FACE: _ClassVar[UpdateMask]
    KEEP_ALL: _ClassVar[UpdateMask]

class SecurityLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SECURITY_LEVEL_LOWEST: _ClassVar[SecurityLevel]
    SECURITY_LEVEL_LOWER: _ClassVar[SecurityLevel]
    SECURITY_LEVEL_LOW: _ClassVar[SecurityLevel]
    SECURITY_LEVEL_NORMAL: _ClassVar[SecurityLevel]
    SECURITY_LEVEL_HIGH: _ClassVar[SecurityLevel]
    SECURITY_LEVEL_HIGHER: _ClassVar[SecurityLevel]

class InfoMask(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_MASK_ID_ONLY: _ClassVar[InfoMask]
    USER_MASK_HDR: _ClassVar[InfoMask]
    USER_MASK_SETTING: _ClassVar[InfoMask]
    USER_MASK_NAME: _ClassVar[InfoMask]
    USER_MASK_PHOTO: _ClassVar[InfoMask]
    USER_MASK_PIN: _ClassVar[InfoMask]
    USER_MASK_CARD: _ClassVar[InfoMask]
    USER_MASK_FINGER: _ClassVar[InfoMask]
    USER_MASK_FACE: _ClassVar[InfoMask]
    USER_MASK_ACCESS_GROUP: _ClassVar[InfoMask]
    USER_MASK_JOB: _ClassVar[InfoMask]
    USER_MASK_PHRASE: _ClassVar[InfoMask]
    USER_MASK_FACE_EX: _ClassVar[InfoMask]
    USER_MASK_SETTING_EX: _ClassVar[InfoMask]
    USER_MASK_ALL: _ClassVar[InfoMask]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
MAX_ACCESS_GROUPS: Enum
MAX_JOB_CODES: Enum
MAX_PIN_LENGTH: Enum
MIN_PIN_LENGTH: Enum
MAX_JOB_LABEL_LENGTH: Enum
MAX_NAME_LENGTH: Enum
USER_FLAG_NONE: UserFlag
USER_FLAG_CREATED: UserFlag
USER_FLAG_UPDATED: UserFlag
USER_FLAG_DELETED: UserFlag
USER_FLAG_DISABLED: UserFlag
USER_FLAG_ALL: UserFlag
KEEP_NONE: UpdateMask
KEEP_USER_PHRASE: UpdateMask
KEEP_USER_JOB_CODE: UpdateMask
KEEP_USER_NAME: UpdateMask
KEEP_USER_PHOTO: UpdateMask
KEEP_USER_PIN: UpdateMask
KEEP_USER_CARD: UpdateMask
KEEP_USER_FINGER: UpdateMask
KEEP_USER_FACE: UpdateMask
KEEP_ALL: UpdateMask
SECURITY_LEVEL_LOWEST: SecurityLevel
SECURITY_LEVEL_LOWER: SecurityLevel
SECURITY_LEVEL_LOW: SecurityLevel
SECURITY_LEVEL_NORMAL: SecurityLevel
SECURITY_LEVEL_HIGH: SecurityLevel
SECURITY_LEVEL_HIGHER: SecurityLevel
USER_MASK_ID_ONLY: InfoMask
USER_MASK_HDR: InfoMask
USER_MASK_SETTING: InfoMask
USER_MASK_NAME: InfoMask
USER_MASK_PHOTO: InfoMask
USER_MASK_PIN: InfoMask
USER_MASK_CARD: InfoMask
USER_MASK_FINGER: InfoMask
USER_MASK_FACE: InfoMask
USER_MASK_ACCESS_GROUP: InfoMask
USER_MASK_JOB: InfoMask
USER_MASK_PHRASE: InfoMask
USER_MASK_FACE_EX: InfoMask
USER_MASK_SETTING_EX: InfoMask
USER_MASK_ALL: InfoMask

class UserHdr(_message.Message):
    __slots__ = ("ID", "userFlag", "numOfCard", "numOfFinger", "numOfFace", "authGroupID", "updateMask")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERFLAG_FIELD_NUMBER: _ClassVar[int]
    NUMOFCARD_FIELD_NUMBER: _ClassVar[int]
    NUMOFFINGER_FIELD_NUMBER: _ClassVar[int]
    NUMOFFACE_FIELD_NUMBER: _ClassVar[int]
    AUTHGROUPID_FIELD_NUMBER: _ClassVar[int]
    UPDATEMASK_FIELD_NUMBER: _ClassVar[int]
    ID: str
    userFlag: int
    numOfCard: int
    numOfFinger: int
    numOfFace: int
    authGroupID: int
    updateMask: int
    def __init__(self, ID: _Optional[str] = ..., userFlag: _Optional[int] = ..., numOfCard: _Optional[int] = ..., numOfFinger: _Optional[int] = ..., numOfFace: _Optional[int] = ..., authGroupID: _Optional[int] = ..., updateMask: _Optional[int] = ...) -> None: ...

class GetListRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetListResponse(_message.Message):
    __slots__ = ("hdrs",)
    HDRS_FIELD_NUMBER: _ClassVar[int]
    hdrs: _containers.RepeatedCompositeFieldContainer[UserHdr]
    def __init__(self, hdrs: _Optional[_Iterable[_Union[UserHdr, _Mapping]]] = ...) -> None: ...

class UserSetting(_message.Message):
    __slots__ = ("startTime", "endTime", "biometricAuthMode", "cardAuthMode", "IDAuthMode", "securityLevel", "faceAuthExtMode", "fingerAuthExtMode", "cardAuthExtMode", "IDAuthExtMode")
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICAUTHMODE_FIELD_NUMBER: _ClassVar[int]
    CARDAUTHMODE_FIELD_NUMBER: _ClassVar[int]
    IDAUTHMODE_FIELD_NUMBER: _ClassVar[int]
    SECURITYLEVEL_FIELD_NUMBER: _ClassVar[int]
    FACEAUTHEXTMODE_FIELD_NUMBER: _ClassVar[int]
    FINGERAUTHEXTMODE_FIELD_NUMBER: _ClassVar[int]
    CARDAUTHEXTMODE_FIELD_NUMBER: _ClassVar[int]
    IDAUTHEXTMODE_FIELD_NUMBER: _ClassVar[int]
    startTime: int
    endTime: int
    biometricAuthMode: int
    cardAuthMode: int
    IDAuthMode: int
    securityLevel: SecurityLevel
    faceAuthExtMode: int
    fingerAuthExtMode: int
    cardAuthExtMode: int
    IDAuthExtMode: int
    def __init__(self, startTime: _Optional[int] = ..., endTime: _Optional[int] = ..., biometricAuthMode: _Optional[int] = ..., cardAuthMode: _Optional[int] = ..., IDAuthMode: _Optional[int] = ..., securityLevel: _Optional[_Union[SecurityLevel, str]] = ..., faceAuthExtMode: _Optional[int] = ..., fingerAuthExtMode: _Optional[int] = ..., cardAuthExtMode: _Optional[int] = ..., IDAuthExtMode: _Optional[int] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ("hdr", "setting", "name", "cards", "fingers", "faces", "accessGroupIDs", "jobCodes", "PIN", "photo")
    HDR_FIELD_NUMBER: _ClassVar[int]
    SETTING_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CARDS_FIELD_NUMBER: _ClassVar[int]
    FINGERS_FIELD_NUMBER: _ClassVar[int]
    FACES_FIELD_NUMBER: _ClassVar[int]
    ACCESSGROUPIDS_FIELD_NUMBER: _ClassVar[int]
    JOBCODES_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    hdr: UserHdr
    setting: UserSetting
    name: str
    cards: _containers.RepeatedCompositeFieldContainer[_card_pb2.CSNCardData]
    fingers: _containers.RepeatedCompositeFieldContainer[_finger_pb2.FingerData]
    faces: _containers.RepeatedCompositeFieldContainer[_face_pb2.FaceData]
    accessGroupIDs: _containers.RepeatedScalarFieldContainer[int]
    jobCodes: _containers.RepeatedCompositeFieldContainer[_tna_pb2.JobCode]
    PIN: bytes
    photo: bytes
    def __init__(self, hdr: _Optional[_Union[UserHdr, _Mapping]] = ..., setting: _Optional[_Union[UserSetting, _Mapping]] = ..., name: _Optional[str] = ..., cards: _Optional[_Iterable[_Union[_card_pb2.CSNCardData, _Mapping]]] = ..., fingers: _Optional[_Iterable[_Union[_finger_pb2.FingerData, _Mapping]]] = ..., faces: _Optional[_Iterable[_Union[_face_pb2.FaceData, _Mapping]]] = ..., accessGroupIDs: _Optional[_Iterable[int]] = ..., jobCodes: _Optional[_Iterable[_Union[_tna_pb2.JobCode, _Mapping]]] = ..., PIN: _Optional[bytes] = ..., photo: _Optional[bytes] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("deviceID", "userIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    userIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, deviceID: _Optional[int] = ..., userIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[UserInfo]
    def __init__(self, users: _Optional[_Iterable[_Union[UserInfo, _Mapping]]] = ...) -> None: ...

class GetPartialRequest(_message.Message):
    __slots__ = ("deviceID", "userIDs", "infoMask")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    INFOMASK_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    userIDs: _containers.RepeatedScalarFieldContainer[str]
    infoMask: int
    def __init__(self, deviceID: _Optional[int] = ..., userIDs: _Optional[_Iterable[str]] = ..., infoMask: _Optional[int] = ...) -> None: ...

class GetPartialResponse(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[UserInfo]
    def __init__(self, users: _Optional[_Iterable[_Union[UserInfo, _Mapping]]] = ...) -> None: ...

class EnrollRequest(_message.Message):
    __slots__ = ("deviceID", "users", "overwrite")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    users: _containers.RepeatedCompositeFieldContainer[UserInfo]
    overwrite: bool
    def __init__(self, deviceID: _Optional[int] = ..., users: _Optional[_Iterable[_Union[UserInfo, _Mapping]]] = ..., overwrite: bool = ...) -> None: ...

class EnrollResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnrollMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "users", "overwrite")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    users: _containers.RepeatedCompositeFieldContainer[UserInfo]
    overwrite: bool
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., users: _Optional[_Iterable[_Union[UserInfo, _Mapping]]] = ..., overwrite: bool = ...) -> None: ...

class EnrollMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("deviceID", "users")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    users: _containers.RepeatedCompositeFieldContainer[UserInfo]
    def __init__(self, deviceID: _Optional[int] = ..., users: _Optional[_Iterable[_Union[UserInfo, _Mapping]]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "users")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    users: _containers.RepeatedCompositeFieldContainer[UserInfo]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., users: _Optional[_Iterable[_Union[UserInfo, _Mapping]]] = ...) -> None: ...

class UpdateMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("deviceID", "userIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    userIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, deviceID: _Optional[int] = ..., userIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "userIDs")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    userIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., userIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteAllRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class DeleteAllResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAllMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteAllMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class UserCard(_message.Message):
    __slots__ = ("userID", "cards")
    USERID_FIELD_NUMBER: _ClassVar[int]
    CARDS_FIELD_NUMBER: _ClassVar[int]
    userID: str
    cards: _containers.RepeatedCompositeFieldContainer[_card_pb2.CSNCardData]
    def __init__(self, userID: _Optional[str] = ..., cards: _Optional[_Iterable[_Union[_card_pb2.CSNCardData, _Mapping]]] = ...) -> None: ...

class GetCardRequest(_message.Message):
    __slots__ = ("deviceID", "userIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    userIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, deviceID: _Optional[int] = ..., userIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class GetCardResponse(_message.Message):
    __slots__ = ("userCards",)
    USERCARDS_FIELD_NUMBER: _ClassVar[int]
    userCards: _containers.RepeatedCompositeFieldContainer[UserCard]
    def __init__(self, userCards: _Optional[_Iterable[_Union[UserCard, _Mapping]]] = ...) -> None: ...

class SetCardRequest(_message.Message):
    __slots__ = ("deviceID", "userCards")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERCARDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    userCards: _containers.RepeatedCompositeFieldContainer[UserCard]
    def __init__(self, deviceID: _Optional[int] = ..., userCards: _Optional[_Iterable[_Union[UserCard, _Mapping]]] = ...) -> None: ...

class SetCardResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetCardMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "userCards")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    USERCARDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    userCards: _containers.RepeatedCompositeFieldContainer[UserCard]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., userCards: _Optional[_Iterable[_Union[UserCard, _Mapping]]] = ...) -> None: ...

class SetCardMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class UserFinger(_message.Message):
    __slots__ = ("userID", "fingers")
    USERID_FIELD_NUMBER: _ClassVar[int]
    FINGERS_FIELD_NUMBER: _ClassVar[int]
    userID: str
    fingers: _containers.RepeatedCompositeFieldContainer[_finger_pb2.FingerData]
    def __init__(self, userID: _Optional[str] = ..., fingers: _Optional[_Iterable[_Union[_finger_pb2.FingerData, _Mapping]]] = ...) -> None: ...

class GetFingerRequest(_message.Message):
    __slots__ = ("deviceID", "userIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    userIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, deviceID: _Optional[int] = ..., userIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class GetFingerResponse(_message.Message):
    __slots__ = ("userFingers",)
    USERFINGERS_FIELD_NUMBER: _ClassVar[int]
    userFingers: _containers.RepeatedCompositeFieldContainer[UserFinger]
    def __init__(self, userFingers: _Optional[_Iterable[_Union[UserFinger, _Mapping]]] = ...) -> None: ...

class SetFingerRequest(_message.Message):
    __slots__ = ("deviceID", "userFingers")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERFINGERS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    userFingers: _containers.RepeatedCompositeFieldContainer[UserFinger]
    def __init__(self, deviceID: _Optional[int] = ..., userFingers: _Optional[_Iterable[_Union[UserFinger, _Mapping]]] = ...) -> None: ...

class SetFingerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetFingerMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "userFingers")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    USERFINGERS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    userFingers: _containers.RepeatedCompositeFieldContainer[UserFinger]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., userFingers: _Optional[_Iterable[_Union[UserFinger, _Mapping]]] = ...) -> None: ...

class SetFingerMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class UserFace(_message.Message):
    __slots__ = ("userID", "faces")
    USERID_FIELD_NUMBER: _ClassVar[int]
    FACES_FIELD_NUMBER: _ClassVar[int]
    userID: str
    faces: _containers.RepeatedCompositeFieldContainer[_face_pb2.FaceData]
    def __init__(self, userID: _Optional[str] = ..., faces: _Optional[_Iterable[_Union[_face_pb2.FaceData, _Mapping]]] = ...) -> None: ...

class GetFaceRequest(_message.Message):
    __slots__ = ("deviceID", "userIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    userIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, deviceID: _Optional[int] = ..., userIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class GetFaceResponse(_message.Message):
    __slots__ = ("userFaces",)
    USERFACES_FIELD_NUMBER: _ClassVar[int]
    userFaces: _containers.RepeatedCompositeFieldContainer[UserFace]
    def __init__(self, userFaces: _Optional[_Iterable[_Union[UserFace, _Mapping]]] = ...) -> None: ...

class SetFaceRequest(_message.Message):
    __slots__ = ("deviceID", "userFaces")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERFACES_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    userFaces: _containers.RepeatedCompositeFieldContainer[UserFace]
    def __init__(self, deviceID: _Optional[int] = ..., userFaces: _Optional[_Iterable[_Union[UserFace, _Mapping]]] = ...) -> None: ...

class SetFaceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetFaceMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "userFaces")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    USERFACES_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    userFaces: _containers.RepeatedCompositeFieldContainer[UserFace]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., userFaces: _Optional[_Iterable[_Union[UserFace, _Mapping]]] = ...) -> None: ...

class SetFaceMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class UserAccessGroup(_message.Message):
    __slots__ = ("userID", "accessGroupIDs")
    USERID_FIELD_NUMBER: _ClassVar[int]
    ACCESSGROUPIDS_FIELD_NUMBER: _ClassVar[int]
    userID: str
    accessGroupIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, userID: _Optional[str] = ..., accessGroupIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class GetAccessGroupRequest(_message.Message):
    __slots__ = ("deviceID", "userIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    userIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, deviceID: _Optional[int] = ..., userIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class GetAccessGroupResponse(_message.Message):
    __slots__ = ("userAccessGroups",)
    USERACCESSGROUPS_FIELD_NUMBER: _ClassVar[int]
    userAccessGroups: _containers.RepeatedCompositeFieldContainer[UserAccessGroup]
    def __init__(self, userAccessGroups: _Optional[_Iterable[_Union[UserAccessGroup, _Mapping]]] = ...) -> None: ...

class SetAccessGroupRequest(_message.Message):
    __slots__ = ("deviceID", "userAccessGroups")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERACCESSGROUPS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    userAccessGroups: _containers.RepeatedCompositeFieldContainer[UserAccessGroup]
    def __init__(self, deviceID: _Optional[int] = ..., userAccessGroups: _Optional[_Iterable[_Union[UserAccessGroup, _Mapping]]] = ...) -> None: ...

class SetAccessGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetAccessGroupMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "userAccessGroups")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    USERACCESSGROUPS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    userAccessGroups: _containers.RepeatedCompositeFieldContainer[UserAccessGroup]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., userAccessGroups: _Optional[_Iterable[_Union[UserAccessGroup, _Mapping]]] = ...) -> None: ...

class SetAccessGroupMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class UserJobCode(_message.Message):
    __slots__ = ("userID", "jobCodes")
    USERID_FIELD_NUMBER: _ClassVar[int]
    JOBCODES_FIELD_NUMBER: _ClassVar[int]
    userID: str
    jobCodes: _containers.RepeatedCompositeFieldContainer[_tna_pb2.JobCode]
    def __init__(self, userID: _Optional[str] = ..., jobCodes: _Optional[_Iterable[_Union[_tna_pb2.JobCode, _Mapping]]] = ...) -> None: ...

class GetJobCodeRequest(_message.Message):
    __slots__ = ("deviceID", "userIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    userIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, deviceID: _Optional[int] = ..., userIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class GetJobCodeResponse(_message.Message):
    __slots__ = ("userJobCodes",)
    USERJOBCODES_FIELD_NUMBER: _ClassVar[int]
    userJobCodes: _containers.RepeatedCompositeFieldContainer[UserJobCode]
    def __init__(self, userJobCodes: _Optional[_Iterable[_Union[UserJobCode, _Mapping]]] = ...) -> None: ...

class SetJobCodeRequest(_message.Message):
    __slots__ = ("deviceID", "userJobCodes")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERJOBCODES_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    userJobCodes: _containers.RepeatedCompositeFieldContainer[UserJobCode]
    def __init__(self, deviceID: _Optional[int] = ..., userJobCodes: _Optional[_Iterable[_Union[UserJobCode, _Mapping]]] = ...) -> None: ...

class SetJobCodeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetJobCodeMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "userJobCodes")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    USERJOBCODES_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    userJobCodes: _containers.RepeatedCompositeFieldContainer[UserJobCode]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., userJobCodes: _Optional[_Iterable[_Union[UserJobCode, _Mapping]]] = ...) -> None: ...

class SetJobCodeMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class GetPINHashRequest(_message.Message):
    __slots__ = ("PIN",)
    PIN_FIELD_NUMBER: _ClassVar[int]
    PIN: str
    def __init__(self, PIN: _Optional[str] = ...) -> None: ...

class GetPINHashResponse(_message.Message):
    __slots__ = ("hashVal",)
    HASHVAL_FIELD_NUMBER: _ClassVar[int]
    hashVal: bytes
    def __init__(self, hashVal: _Optional[bytes] = ...) -> None: ...

class GetPINHashWithKeyRequest(_message.Message):
    __slots__ = ("PIN", "hashKey")
    PIN_FIELD_NUMBER: _ClassVar[int]
    HASHKEY_FIELD_NUMBER: _ClassVar[int]
    PIN: str
    hashKey: bytes
    def __init__(self, PIN: _Optional[str] = ..., hashKey: _Optional[bytes] = ...) -> None: ...

class GetStatisticRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class UserStatistic(_message.Message):
    __slots__ = ("numOfUsers", "numOfCards", "numOfFingerprints", "numOfFaces", "numOfNames", "numOfImages", "numOfPhrases")
    NUMOFUSERS_FIELD_NUMBER: _ClassVar[int]
    NUMOFCARDS_FIELD_NUMBER: _ClassVar[int]
    NUMOFFINGERPRINTS_FIELD_NUMBER: _ClassVar[int]
    NUMOFFACES_FIELD_NUMBER: _ClassVar[int]
    NUMOFNAMES_FIELD_NUMBER: _ClassVar[int]
    NUMOFIMAGES_FIELD_NUMBER: _ClassVar[int]
    NUMOFPHRASES_FIELD_NUMBER: _ClassVar[int]
    numOfUsers: int
    numOfCards: int
    numOfFingerprints: int
    numOfFaces: int
    numOfNames: int
    numOfImages: int
    numOfPhrases: int
    def __init__(self, numOfUsers: _Optional[int] = ..., numOfCards: _Optional[int] = ..., numOfFingerprints: _Optional[int] = ..., numOfFaces: _Optional[int] = ..., numOfNames: _Optional[int] = ..., numOfImages: _Optional[int] = ..., numOfPhrases: _Optional[int] = ...) -> None: ...

class GetStatisticResponse(_message.Message):
    __slots__ = ("userStatistic",)
    USERSTATISTIC_FIELD_NUMBER: _ClassVar[int]
    userStatistic: UserStatistic
    def __init__(self, userStatistic: _Optional[_Union[UserStatistic, _Mapping]] = ...) -> None: ...

class UserOverride(_message.Message):
    __slots__ = ("userID", "useExtendedDoorOpenTime")
    USERID_FIELD_NUMBER: _ClassVar[int]
    USEEXTENDEDDOOROPENTIME_FIELD_NUMBER: _ClassVar[int]
    userID: str
    useExtendedDoorOpenTime: bool
    def __init__(self, userID: _Optional[str] = ..., useExtendedDoorOpenTime: bool = ...) -> None: ...

class GetUserOverrideRequest(_message.Message):
    __slots__ = ("deviceID", "userIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    userIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, deviceID: _Optional[int] = ..., userIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class GetUserOverrideResponse(_message.Message):
    __slots__ = ("userOverrides",)
    USEROVERRIDES_FIELD_NUMBER: _ClassVar[int]
    userOverrides: _containers.RepeatedCompositeFieldContainer[UserOverride]
    def __init__(self, userOverrides: _Optional[_Iterable[_Union[UserOverride, _Mapping]]] = ...) -> None: ...

class GetAllUserOverrideRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetAllUserOverrideResponse(_message.Message):
    __slots__ = ("userOverrides",)
    USEROVERRIDES_FIELD_NUMBER: _ClassVar[int]
    userOverrides: _containers.RepeatedCompositeFieldContainer[UserOverride]
    def __init__(self, userOverrides: _Optional[_Iterable[_Union[UserOverride, _Mapping]]] = ...) -> None: ...

class SetUserOverrideRequest(_message.Message):
    __slots__ = ("deviceID", "userOverrides")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USEROVERRIDES_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    userOverrides: _containers.RepeatedCompositeFieldContainer[UserOverride]
    def __init__(self, deviceID: _Optional[int] = ..., userOverrides: _Optional[_Iterable[_Union[UserOverride, _Mapping]]] = ...) -> None: ...

class SetUserOverrideResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetUserOverrideMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "userOverrides")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    USEROVERRIDES_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    userOverrides: _containers.RepeatedCompositeFieldContainer[UserOverride]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., userOverrides: _Optional[_Iterable[_Union[UserOverride, _Mapping]]] = ...) -> None: ...

class SetUserOverrideMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteUserOverrideRequest(_message.Message):
    __slots__ = ("deviceID", "userIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    userIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, deviceID: _Optional[int] = ..., userIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteUserOverrideResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteUserOverrideMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "userIDs")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    userIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., userIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteUserOverrideMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteAllUserOverrideRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class DeleteAllUserOverrideResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAllUserOverrideMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteAllUserOverrideMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...
