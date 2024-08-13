# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import wiegand_pb2 as wiegand__pb2

GRPC_GENERATED_VERSION = '1.65.4'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in wiegand_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class WiegandStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetConfig = channel.unary_unary(
                '/gsdk.wiegand.Wiegand/GetConfig',
                request_serializer=wiegand__pb2.GetConfigRequest.SerializeToString,
                response_deserializer=wiegand__pb2.GetConfigResponse.FromString,
                _registered_method=True)
        self.SetConfig = channel.unary_unary(
                '/gsdk.wiegand.Wiegand/SetConfig',
                request_serializer=wiegand__pb2.SetConfigRequest.SerializeToString,
                response_deserializer=wiegand__pb2.SetConfigResponse.FromString,
                _registered_method=True)
        self.SetConfigMulti = channel.unary_unary(
                '/gsdk.wiegand.Wiegand/SetConfigMulti',
                request_serializer=wiegand__pb2.SetConfigMultiRequest.SerializeToString,
                response_deserializer=wiegand__pb2.SetConfigMultiResponse.FromString,
                _registered_method=True)
        self.SearchDevice = channel.unary_unary(
                '/gsdk.wiegand.Wiegand/SearchDevice',
                request_serializer=wiegand__pb2.SearchDeviceRequest.SerializeToString,
                response_deserializer=wiegand__pb2.SearchDeviceResponse.FromString,
                _registered_method=True)
        self.SetDevice = channel.unary_unary(
                '/gsdk.wiegand.Wiegand/SetDevice',
                request_serializer=wiegand__pb2.SetDeviceRequest.SerializeToString,
                response_deserializer=wiegand__pb2.SetDeviceResponse.FromString,
                _registered_method=True)
        self.GetDevice = channel.unary_unary(
                '/gsdk.wiegand.Wiegand/GetDevice',
                request_serializer=wiegand__pb2.GetDeviceRequest.SerializeToString,
                response_deserializer=wiegand__pb2.GetDeviceResponse.FromString,
                _registered_method=True)


class WiegandServicer(object):
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

    def SearchDevice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDevice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDevice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WiegandServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConfig,
                    request_deserializer=wiegand__pb2.GetConfigRequest.FromString,
                    response_serializer=wiegand__pb2.GetConfigResponse.SerializeToString,
            ),
            'SetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfig,
                    request_deserializer=wiegand__pb2.SetConfigRequest.FromString,
                    response_serializer=wiegand__pb2.SetConfigResponse.SerializeToString,
            ),
            'SetConfigMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfigMulti,
                    request_deserializer=wiegand__pb2.SetConfigMultiRequest.FromString,
                    response_serializer=wiegand__pb2.SetConfigMultiResponse.SerializeToString,
            ),
            'SearchDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchDevice,
                    request_deserializer=wiegand__pb2.SearchDeviceRequest.FromString,
                    response_serializer=wiegand__pb2.SearchDeviceResponse.SerializeToString,
            ),
            'SetDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDevice,
                    request_deserializer=wiegand__pb2.SetDeviceRequest.FromString,
                    response_serializer=wiegand__pb2.SetDeviceResponse.SerializeToString,
            ),
            'GetDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDevice,
                    request_deserializer=wiegand__pb2.GetDeviceRequest.FromString,
                    response_serializer=wiegand__pb2.GetDeviceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gsdk.wiegand.Wiegand', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('gsdk.wiegand.Wiegand', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Wiegand(object):
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.wiegand.Wiegand/GetConfig',
            wiegand__pb2.GetConfigRequest.SerializeToString,
            wiegand__pb2.GetConfigResponse.FromString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.wiegand.Wiegand/SetConfig',
            wiegand__pb2.SetConfigRequest.SerializeToString,
            wiegand__pb2.SetConfigResponse.FromString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.wiegand.Wiegand/SetConfigMulti',
            wiegand__pb2.SetConfigMultiRequest.SerializeToString,
            wiegand__pb2.SetConfigMultiResponse.FromString,
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
    def SearchDevice(request,
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
            '/gsdk.wiegand.Wiegand/SearchDevice',
            wiegand__pb2.SearchDeviceRequest.SerializeToString,
            wiegand__pb2.SearchDeviceResponse.FromString,
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
    def SetDevice(request,
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
            '/gsdk.wiegand.Wiegand/SetDevice',
            wiegand__pb2.SetDeviceRequest.SerializeToString,
            wiegand__pb2.SetDeviceResponse.FromString,
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
    def GetDevice(request,
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
            '/gsdk.wiegand.Wiegand/GetDevice',
            wiegand__pb2.GetDeviceRequest.SerializeToString,
            wiegand__pb2.GetDeviceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)