# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from biostarPython.service import time_pb2 as time__pb2


class TimeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/time.Time/Get',
                request_serializer=time__pb2.GetRequest.SerializeToString,
                response_deserializer=time__pb2.GetResponse.FromString,
                )
        self.Set = channel.unary_unary(
                '/time.Time/Set',
                request_serializer=time__pb2.SetRequest.SerializeToString,
                response_deserializer=time__pb2.SetResponse.FromString,
                )
        self.SetMulti = channel.unary_unary(
                '/time.Time/SetMulti',
                request_serializer=time__pb2.SetMultiRequest.SerializeToString,
                response_deserializer=time__pb2.SetMultiResponse.FromString,
                )
        self.GetConfig = channel.unary_unary(
                '/time.Time/GetConfig',
                request_serializer=time__pb2.GetConfigRequest.SerializeToString,
                response_deserializer=time__pb2.GetConfigResponse.FromString,
                )
        self.SetConfig = channel.unary_unary(
                '/time.Time/SetConfig',
                request_serializer=time__pb2.SetConfigRequest.SerializeToString,
                response_deserializer=time__pb2.SetConfigResponse.FromString,
                )
        self.SetConfigMulti = channel.unary_unary(
                '/time.Time/SetConfigMulti',
                request_serializer=time__pb2.SetConfigMultiRequest.SerializeToString,
                response_deserializer=time__pb2.SetConfigMultiResponse.FromString,
                )
        self.GetDSTConfig = channel.unary_unary(
                '/time.Time/GetDSTConfig',
                request_serializer=time__pb2.GetDSTConfigRequest.SerializeToString,
                response_deserializer=time__pb2.GetDSTConfigResponse.FromString,
                )
        self.SetDSTConfig = channel.unary_unary(
                '/time.Time/SetDSTConfig',
                request_serializer=time__pb2.SetDSTConfigRequest.SerializeToString,
                response_deserializer=time__pb2.SetDSTConfigResponse.FromString,
                )
        self.SetDSTConfigMulti = channel.unary_unary(
                '/time.Time/SetDSTConfigMulti',
                request_serializer=time__pb2.SetDSTConfigMultiRequest.SerializeToString,
                response_deserializer=time__pb2.SetDSTConfigMultiResponse.FromString,
                )


class TimeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Set(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
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

    def GetDSTConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDSTConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDSTConfigMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TimeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=time__pb2.GetRequest.FromString,
                    response_serializer=time__pb2.GetResponse.SerializeToString,
            ),
            'Set': grpc.unary_unary_rpc_method_handler(
                    servicer.Set,
                    request_deserializer=time__pb2.SetRequest.FromString,
                    response_serializer=time__pb2.SetResponse.SerializeToString,
            ),
            'SetMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.SetMulti,
                    request_deserializer=time__pb2.SetMultiRequest.FromString,
                    response_serializer=time__pb2.SetMultiResponse.SerializeToString,
            ),
            'GetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConfig,
                    request_deserializer=time__pb2.GetConfigRequest.FromString,
                    response_serializer=time__pb2.GetConfigResponse.SerializeToString,
            ),
            'SetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfig,
                    request_deserializer=time__pb2.SetConfigRequest.FromString,
                    response_serializer=time__pb2.SetConfigResponse.SerializeToString,
            ),
            'SetConfigMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfigMulti,
                    request_deserializer=time__pb2.SetConfigMultiRequest.FromString,
                    response_serializer=time__pb2.SetConfigMultiResponse.SerializeToString,
            ),
            'GetDSTConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDSTConfig,
                    request_deserializer=time__pb2.GetDSTConfigRequest.FromString,
                    response_serializer=time__pb2.GetDSTConfigResponse.SerializeToString,
            ),
            'SetDSTConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDSTConfig,
                    request_deserializer=time__pb2.SetDSTConfigRequest.FromString,
                    response_serializer=time__pb2.SetDSTConfigResponse.SerializeToString,
            ),
            'SetDSTConfigMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDSTConfigMulti,
                    request_deserializer=time__pb2.SetDSTConfigMultiRequest.FromString,
                    response_serializer=time__pb2.SetDSTConfigMultiResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'time.Time', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Time(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/time.Time/Get',
            time__pb2.GetRequest.SerializeToString,
            time__pb2.GetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Set(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/time.Time/Set',
            time__pb2.SetRequest.SerializeToString,
            time__pb2.SetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/time.Time/SetMulti',
            time__pb2.SetMultiRequest.SerializeToString,
            time__pb2.SetMultiResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/time.Time/GetConfig',
            time__pb2.GetConfigRequest.SerializeToString,
            time__pb2.GetConfigResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/time.Time/SetConfig',
            time__pb2.SetConfigRequest.SerializeToString,
            time__pb2.SetConfigResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/time.Time/SetConfigMulti',
            time__pb2.SetConfigMultiRequest.SerializeToString,
            time__pb2.SetConfigMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDSTConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/time.Time/GetDSTConfig',
            time__pb2.GetDSTConfigRequest.SerializeToString,
            time__pb2.GetDSTConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDSTConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/time.Time/SetDSTConfig',
            time__pb2.SetDSTConfigRequest.SerializeToString,
            time__pb2.SetDSTConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDSTConfigMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/time.Time/SetDSTConfigMulti',
            time__pb2.SetDSTConfigMultiRequest.SerializeToString,
            time__pb2.SetDSTConfigMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)