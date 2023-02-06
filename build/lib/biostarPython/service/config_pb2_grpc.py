# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from biostarPython.service import config_pb2 as config__pb2


class ConfigStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSystem = channel.unary_unary(
                '/config.Config/GetSystem',
                request_serializer=config__pb2.GetSystemRequest.SerializeToString,
                response_deserializer=config__pb2.GetSystemResponse.FromString,
                )
        self.SetSystem = channel.unary_unary(
                '/config.Config/SetSystem',
                request_serializer=config__pb2.SetSystemRequest.SerializeToString,
                response_deserializer=config__pb2.SetSystemResponse.FromString,
                )
        self.SetSystemMulti = channel.unary_unary(
                '/config.Config/SetSystemMulti',
                request_serializer=config__pb2.SetSystemMultiRequest.SerializeToString,
                response_deserializer=config__pb2.SetSystemMultiResponse.FromString,
                )


class ConfigServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSystem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSystem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSystemMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConfigServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSystem': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSystem,
                    request_deserializer=config__pb2.GetSystemRequest.FromString,
                    response_serializer=config__pb2.GetSystemResponse.SerializeToString,
            ),
            'SetSystem': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSystem,
                    request_deserializer=config__pb2.SetSystemRequest.FromString,
                    response_serializer=config__pb2.SetSystemResponse.SerializeToString,
            ),
            'SetSystemMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSystemMulti,
                    request_deserializer=config__pb2.SetSystemMultiRequest.FromString,
                    response_serializer=config__pb2.SetSystemMultiResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'config.Config', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Config(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSystem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.Config/GetSystem',
            config__pb2.GetSystemRequest.SerializeToString,
            config__pb2.GetSystemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSystem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.Config/SetSystem',
            config__pb2.SetSystemRequest.SerializeToString,
            config__pb2.SetSystemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSystemMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.Config/SetSystemMulti',
            config__pb2.SetSystemMultiRequest.SerializeToString,
            config__pb2.SetSystemMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
