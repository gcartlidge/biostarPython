# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from biostarPython.service import tenant_pb2 as tenant__pb2

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
        + f' but the generated code in tenant_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TenantStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetList = channel.unary_unary(
                '/gsdk.tenant.Tenant/GetList',
                request_serializer=tenant__pb2.GetListRequest.SerializeToString,
                response_deserializer=tenant__pb2.GetListResponse.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/gsdk.tenant.Tenant/Get',
                request_serializer=tenant__pb2.GetRequest.SerializeToString,
                response_deserializer=tenant__pb2.GetResponse.FromString,
                _registered_method=True)
        self.Add = channel.unary_unary(
                '/gsdk.tenant.Tenant/Add',
                request_serializer=tenant__pb2.AddRequest.SerializeToString,
                response_deserializer=tenant__pb2.AddResponse.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/gsdk.tenant.Tenant/Delete',
                request_serializer=tenant__pb2.DeleteRequest.SerializeToString,
                response_deserializer=tenant__pb2.DeleteResponse.FromString,
                _registered_method=True)
        self.AddGateway = channel.unary_unary(
                '/gsdk.tenant.Tenant/AddGateway',
                request_serializer=tenant__pb2.AddGatewayRequest.SerializeToString,
                response_deserializer=tenant__pb2.AddGatewayResponse.FromString,
                _registered_method=True)
        self.DeleteGateway = channel.unary_unary(
                '/gsdk.tenant.Tenant/DeleteGateway',
                request_serializer=tenant__pb2.DeleteGatewayRequest.SerializeToString,
                response_deserializer=tenant__pb2.DeleteGatewayResponse.FromString,
                _registered_method=True)
        self.CreateCertificate = channel.unary_unary(
                '/gsdk.tenant.Tenant/CreateCertificate',
                request_serializer=tenant__pb2.CreateCertificateRequest.SerializeToString,
                response_deserializer=tenant__pb2.CreateCertificateResponse.FromString,
                _registered_method=True)
        self.GetIssuanceHistory = channel.unary_unary(
                '/gsdk.tenant.Tenant/GetIssuanceHistory',
                request_serializer=tenant__pb2.GetIssuanceHistoryRequest.SerializeToString,
                response_deserializer=tenant__pb2.GetIssuanceHistoryResponse.FromString,
                _registered_method=True)
        self.GetCertificateBlacklist = channel.unary_unary(
                '/gsdk.tenant.Tenant/GetCertificateBlacklist',
                request_serializer=tenant__pb2.GetCertificateBlacklistRequest.SerializeToString,
                response_deserializer=tenant__pb2.GetCertificateBlacklistResponse.FromString,
                _registered_method=True)
        self.AddCertificateBlacklist = channel.unary_unary(
                '/gsdk.tenant.Tenant/AddCertificateBlacklist',
                request_serializer=tenant__pb2.AddCertificateBlacklistRequest.SerializeToString,
                response_deserializer=tenant__pb2.AddCertificateBlacklistResponse.FromString,
                _registered_method=True)
        self.DeleteCertificateBlacklist = channel.unary_unary(
                '/gsdk.tenant.Tenant/DeleteCertificateBlacklist',
                request_serializer=tenant__pb2.DeleteCertificateBlacklistRequest.SerializeToString,
                response_deserializer=tenant__pb2.DeleteCertificateBlacklistResponse.FromString,
                _registered_method=True)


