# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import gateway_pb2 as gateway__pb2

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
        + f' but the generated code in gateway_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class GatewayStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetList = channel.unary_unary(
                '/gsdk.gateway.Gateway/GetList',
                request_serializer=gateway__pb2.GetListRequest.SerializeToString,
                response_deserializer=gateway__pb2.GetListResponse.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/gsdk.gateway.Gateway/Get',
                request_serializer=gateway__pb2.GetRequest.SerializeToString,
                response_deserializer=gateway__pb2.GetResponse.FromString,
                _registered_method=True)
        self.Add = channel.unary_unary(
                '/gsdk.gateway.Gateway/Add',
                request_serializer=gateway__pb2.AddRequest.SerializeToString,
                response_deserializer=gateway__pb2.AddResponse.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/gsdk.gateway.Gateway/Delete',
                request_serializer=gateway__pb2.DeleteRequest.SerializeToString,
                response_deserializer=gateway__pb2.DeleteResponse.FromString,
                _registered_method=True)
        self.CreateCertificate = channel.unary_unary(
                '/gsdk.gateway.Gateway/CreateCertificate',
                request_serializer=gateway__pb2.CreateCertificateRequest.SerializeToString,
                response_deserializer=gateway__pb2.CreateCertificateResponse.FromString,
                _registered_method=True)
        self.GetIssuanceHistory = channel.unary_unary(
                '/gsdk.gateway.Gateway/GetIssuanceHistory',
                request_serializer=gateway__pb2.GetIssuanceHistoryRequest.SerializeToString,
                response_deserializer=gateway__pb2.GetIssuanceHistoryResponse.FromString,
                _registered_method=True)
        self.GetCertificateBlacklist = channel.unary_unary(
                '/gsdk.gateway.Gateway/GetCertificateBlacklist',
                request_serializer=gateway__pb2.GetCertificateBlacklistRequest.SerializeToString,
                response_deserializer=gateway__pb2.GetCertificateBlacklistResponse.FromString,
                _registered_method=True)
        self.AddCertificateBlacklist = channel.unary_unary(
                '/gsdk.gateway.Gateway/AddCertificateBlacklist',
                request_serializer=gateway__pb2.AddCertificateBlacklistRequest.SerializeToString,
                response_deserializer=gateway__pb2.AddCertificateBlacklistResponse.FromString,
                _registered_method=True)
        self.DeleteCertificateBlacklist = channel.unary_unary(
                '/gsdk.gateway.Gateway/DeleteCertificateBlacklist',
                request_serializer=gateway__pb2.DeleteCertificateBlacklistRequest.SerializeToString,
                response_deserializer=gateway__pb2.DeleteCertificateBlacklistResponse.FromString,
                _registered_method=True)
        self.SubscribeStatus = channel.unary_stream(
                '/gsdk.gateway.Gateway/SubscribeStatus',
                request_serializer=gateway__pb2.SubscribeStatusRequest.SerializeToString,
                response_deserializer=gateway__pb2.StatusChange.FromString,
                _registered_method=True)


class GatewayServicer(object):
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

    def Add(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCertificate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIssuanceHistory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCertificateBlacklist(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddCertificateBlacklist(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCertificateBlacklist(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GatewayServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetList,
                    request_deserializer=gateway__pb2.GetListRequest.FromString,
                    response_serializer=gateway__pb2.GetListResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=gateway__pb2.GetRequest.FromString,
                    response_serializer=gateway__pb2.GetResponse.SerializeToString,
            ),
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=gateway__pb2.AddRequest.FromString,
                    response_serializer=gateway__pb2.AddResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=gateway__pb2.DeleteRequest.FromString,
                    response_serializer=gateway__pb2.DeleteResponse.SerializeToString,
            ),
            'CreateCertificate': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCertificate,
                    request_deserializer=gateway__pb2.CreateCertificateRequest.FromString,
                    response_serializer=gateway__pb2.CreateCertificateResponse.SerializeToString,
            ),
            'GetIssuanceHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIssuanceHistory,
                    request_deserializer=gateway__pb2.GetIssuanceHistoryRequest.FromString,
                    response_serializer=gateway__pb2.GetIssuanceHistoryResponse.SerializeToString,
            ),
            'GetCertificateBlacklist': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCertificateBlacklist,
                    request_deserializer=gateway__pb2.GetCertificateBlacklistRequest.FromString,
                    response_serializer=gateway__pb2.GetCertificateBlacklistResponse.SerializeToString,
            ),
            'AddCertificateBlacklist': grpc.unary_unary_rpc_method_handler(
                    servicer.AddCertificateBlacklist,
                    request_deserializer=gateway__pb2.AddCertificateBlacklistRequest.FromString,
                    response_serializer=gateway__pb2.AddCertificateBlacklistResponse.SerializeToString,
            ),
            'DeleteCertificateBlacklist': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCertificateBlacklist,
                    request_deserializer=gateway__pb2.DeleteCertificateBlacklistRequest.FromString,
                    response_serializer=gateway__pb2.DeleteCertificateBlacklistResponse.SerializeToString,
            ),
            'SubscribeStatus': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeStatus,
                    request_deserializer=gateway__pb2.SubscribeStatusRequest.FromString,
                    response_serializer=gateway__pb2.StatusChange.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gsdk.gateway.Gateway', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('gsdk.gateway.Gateway', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Gateway(object):
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.gateway.Gateway/GetList',
            gateway__pb2.GetListRequest.SerializeToString,
            gateway__pb2.GetListResponse.FromString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.gateway.Gateway/Get',
            gateway__pb2.GetRequest.SerializeToString,
            gateway__pb2.GetResponse.FromString,
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
    def Add(request,
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
            '/gsdk.gateway.Gateway/Add',
            gateway__pb2.AddRequest.SerializeToString,
            gateway__pb2.AddResponse.FromString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.gateway.Gateway/Delete',
            gateway__pb2.DeleteRequest.SerializeToString,
            gateway__pb2.DeleteResponse.FromString,
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
    def CreateCertificate(request,
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
            '/gsdk.gateway.Gateway/CreateCertificate',
            gateway__pb2.CreateCertificateRequest.SerializeToString,
            gateway__pb2.CreateCertificateResponse.FromString,
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
    def GetIssuanceHistory(request,
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
            '/gsdk.gateway.Gateway/GetIssuanceHistory',
            gateway__pb2.GetIssuanceHistoryRequest.SerializeToString,
            gateway__pb2.GetIssuanceHistoryResponse.FromString,
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
    def GetCertificateBlacklist(request,
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
            '/gsdk.gateway.Gateway/GetCertificateBlacklist',
            gateway__pb2.GetCertificateBlacklistRequest.SerializeToString,
            gateway__pb2.GetCertificateBlacklistResponse.FromString,
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
    def AddCertificateBlacklist(request,
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
            '/gsdk.gateway.Gateway/AddCertificateBlacklist',
            gateway__pb2.AddCertificateBlacklistRequest.SerializeToString,
            gateway__pb2.AddCertificateBlacklistResponse.FromString,
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
    def DeleteCertificateBlacklist(request,
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
            '/gsdk.gateway.Gateway/DeleteCertificateBlacklist',
            gateway__pb2.DeleteCertificateBlacklistRequest.SerializeToString,
            gateway__pb2.DeleteCertificateBlacklistResponse.FromString,
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
    def SubscribeStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/gsdk.gateway.Gateway/SubscribeStatus',
            gateway__pb2.SubscribeStatusRequest.SerializeToString,
            gateway__pb2.StatusChange.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
