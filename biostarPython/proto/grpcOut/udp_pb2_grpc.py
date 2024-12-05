# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from biostarPython.service import udp_pb2 as udp__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in udp_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


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
                _registered_method=True)
        self.SetIPConfig = channel.unary_unary(
                '/gsdk.udp.UDP/SetIPConfig',
                request_serializer=udp__pb2.SetIPConfigRequest.SerializeToString,
                response_deserializer=udp__pb2.SetIPConfigResponse.FromString,
                _registered_method=True)


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
    server.add_registered_method_handlers('gsdk.udp.UDP', rpc_method_handlers)


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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.udp.UDP/GetIPConfig',
            udp__pb2.GetIPConfigRequest.SerializeToString,
            udp__pb2.GetIPConfigResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.udp.UDP/SetIPConfig',
            udp__pb2.SetIPConfigRequest.SerializeToString,
            udp__pb2.SetIPConfigResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
