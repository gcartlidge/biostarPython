# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from biostarPython.service import input_pb2 as input__pb2


class InputStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetConfig = channel.unary_unary(
                '/gsdk.input.Input/GetConfig',
                request_serializer=input__pb2.GetConfigRequest.SerializeToString,
                response_deserializer=input__pb2.GetConfigResponse.FromString,
                )
        self.SetConfig = channel.unary_unary(
                '/gsdk.input.Input/SetConfig',
                request_serializer=input__pb2.SetConfigRequest.SerializeToString,
                response_deserializer=input__pb2.SetConfigResponse.FromString,
                )
        self.SetConfigMulti = channel.unary_unary(
                '/gsdk.input.Input/SetConfigMulti',
                request_serializer=input__pb2.SetConfigMultiRequest.SerializeToString,
                response_deserializer=input__pb2.SetConfigMultiResponse.FromString,
                )


class InputServicer(object):
    """Missing associated documentation comment in .proto file."""

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


def add_InputServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConfig,
                    request_deserializer=input__pb2.GetConfigRequest.FromString,
                    response_serializer=input__pb2.GetConfigResponse.SerializeToString,
            ),
            'SetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfig,
                    request_deserializer=input__pb2.SetConfigRequest.FromString,
                    response_serializer=input__pb2.SetConfigResponse.SerializeToString,
            ),
            'SetConfigMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfigMulti,
                    request_deserializer=input__pb2.SetConfigMultiRequest.FromString,
                    response_serializer=input__pb2.SetConfigMultiResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gsdk.input.Input', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Input(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/gsdk.input.Input/GetConfig',
            input__pb2.GetConfigRequest.SerializeToString,
            input__pb2.GetConfigResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/gsdk.input.Input/SetConfig',
            input__pb2.SetConfigRequest.SerializeToString,
            input__pb2.SetConfigResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/gsdk.input.Input/SetConfigMulti',
            input__pb2.SetConfigMultiRequest.SerializeToString,
            input__pb2.SetConfigMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
