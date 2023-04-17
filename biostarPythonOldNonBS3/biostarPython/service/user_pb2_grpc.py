# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from biostarPython.service import user_pb2 as user__pb2


class UserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetList = channel.unary_unary(
                '/user.User/GetList',
                request_serializer=user__pb2.GetListRequest.SerializeToString,
                response_deserializer=user__pb2.GetListResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/user.User/Get',
                request_serializer=user__pb2.GetRequest.SerializeToString,
                response_deserializer=user__pb2.GetResponse.FromString,
                )
        self.GetPartial = channel.unary_unary(
                '/user.User/GetPartial',
                request_serializer=user__pb2.GetPartialRequest.SerializeToString,
                response_deserializer=user__pb2.GetPartialResponse.FromString,
                )
        self.Enroll = channel.unary_unary(
                '/user.User/Enroll',
                request_serializer=user__pb2.EnrollRequest.SerializeToString,
                response_deserializer=user__pb2.EnrollResponse.FromString,
                )
        self.EnrollMulti = channel.unary_unary(
                '/user.User/EnrollMulti',
                request_serializer=user__pb2.EnrollMultiRequest.SerializeToString,
                response_deserializer=user__pb2.EnrollMultiResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/user.User/Delete',
                request_serializer=user__pb2.DeleteRequest.SerializeToString,
                response_deserializer=user__pb2.DeleteResponse.FromString,
                )
        self.DeleteMulti = channel.unary_unary(
                '/user.User/DeleteMulti',
                request_serializer=user__pb2.DeleteMultiRequest.SerializeToString,
                response_deserializer=user__pb2.DeleteMultiResponse.FromString,
                )
        self.DeleteAll = channel.unary_unary(
                '/user.User/DeleteAll',
                request_serializer=user__pb2.DeleteAllRequest.SerializeToString,
                response_deserializer=user__pb2.DeleteAllResponse.FromString,
                )
        self.DeleteAllMulti = channel.unary_unary(
                '/user.User/DeleteAllMulti',
                request_serializer=user__pb2.DeleteAllMultiRequest.SerializeToString,
                response_deserializer=user__pb2.DeleteAllMultiResponse.FromString,
                )
        self.GetCard = channel.unary_unary(
                '/user.User/GetCard',
                request_serializer=user__pb2.GetCardRequest.SerializeToString,
                response_deserializer=user__pb2.GetCardResponse.FromString,
                )
        self.SetCard = channel.unary_unary(
                '/user.User/SetCard',
                request_serializer=user__pb2.SetCardRequest.SerializeToString,
                response_deserializer=user__pb2.SetCardResponse.FromString,
                )
        self.SetCardMulti = channel.unary_unary(
                '/user.User/SetCardMulti',
                request_serializer=user__pb2.SetCardMultiRequest.SerializeToString,
                response_deserializer=user__pb2.SetCardMultiResponse.FromString,
                )
        self.GetFinger = channel.unary_unary(
                '/user.User/GetFinger',
                request_serializer=user__pb2.GetFingerRequest.SerializeToString,
                response_deserializer=user__pb2.GetFingerResponse.FromString,
                )
        self.SetFinger = channel.unary_unary(
                '/user.User/SetFinger',
                request_serializer=user__pb2.SetFingerRequest.SerializeToString,
                response_deserializer=user__pb2.SetFingerResponse.FromString,
                )
        self.SetFingerMulti = channel.unary_unary(
                '/user.User/SetFingerMulti',
                request_serializer=user__pb2.SetFingerMultiRequest.SerializeToString,
                response_deserializer=user__pb2.SetFingerMultiResponse.FromString,
                )
        self.GetFace = channel.unary_unary(
                '/user.User/GetFace',
                request_serializer=user__pb2.GetFaceRequest.SerializeToString,
                response_deserializer=user__pb2.GetFaceResponse.FromString,
                )
        self.SetFace = channel.unary_unary(
                '/user.User/SetFace',
                request_serializer=user__pb2.SetFaceRequest.SerializeToString,
                response_deserializer=user__pb2.SetFaceResponse.FromString,
                )
        self.SetFaceMulti = channel.unary_unary(
                '/user.User/SetFaceMulti',
                request_serializer=user__pb2.SetFaceMultiRequest.SerializeToString,
                response_deserializer=user__pb2.SetFaceMultiResponse.FromString,
                )
        self.GetAccessGroup = channel.unary_unary(
                '/user.User/GetAccessGroup',
                request_serializer=user__pb2.GetAccessGroupRequest.SerializeToString,
                response_deserializer=user__pb2.GetAccessGroupResponse.FromString,
                )
        self.SetAccessGroup = channel.unary_unary(
                '/user.User/SetAccessGroup',
                request_serializer=user__pb2.SetAccessGroupRequest.SerializeToString,
                response_deserializer=user__pb2.SetAccessGroupResponse.FromString,
                )
        self.SetAccessGroupMulti = channel.unary_unary(
                '/user.User/SetAccessGroupMulti',
                request_serializer=user__pb2.SetAccessGroupMultiRequest.SerializeToString,
                response_deserializer=user__pb2.SetAccessGroupMultiResponse.FromString,
                )
        self.GetJobCode = channel.unary_unary(
                '/user.User/GetJobCode',
                request_serializer=user__pb2.GetJobCodeRequest.SerializeToString,
                response_deserializer=user__pb2.GetJobCodeResponse.FromString,
                )
        self.SetJobCode = channel.unary_unary(
                '/user.User/SetJobCode',
                request_serializer=user__pb2.SetJobCodeRequest.SerializeToString,
                response_deserializer=user__pb2.SetJobCodeResponse.FromString,
                )
        self.SetJobCodeMulti = channel.unary_unary(
                '/user.User/SetJobCodeMulti',
                request_serializer=user__pb2.SetJobCodeMultiRequest.SerializeToString,
                response_deserializer=user__pb2.SetJobCodeMultiResponse.FromString,
                )
        self.GetPINHash = channel.unary_unary(
                '/user.User/GetPINHash',
                request_serializer=user__pb2.GetPINHashRequest.SerializeToString,
                response_deserializer=user__pb2.GetPINHashResponse.FromString,
                )


class UserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPartial(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Enroll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnrollMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAllMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCard(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCard(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCardMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFinger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetFinger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetFingerMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetFace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetFaceMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAccessGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAccessGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAccessGroupMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJobCode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetJobCode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetJobCodeMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPINHash(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetList,
                    request_deserializer=user__pb2.GetListRequest.FromString,
                    response_serializer=user__pb2.GetListResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=user__pb2.GetRequest.FromString,
                    response_serializer=user__pb2.GetResponse.SerializeToString,
            ),
            'GetPartial': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPartial,
                    request_deserializer=user__pb2.GetPartialRequest.FromString,
                    response_serializer=user__pb2.GetPartialResponse.SerializeToString,
            ),
            'Enroll': grpc.unary_unary_rpc_method_handler(
                    servicer.Enroll,
                    request_deserializer=user__pb2.EnrollRequest.FromString,
                    response_serializer=user__pb2.EnrollResponse.SerializeToString,
            ),
            'EnrollMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.EnrollMulti,
                    request_deserializer=user__pb2.EnrollMultiRequest.FromString,
                    response_serializer=user__pb2.EnrollMultiResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=user__pb2.DeleteRequest.FromString,
                    response_serializer=user__pb2.DeleteResponse.SerializeToString,
            ),
            'DeleteMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteMulti,
                    request_deserializer=user__pb2.DeleteMultiRequest.FromString,
                    response_serializer=user__pb2.DeleteMultiResponse.SerializeToString,
            ),
            'DeleteAll': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAll,
                    request_deserializer=user__pb2.DeleteAllRequest.FromString,
                    response_serializer=user__pb2.DeleteAllResponse.SerializeToString,
            ),
            'DeleteAllMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAllMulti,
                    request_deserializer=user__pb2.DeleteAllMultiRequest.FromString,
                    response_serializer=user__pb2.DeleteAllMultiResponse.SerializeToString,
            ),
            'GetCard': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCard,
                    request_deserializer=user__pb2.GetCardRequest.FromString,
                    response_serializer=user__pb2.GetCardResponse.SerializeToString,
            ),
            'SetCard': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCard,
                    request_deserializer=user__pb2.SetCardRequest.FromString,
                    response_serializer=user__pb2.SetCardResponse.SerializeToString,
            ),
            'SetCardMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCardMulti,
                    request_deserializer=user__pb2.SetCardMultiRequest.FromString,
                    response_serializer=user__pb2.SetCardMultiResponse.SerializeToString,
            ),
            'GetFinger': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFinger,
                    request_deserializer=user__pb2.GetFingerRequest.FromString,
                    response_serializer=user__pb2.GetFingerResponse.SerializeToString,
            ),
            'SetFinger': grpc.unary_unary_rpc_method_handler(
                    servicer.SetFinger,
                    request_deserializer=user__pb2.SetFingerRequest.FromString,
                    response_serializer=user__pb2.SetFingerResponse.SerializeToString,
            ),
            'SetFingerMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.SetFingerMulti,
                    request_deserializer=user__pb2.SetFingerMultiRequest.FromString,
                    response_serializer=user__pb2.SetFingerMultiResponse.SerializeToString,
            ),
            'GetFace': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFace,
                    request_deserializer=user__pb2.GetFaceRequest.FromString,
                    response_serializer=user__pb2.GetFaceResponse.SerializeToString,
            ),
            'SetFace': grpc.unary_unary_rpc_method_handler(
                    servicer.SetFace,
                    request_deserializer=user__pb2.SetFaceRequest.FromString,
                    response_serializer=user__pb2.SetFaceResponse.SerializeToString,
            ),
            'SetFaceMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.SetFaceMulti,
                    request_deserializer=user__pb2.SetFaceMultiRequest.FromString,
                    response_serializer=user__pb2.SetFaceMultiResponse.SerializeToString,
            ),
            'GetAccessGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccessGroup,
                    request_deserializer=user__pb2.GetAccessGroupRequest.FromString,
                    response_serializer=user__pb2.GetAccessGroupResponse.SerializeToString,
            ),
            'SetAccessGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAccessGroup,
                    request_deserializer=user__pb2.SetAccessGroupRequest.FromString,
                    response_serializer=user__pb2.SetAccessGroupResponse.SerializeToString,
            ),
            'SetAccessGroupMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAccessGroupMulti,
                    request_deserializer=user__pb2.SetAccessGroupMultiRequest.FromString,
                    response_serializer=user__pb2.SetAccessGroupMultiResponse.SerializeToString,
            ),
            'GetJobCode': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJobCode,
                    request_deserializer=user__pb2.GetJobCodeRequest.FromString,
                    response_serializer=user__pb2.GetJobCodeResponse.SerializeToString,
            ),
            'SetJobCode': grpc.unary_unary_rpc_method_handler(
                    servicer.SetJobCode,
                    request_deserializer=user__pb2.SetJobCodeRequest.FromString,
                    response_serializer=user__pb2.SetJobCodeResponse.SerializeToString,
            ),
            'SetJobCodeMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.SetJobCodeMulti,
                    request_deserializer=user__pb2.SetJobCodeMultiRequest.FromString,
                    response_serializer=user__pb2.SetJobCodeMultiResponse.SerializeToString,
            ),
            'GetPINHash': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPINHash,
                    request_deserializer=user__pb2.GetPINHashRequest.FromString,
                    response_serializer=user__pb2.GetPINHashResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.User', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class User(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/GetList',
            user__pb2.GetListRequest.SerializeToString,
            user__pb2.GetListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/Get',
            user__pb2.GetRequest.SerializeToString,
            user__pb2.GetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPartial(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/GetPartial',
            user__pb2.GetPartialRequest.SerializeToString,
            user__pb2.GetPartialResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Enroll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/Enroll',
            user__pb2.EnrollRequest.SerializeToString,
            user__pb2.EnrollResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnrollMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/EnrollMulti',
            user__pb2.EnrollMultiRequest.SerializeToString,
            user__pb2.EnrollMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/Delete',
            user__pb2.DeleteRequest.SerializeToString,
            user__pb2.DeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/DeleteMulti',
            user__pb2.DeleteMultiRequest.SerializeToString,
            user__pb2.DeleteMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/DeleteAll',
            user__pb2.DeleteAllRequest.SerializeToString,
            user__pb2.DeleteAllResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAllMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/DeleteAllMulti',
            user__pb2.DeleteAllMultiRequest.SerializeToString,
            user__pb2.DeleteAllMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCard(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/GetCard',
            user__pb2.GetCardRequest.SerializeToString,
            user__pb2.GetCardResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetCard(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/SetCard',
            user__pb2.SetCardRequest.SerializeToString,
            user__pb2.SetCardResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetCardMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/SetCardMulti',
            user__pb2.SetCardMultiRequest.SerializeToString,
            user__pb2.SetCardMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFinger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/GetFinger',
            user__pb2.GetFingerRequest.SerializeToString,
            user__pb2.GetFingerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetFinger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/SetFinger',
            user__pb2.SetFingerRequest.SerializeToString,
            user__pb2.SetFingerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetFingerMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/SetFingerMulti',
            user__pb2.SetFingerMultiRequest.SerializeToString,
            user__pb2.SetFingerMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/GetFace',
            user__pb2.GetFaceRequest.SerializeToString,
            user__pb2.GetFaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetFace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/SetFace',
            user__pb2.SetFaceRequest.SerializeToString,
            user__pb2.SetFaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetFaceMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/SetFaceMulti',
            user__pb2.SetFaceMultiRequest.SerializeToString,
            user__pb2.SetFaceMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAccessGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/GetAccessGroup',
            user__pb2.GetAccessGroupRequest.SerializeToString,
            user__pb2.GetAccessGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAccessGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/SetAccessGroup',
            user__pb2.SetAccessGroupRequest.SerializeToString,
            user__pb2.SetAccessGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAccessGroupMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/SetAccessGroupMulti',
            user__pb2.SetAccessGroupMultiRequest.SerializeToString,
            user__pb2.SetAccessGroupMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetJobCode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/GetJobCode',
            user__pb2.GetJobCodeRequest.SerializeToString,
            user__pb2.GetJobCodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetJobCode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/SetJobCode',
            user__pb2.SetJobCodeRequest.SerializeToString,
            user__pb2.SetJobCodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetJobCodeMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/SetJobCodeMulti',
            user__pb2.SetJobCodeMultiRequest.SerializeToString,
            user__pb2.SetJobCodeMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPINHash(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/GetPINHash',
            user__pb2.GetPINHashRequest.SerializeToString,
            user__pb2.GetPINHashResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)