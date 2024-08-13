# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import tna_pb2 as tna__pb2

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
        + f' but the generated code in tna_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class TNAStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetConfig = channel.unary_unary(
                '/gsdk.tna.TNA/GetConfig',
                request_serializer=tna__pb2.GetConfigRequest.SerializeToString,
                response_deserializer=tna__pb2.GetConfigResponse.FromString,
                _registered_method=True)
        self.SetConfig = channel.unary_unary(
                '/gsdk.tna.TNA/SetConfig',
                request_serializer=tna__pb2.SetConfigRequest.SerializeToString,
                response_deserializer=tna__pb2.SetConfigResponse.FromString,
                _registered_method=True)
        self.SetConfigMulti = channel.unary_unary(
                '/gsdk.tna.TNA/SetConfigMulti',
                request_serializer=tna__pb2.SetConfigMultiRequest.SerializeToString,
                response_deserializer=tna__pb2.SetConfigMultiResponse.FromString,
                _registered_method=True)
        self.GetTNALog = channel.unary_unary(
                '/gsdk.tna.TNA/GetTNALog',
                request_serializer=tna__pb2.GetTNALogRequest.SerializeToString,
                response_deserializer=tna__pb2.GetTNALogResponse.FromString,
                _registered_method=True)
        self.GetJobCodeLog = channel.unary_unary(
                '/gsdk.tna.TNA/GetJobCodeLog',
                request_serializer=tna__pb2.GetJobCodeLogRequest.SerializeToString,
                response_deserializer=tna__pb2.GetJobCodeLogResponse.FromString,
                _registered_method=True)


class TNAServicer(object):
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

    def GetTNALog(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJobCodeLog(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TNAServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConfig,
                    request_deserializer=tna__pb2.GetConfigRequest.FromString,
                    response_serializer=tna__pb2.GetConfigResponse.SerializeToString,
            ),
            'SetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfig,
                    request_deserializer=tna__pb2.SetConfigRequest.FromString,
                    response_serializer=tna__pb2.SetConfigResponse.SerializeToString,
            ),
            'SetConfigMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfigMulti,
                    request_deserializer=tna__pb2.SetConfigMultiRequest.FromString,
                    response_serializer=tna__pb2.SetConfigMultiResponse.SerializeToString,
            ),
            'GetTNALog': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTNALog,
                    request_deserializer=tna__pb2.GetTNALogRequest.FromString,
                    response_serializer=tna__pb2.GetTNALogResponse.SerializeToString,
            ),
            'GetJobCodeLog': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJobCodeLog,
                    request_deserializer=tna__pb2.GetJobCodeLogRequest.FromString,
                    response_serializer=tna__pb2.GetJobCodeLogResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gsdk.tna.TNA', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('gsdk.tna.TNA', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TNA(object):
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
            '/gsdk.tna.TNA/GetConfig',
            tna__pb2.GetConfigRequest.SerializeToString,
            tna__pb2.GetConfigResponse.FromString,
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
            '/gsdk.tna.TNA/SetConfig',
            tna__pb2.SetConfigRequest.SerializeToString,
            tna__pb2.SetConfigResponse.FromString,
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
            '/gsdk.tna.TNA/SetConfigMulti',
            tna__pb2.SetConfigMultiRequest.SerializeToString,
            tna__pb2.SetConfigMultiResponse.FromString,
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
    def GetTNALog(request,
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
            '/gsdk.tna.TNA/GetTNALog',
            tna__pb2.GetTNALogRequest.SerializeToString,
            tna__pb2.GetTNALogResponse.FromString,
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
    def GetJobCodeLog(request,
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
            '/gsdk.tna.TNA/GetJobCodeLog',
            tna__pb2.GetJobCodeLogRequest.SerializeToString,
            tna__pb2.GetJobCodeLogResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)