class TenantServicer(object):
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

    def AddGateway(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteGateway(self, request, context):
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


def add_TenantServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetList,
                    request_deserializer=tenant__pb2.GetListRequest.FromString,
                    response_serializer=tenant__pb2.GetListResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=tenant__pb2.GetRequest.FromString,
                    response_serializer=tenant__pb2.GetResponse.SerializeToString,
            ),
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=tenant__pb2.AddRequest.FromString,
                    response_serializer=tenant__pb2.AddResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=tenant__pb2.DeleteRequest.FromString,
                    response_serializer=tenant__pb2.DeleteResponse.SerializeToString,
            ),
            'AddGateway': grpc.unary_unary_rpc_method_handler(
                    servicer.AddGateway,
                    request_deserializer=tenant__pb2.AddGatewayRequest.FromString,
                    response_serializer=tenant__pb2.AddGatewayResponse.SerializeToString,
            ),
            'DeleteGateway': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteGateway,
                    request_deserializer=tenant__pb2.DeleteGatewayRequest.FromString,
                    response_serializer=tenant__pb2.DeleteGatewayResponse.SerializeToString,
            ),
            'CreateCertificate': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCertificate,
                    request_deserializer=tenant__pb2.CreateCertificateRequest.FromString,
                    response_serializer=tenant__pb2.CreateCertificateResponse.SerializeToString,
            ),
            'GetIssuanceHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIssuanceHistory,
                    request_deserializer=tenant__pb2.GetIssuanceHistoryRequest.FromString,
                    response_serializer=tenant__pb2.GetIssuanceHistoryResponse.SerializeToString,
            ),
            'GetCertificateBlacklist': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCertificateBlacklist,
                    request_deserializer=tenant__pb2.GetCertificateBlacklistRequest.FromString,
                    response_serializer=tenant__pb2.GetCertificateBlacklistResponse.SerializeToString,
            ),
            'AddCertificateBlacklist': grpc.unary_unary_rpc_method_handler(
                    servicer.AddCertificateBlacklist,
                    request_deserializer=tenant__pb2.AddCertificateBlacklistRequest.FromString,
                    response_serializer=tenant__pb2.AddCertificateBlacklistResponse.SerializeToString,
            ),
            'DeleteCertificateBlacklist': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCertificateBlacklist,
                    request_deserializer=tenant__pb2.DeleteCertificateBlacklistRequest.FromString,
                    response_serializer=tenant__pb2.DeleteCertificateBlacklistResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gsdk.tenant.Tenant', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('gsdk.tenant.Tenant', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Tenant(object):
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
            '/gsdk.tenant.Tenant/GetList',
            tenant__pb2.GetListRequest.SerializeToString,
            tenant__pb2.GetListResponse.FromString,
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
            '/gsdk.tenant.Tenant/Get',
            tenant__pb2.GetRequest.SerializeToString,
            tenant__pb2.GetResponse.FromString,
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
            '/gsdk.tenant.Tenant/Add',
            tenant__pb2.AddRequest.SerializeToString,
            tenant__pb2.AddResponse.FromString,
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
            '/gsdk.tenant.Tenant/Delete',
            tenant__pb2.DeleteRequest.SerializeToString,
            tenant__pb2.DeleteResponse.FromString,
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
    def AddGateway(request,
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
            '/gsdk.tenant.Tenant/AddGateway',
            tenant__pb2.AddGatewayRequest.SerializeToString,
            tenant__pb2.AddGatewayResponse.FromString,
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
    def DeleteGateway(request,
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
            '/gsdk.tenant.Tenant/DeleteGateway',
            tenant__pb2.DeleteGatewayRequest.SerializeToString,
            tenant__pb2.DeleteGatewayResponse.FromString,
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
            '/gsdk.tenant.Tenant/CreateCertificate',
            tenant__pb2.CreateCertificateRequest.SerializeToString,
            tenant__pb2.CreateCertificateResponse.FromString,
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
            '/gsdk.tenant.Tenant/GetIssuanceHistory',
            tenant__pb2.GetIssuanceHistoryRequest.SerializeToString,
            tenant__pb2.GetIssuanceHistoryResponse.FromString,
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
            '/gsdk.tenant.Tenant/GetCertificateBlacklist',
            tenant__pb2.GetCertificateBlacklistRequest.SerializeToString,
            tenant__pb2.GetCertificateBlacklistResponse.FromString,
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
            '/gsdk.tenant.Tenant/AddCertificateBlacklist',
            tenant__pb2.AddCertificateBlacklistRequest.SerializeToString,
            tenant__pb2.AddCertificateBlacklistResponse.FromString,
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
            '/gsdk.tenant.Tenant/DeleteCertificateBlacklist',
            tenant__pb2.DeleteCertificateBlacklistRequest.SerializeToString,
            tenant__pb2.DeleteCertificateBlacklistResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
