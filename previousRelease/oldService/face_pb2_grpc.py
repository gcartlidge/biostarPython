# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from biostarPython.service import face_pb2 as face__pb2


class FaceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Scan = channel.unary_unary(
                '/gsdk.face.Face/Scan',
                request_serializer=face__pb2.ScanRequest.SerializeToString,
                response_deserializer=face__pb2.ScanResponse.FromString,
                )
        self.Extract = channel.unary_unary(
                '/gsdk.face.Face/Extract',
                request_serializer=face__pb2.ExtractRequest.SerializeToString,
                response_deserializer=face__pb2.ExtractResponse.FromString,
                )
        self.Normalize = channel.unary_unary(
                '/gsdk.face.Face/Normalize',
                request_serializer=face__pb2.NormalizeRequest.SerializeToString,
                response_deserializer=face__pb2.NormalizeResponse.FromString,
                )
        self.GetConfig = channel.unary_unary(
                '/gsdk.face.Face/GetConfig',
                request_serializer=face__pb2.GetConfigRequest.SerializeToString,
                response_deserializer=face__pb2.GetConfigResponse.FromString,
                )
        self.SetConfig = channel.unary_unary(
                '/gsdk.face.Face/SetConfig',
                request_serializer=face__pb2.SetConfigRequest.SerializeToString,
                response_deserializer=face__pb2.SetConfigResponse.FromString,
                )
        self.SetConfigMulti = channel.unary_unary(
                '/gsdk.face.Face/SetConfigMulti',
                request_serializer=face__pb2.SetConfigMultiRequest.SerializeToString,
                response_deserializer=face__pb2.SetConfigMultiResponse.FromString,
                )
        self.GetAuthGroup = channel.unary_unary(
                '/gsdk.face.Face/GetAuthGroup',
                request_serializer=face__pb2.GetAuthGroupRequest.SerializeToString,
                response_deserializer=face__pb2.GetAuthGroupResponse.FromString,
                )
        self.AddAuthGroup = channel.unary_unary(
                '/gsdk.face.Face/AddAuthGroup',
                request_serializer=face__pb2.AddAuthGroupRequest.SerializeToString,
                response_deserializer=face__pb2.AddAuthGroupResponse.FromString,
                )
        self.AddAuthGroupMulti = channel.unary_unary(
                '/gsdk.face.Face/AddAuthGroupMulti',
                request_serializer=face__pb2.AddAuthGroupMultiRequest.SerializeToString,
                response_deserializer=face__pb2.AddAuthGroupMultiResponse.FromString,
                )
        self.DeleteAuthGroup = channel.unary_unary(
                '/gsdk.face.Face/DeleteAuthGroup',
                request_serializer=face__pb2.DeleteAuthGroupRequest.SerializeToString,
                response_deserializer=face__pb2.DeleteAuthGroupResponse.FromString,
                )
        self.DeleteAuthGroupMulti = channel.unary_unary(
                '/gsdk.face.Face/DeleteAuthGroupMulti',
                request_serializer=face__pb2.DeleteAuthGroupMultiRequest.SerializeToString,
                response_deserializer=face__pb2.DeleteAuthGroupMultiResponse.FromString,
                )
        self.DeleteAllAuthGroup = channel.unary_unary(
                '/gsdk.face.Face/DeleteAllAuthGroup',
                request_serializer=face__pb2.DeleteAllAuthGroupRequest.SerializeToString,
                response_deserializer=face__pb2.DeleteAllAuthGroupResponse.FromString,
                )
        self.DeleteAllAuthGroupMulti = channel.unary_unary(
                '/gsdk.face.Face/DeleteAllAuthGroupMulti',
                request_serializer=face__pb2.DeleteAllAuthGroupMultiRequest.SerializeToString,
                response_deserializer=face__pb2.DeleteAllAuthGroupMultiResponse.FromString,
                )


class FaceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Scan(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Extract(self, request, context):
        """F2 and BS3 only
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Normalize(self, request, context):
        """F2 and BS3 only
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetConfigMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAuthGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddAuthGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddAuthGroupMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAuthGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAuthGroupMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAllAuthGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAllAuthGroupMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FaceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Scan': grpc.unary_unary_rpc_method_handler(
                    servicer.Scan,
                    request_deserializer=face__pb2.ScanRequest.FromString,
                    response_serializer=face__pb2.ScanResponse.SerializeToString,
            ),
            'Extract': grpc.unary_unary_rpc_method_handler(
                    servicer.Extract,
                    request_deserializer=face__pb2.ExtractRequest.FromString,
                    response_serializer=face__pb2.ExtractResponse.SerializeToString,
            ),
            'Normalize': grpc.unary_unary_rpc_method_handler(
                    servicer.Normalize,
                    request_deserializer=face__pb2.NormalizeRequest.FromString,
                    response_serializer=face__pb2.NormalizeResponse.SerializeToString,
            ),
            'GetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConfig,
                    request_deserializer=face__pb2.GetConfigRequest.FromString,
                    response_serializer=face__pb2.GetConfigResponse.SerializeToString,
            ),
            'SetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfig,
                    request_deserializer=face__pb2.SetConfigRequest.FromString,
                    response_serializer=face__pb2.SetConfigResponse.SerializeToString,
            ),
            'SetConfigMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfigMulti,
                    request_deserializer=face__pb2.SetConfigMultiRequest.FromString,
                    response_serializer=face__pb2.SetConfigMultiResponse.SerializeToString,
            ),
            'GetAuthGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAuthGroup,
                    request_deserializer=face__pb2.GetAuthGroupRequest.FromString,
                    response_serializer=face__pb2.GetAuthGroupResponse.SerializeToString,
            ),
            'AddAuthGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.AddAuthGroup,
                    request_deserializer=face__pb2.AddAuthGroupRequest.FromString,
                    response_serializer=face__pb2.AddAuthGroupResponse.SerializeToString,
            ),
            'AddAuthGroupMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.AddAuthGroupMulti,
                    request_deserializer=face__pb2.AddAuthGroupMultiRequest.FromString,
                    response_serializer=face__pb2.AddAuthGroupMultiResponse.SerializeToString,
            ),
            'DeleteAuthGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAuthGroup,
                    request_deserializer=face__pb2.DeleteAuthGroupRequest.FromString,
                    response_serializer=face__pb2.DeleteAuthGroupResponse.SerializeToString,
            ),
            'DeleteAuthGroupMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAuthGroupMulti,
                    request_deserializer=face__pb2.DeleteAuthGroupMultiRequest.FromString,
                    response_serializer=face__pb2.DeleteAuthGroupMultiResponse.SerializeToString,
            ),
            'DeleteAllAuthGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAllAuthGroup,
                    request_deserializer=face__pb2.DeleteAllAuthGroupRequest.FromString,
                    response_serializer=face__pb2.DeleteAllAuthGroupResponse.SerializeToString,
            ),
            'DeleteAllAuthGroupMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAllAuthGroupMulti,
                    request_deserializer=face__pb2.DeleteAllAuthGroupMultiRequest.FromString,
                    response_serializer=face__pb2.DeleteAllAuthGroupMultiResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gsdk.face.Face', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Face(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Scan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.face.Face/Scan',
            face__pb2.ScanRequest.SerializeToString,
            face__pb2.ScanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Extract(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.face.Face/Extract',
            face__pb2.ExtractRequest.SerializeToString,
            face__pb2.ExtractResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Normalize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.face.Face/Normalize',
            face__pb2.NormalizeRequest.SerializeToString,
            face__pb2.NormalizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.face.Face/GetConfig',
            face__pb2.GetConfigRequest.SerializeToString,
            face__pb2.GetConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.face.Face/SetConfig',
            face__pb2.SetConfigRequest.SerializeToString,
            face__pb2.SetConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetConfigMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.face.Face/SetConfigMulti',
            face__pb2.SetConfigMultiRequest.SerializeToString,
            face__pb2.SetConfigMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAuthGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.face.Face/GetAuthGroup',
            face__pb2.GetAuthGroupRequest.SerializeToString,
            face__pb2.GetAuthGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddAuthGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.face.Face/AddAuthGroup',
            face__pb2.AddAuthGroupRequest.SerializeToString,
            face__pb2.AddAuthGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddAuthGroupMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.face.Face/AddAuthGroupMulti',
            face__pb2.AddAuthGroupMultiRequest.SerializeToString,
            face__pb2.AddAuthGroupMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAuthGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.face.Face/DeleteAuthGroup',
            face__pb2.DeleteAuthGroupRequest.SerializeToString,
            face__pb2.DeleteAuthGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAuthGroupMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.face.Face/DeleteAuthGroupMulti',
            face__pb2.DeleteAuthGroupMultiRequest.SerializeToString,
            face__pb2.DeleteAuthGroupMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAllAuthGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.face.Face/DeleteAllAuthGroup',
            face__pb2.DeleteAllAuthGroupRequest.SerializeToString,
            face__pb2.DeleteAllAuthGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAllAuthGroupMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.face.Face/DeleteAllAuthGroupMulti',
            face__pb2.DeleteAllAuthGroupMultiRequest.SerializeToString,
            face__pb2.DeleteAllAuthGroupMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
