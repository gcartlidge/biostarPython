# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from biostarPython.service import udp_pb2 as udp__pb2


class UDPStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetIPConfig = channel.unary_unary(
                '/gsdk.udp.UDP/GetIPConfig',
                request_serializer=udp__pb2.GetIPConfigRequest.SerializeToString,
                response_deserializer=udp__pb2.GetIPConfigResponse.FromString,
                )
        self.SetIPConfig = channel.unary_unary(
                '/gsdk.udp.UDP/SetIPConfig',
                request_serializer=udp__pb2.SetIPConfigRequest.SerializeToString,
                response_deserializer=udp__pb2.SetIPConfigResponse.FromString,
                )


class UDPServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetIPConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetIPConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UDPServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetIPConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIPConfig,
                    request_deserializer=udp__pb2.GetIPConfigRequest.FromString,
                    response_serializer=udp__pb2.GetIPConfigResponse.SerializeToString,
            ),
            'SetIPConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SetIPConfig,
                    request_deserializer=udp__pb2.SetIPConfigRequest.FromString,
                    response_serializer=udp__pb2.SetIPConfigResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gsdk.udp.UDP', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UDP(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetIPConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.udp.UDP/GetIPConfig',
            udp__pb2.GetIPConfigRequest.SerializeToString,
            udp__pb2.GetIPConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetIPConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.udp.UDP/SetIPConfig',
            udp__pb2.SetIPConfigRequest.SerializeToString,
            udp__pb2.SetIPConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)