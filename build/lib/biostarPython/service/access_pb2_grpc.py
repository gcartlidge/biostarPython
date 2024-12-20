# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from biostarPython.service import access_pb2 as access__pb2

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
        + f' but the generated code in access_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class AccessStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetList = channel.unary_unary(
                '/gsdk.access.Access/GetList',
                request_serializer=access__pb2.GetListRequest.SerializeToString,
                response_deserializer=access__pb2.GetListResponse.FromString,
                _registered_method=True)
        self.Add = channel.unary_unary(
                '/gsdk.access.Access/Add',
                request_serializer=access__pb2.AddRequest.SerializeToString,
                response_deserializer=access__pb2.AddResponse.FromString,
                _registered_method=True)
        self.AddMulti = channel.unary_unary(
                '/gsdk.access.Access/AddMulti',
                request_serializer=access__pb2.AddMultiRequest.SerializeToString,
                response_deserializer=access__pb2.AddMultiResponse.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/gsdk.access.Access/Delete',
                request_serializer=access__pb2.DeleteRequest.SerializeToString,
                response_deserializer=access__pb2.DeleteResponse.FromString,
                _registered_method=True)
        self.DeleteMulti = channel.unary_unary(
                '/gsdk.access.Access/DeleteMulti',
                request_serializer=access__pb2.DeleteMultiRequest.SerializeToString,
                response_deserializer=access__pb2.DeleteMultiResponse.FromString,
                _registered_method=True)
        self.DeleteAll = channel.unary_unary(
                '/gsdk.access.Access/DeleteAll',
                request_serializer=access__pb2.DeleteAllRequest.SerializeToString,
                response_deserializer=access__pb2.DeleteAllResponse.FromString,
                _registered_method=True)
        self.DeleteAllMulti = channel.unary_unary(
                '/gsdk.access.Access/DeleteAllMulti',
                request_serializer=access__pb2.DeleteAllMultiRequest.SerializeToString,
                response_deserializer=access__pb2.DeleteAllMultiResponse.FromString,
                _registered_method=True)
        self.GetLevelList = channel.unary_unary(
                '/gsdk.access.Access/GetLevelList',
                request_serializer=access__pb2.GetLevelListRequest.SerializeToString,
                response_deserializer=access__pb2.GetLevelListResponse.FromString,
                _registered_method=True)
        self.AddLevel = channel.unary_unary(
                '/gsdk.access.Access/AddLevel',
                request_serializer=access__pb2.AddLevelRequest.SerializeToString,
                response_deserializer=access__pb2.AddLevelResponse.FromString,
                _registered_method=True)
        self.AddLevelMulti = channel.unary_unary(
                '/gsdk.access.Access/AddLevelMulti',
                request_serializer=access__pb2.AddLevelMultiRequest.SerializeToString,
                response_deserializer=access__pb2.AddLevelMultiResponse.FromString,
                _registered_method=True)
        self.DeleteLevel = channel.unary_unary(
                '/gsdk.access.Access/DeleteLevel',
                request_serializer=access__pb2.DeleteLevelRequest.SerializeToString,
                response_deserializer=access__pb2.DeleteLevelResponse.FromString,
                _registered_method=True)
        self.DeleteLevelMulti = channel.unary_unary(
                '/gsdk.access.Access/DeleteLevelMulti',
                request_serializer=access__pb2.DeleteLevelMultiRequest.SerializeToString,
                response_deserializer=access__pb2.DeleteLevelMultiResponse.FromString,
                _registered_method=True)
        self.DeleteAllLevel = channel.unary_unary(
                '/gsdk.access.Access/DeleteAllLevel',
                request_serializer=access__pb2.DeleteAllLevelRequest.SerializeToString,
                response_deserializer=access__pb2.DeleteAllLevelResponse.FromString,
                _registered_method=True)
        self.DeleteAllLevelMulti = channel.unary_unary(
                '/gsdk.access.Access/DeleteAllLevelMulti',
                request_serializer=access__pb2.DeleteAllLevelMultiRequest.SerializeToString,
                response_deserializer=access__pb2.DeleteAllLevelMultiResponse.FromString,
                _registered_method=True)
        self.GetFloorLevelList = channel.unary_unary(
                '/gsdk.access.Access/GetFloorLevelList',
                request_serializer=access__pb2.GetFloorLevelListRequest.SerializeToString,
                response_deserializer=access__pb2.GetFloorLevelListResponse.FromString,
                _registered_method=True)
        self.AddFloorLevel = channel.unary_unary(
                '/gsdk.access.Access/AddFloorLevel',
                request_serializer=access__pb2.AddFloorLevelRequest.SerializeToString,
                response_deserializer=access__pb2.AddFloorLevelResponse.FromString,
                _registered_method=True)
        self.AddFloorLevelMulti = channel.unary_unary(
                '/gsdk.access.Access/AddFloorLevelMulti',
                request_serializer=access__pb2.AddFloorLevelMultiRequest.SerializeToString,
                response_deserializer=access__pb2.AddFloorLevelMultiResponse.FromString,
                _registered_method=True)
        self.DeleteFloorLevel = channel.unary_unary(
                '/gsdk.access.Access/DeleteFloorLevel',
                request_serializer=access__pb2.DeleteFloorLevelRequest.SerializeToString,
                response_deserializer=access__pb2.DeleteFloorLevelResponse.FromString,
                _registered_method=True)
        self.DeleteFloorLevelMulti = channel.unary_unary(
                '/gsdk.access.Access/DeleteFloorLevelMulti',
                request_serializer=access__pb2.DeleteFloorLevelMultiRequest.SerializeToString,
                response_deserializer=access__pb2.DeleteFloorLevelMultiResponse.FromString,
                _registered_method=True)
        self.DeleteAllFloorLevel = channel.unary_unary(
                '/gsdk.access.Access/DeleteAllFloorLevel',
                request_serializer=access__pb2.DeleteAllFloorLevelRequest.SerializeToString,
                response_deserializer=access__pb2.DeleteAllFloorLevelResponse.FromString,
                _registered_method=True)
        self.DeleteAllFloorLevelMulti = channel.unary_unary(
                '/gsdk.access.Access/DeleteAllFloorLevelMulti',
                request_serializer=access__pb2.DeleteAllFloorLevelMultiRequest.SerializeToString,
                response_deserializer=access__pb2.DeleteAllFloorLevelMultiResponse.FromString,
                _registered_method=True)


class AccessServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Add(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAllMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLevelList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddLevel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddLevelMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteLevel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteLevelMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAllLevel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAllLevelMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFloorLevelList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddFloorLevel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddFloorLevelMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFloorLevel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFloorLevelMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAllFloorLevel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAllFloorLevelMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccessServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetList,
                    request_deserializer=access__pb2.GetListRequest.FromString,
                    response_serializer=access__pb2.GetListResponse.SerializeToString,
            ),
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=access__pb2.AddRequest.FromString,
                    response_serializer=access__pb2.AddResponse.SerializeToString,
            ),
            'AddMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.AddMulti,
                    request_deserializer=access__pb2.AddMultiRequest.FromString,
                    response_serializer=access__pb2.AddMultiResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=access__pb2.DeleteRequest.FromString,
                    response_serializer=access__pb2.DeleteResponse.SerializeToString,
            ),
            'DeleteMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteMulti,
                    request_deserializer=access__pb2.DeleteMultiRequest.FromString,
                    response_serializer=access__pb2.DeleteMultiResponse.SerializeToString,
            ),
            'DeleteAll': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAll,
                    request_deserializer=access__pb2.DeleteAllRequest.FromString,
                    response_serializer=access__pb2.DeleteAllResponse.SerializeToString,
            ),
            'DeleteAllMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAllMulti,
                    request_deserializer=access__pb2.DeleteAllMultiRequest.FromString,
                    response_serializer=access__pb2.DeleteAllMultiResponse.SerializeToString,
            ),
            'GetLevelList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLevelList,
                    request_deserializer=access__pb2.GetLevelListRequest.FromString,
                    response_serializer=access__pb2.GetLevelListResponse.SerializeToString,
            ),
            'AddLevel': grpc.unary_unary_rpc_method_handler(
                    servicer.AddLevel,
                    request_deserializer=access__pb2.AddLevelRequest.FromString,
                    response_serializer=access__pb2.AddLevelResponse.SerializeToString,
            ),
            'AddLevelMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.AddLevelMulti,
                    request_deserializer=access__pb2.AddLevelMultiRequest.FromString,
                    response_serializer=access__pb2.AddLevelMultiResponse.SerializeToString,
            ),
            'DeleteLevel': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteLevel,
                    request_deserializer=access__pb2.DeleteLevelRequest.FromString,
                    response_serializer=access__pb2.DeleteLevelResponse.SerializeToString,
            ),
            'DeleteLevelMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteLevelMulti,
                    request_deserializer=access__pb2.DeleteLevelMultiRequest.FromString,
                    response_serializer=access__pb2.DeleteLevelMultiResponse.SerializeToString,
            ),
            'DeleteAllLevel': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAllLevel,
                    request_deserializer=access__pb2.DeleteAllLevelRequest.FromString,
                    response_serializer=access__pb2.DeleteAllLevelResponse.SerializeToString,
            ),
            'DeleteAllLevelMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAllLevelMulti,
                    request_deserializer=access__pb2.DeleteAllLevelMultiRequest.FromString,
                    response_serializer=access__pb2.DeleteAllLevelMultiResponse.SerializeToString,
            ),
            'GetFloorLevelList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFloorLevelList,
                    request_deserializer=access__pb2.GetFloorLevelListRequest.FromString,
                    response_serializer=access__pb2.GetFloorLevelListResponse.SerializeToString,
            ),
            'AddFloorLevel': grpc.unary_unary_rpc_method_handler(
                    servicer.AddFloorLevel,
                    request_deserializer=access__pb2.AddFloorLevelRequest.FromString,
                    response_serializer=access__pb2.AddFloorLevelResponse.SerializeToString,
            ),
            'AddFloorLevelMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.AddFloorLevelMulti,
                    request_deserializer=access__pb2.AddFloorLevelMultiRequest.FromString,
                    response_serializer=access__pb2.AddFloorLevelMultiResponse.SerializeToString,
            ),
            'DeleteFloorLevel': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFloorLevel,
                    request_deserializer=access__pb2.DeleteFloorLevelRequest.FromString,
                    response_serializer=access__pb2.DeleteFloorLevelResponse.SerializeToString,
            ),
            'DeleteFloorLevelMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFloorLevelMulti,
                    request_deserializer=access__pb2.DeleteFloorLevelMultiRequest.FromString,
                    response_serializer=access__pb2.DeleteFloorLevelMultiResponse.SerializeToString,
            ),
            'DeleteAllFloorLevel': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAllFloorLevel,
                    request_deserializer=access__pb2.DeleteAllFloorLevelRequest.FromString,
                    response_serializer=access__pb2.DeleteAllFloorLevelResponse.SerializeToString,
            ),
            'DeleteAllFloorLevelMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAllFloorLevelMulti,
                    request_deserializer=access__pb2.DeleteAllFloorLevelMultiRequest.FromString,
                    response_serializer=access__pb2.DeleteAllFloorLevelMultiResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gsdk.access.Access', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('gsdk.access.Access', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Access(object):
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
            '/gsdk.access.Access/GetList',
            access__pb2.GetListRequest.SerializeToString,
            access__pb2.GetListResponse.FromString,
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
            '/gsdk.access.Access/Add',
            access__pb2.AddRequest.SerializeToString,
            access__pb2.AddResponse.FromString,
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
    def AddMulti(request,
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
            '/gsdk.access.Access/AddMulti',
            access__pb2.AddMultiRequest.SerializeToString,
            access__pb2.AddMultiResponse.FromString,
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
            '/gsdk.access.Access/Delete',
            access__pb2.DeleteRequest.SerializeToString,
            access__pb2.DeleteResponse.FromString,
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
    def DeleteMulti(request,
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
            '/gsdk.access.Access/DeleteMulti',
            access__pb2.DeleteMultiRequest.SerializeToString,
            access__pb2.DeleteMultiResponse.FromString,
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
    def DeleteAll(request,
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
            '/gsdk.access.Access/DeleteAll',
            access__pb2.DeleteAllRequest.SerializeToString,
            access__pb2.DeleteAllResponse.FromString,
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
    def DeleteAllMulti(request,
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
            '/gsdk.access.Access/DeleteAllMulti',
            access__pb2.DeleteAllMultiRequest.SerializeToString,
            access__pb2.DeleteAllMultiResponse.FromString,
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
    def GetLevelList(request,
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
            '/gsdk.access.Access/GetLevelList',
            access__pb2.GetLevelListRequest.SerializeToString,
            access__pb2.GetLevelListResponse.FromString,
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
    def AddLevel(request,
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
            '/gsdk.access.Access/AddLevel',
            access__pb2.AddLevelRequest.SerializeToString,
            access__pb2.AddLevelResponse.FromString,
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
    def AddLevelMulti(request,
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
            '/gsdk.access.Access/AddLevelMulti',
            access__pb2.AddLevelMultiRequest.SerializeToString,
            access__pb2.AddLevelMultiResponse.FromString,
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
    def DeleteLevel(request,
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
            '/gsdk.access.Access/DeleteLevel',
            access__pb2.DeleteLevelRequest.SerializeToString,
            access__pb2.DeleteLevelResponse.FromString,
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
    def DeleteLevelMulti(request,
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
            '/gsdk.access.Access/DeleteLevelMulti',
            access__pb2.DeleteLevelMultiRequest.SerializeToString,
            access__pb2.DeleteLevelMultiResponse.FromString,
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
    def DeleteAllLevel(request,
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
            '/gsdk.access.Access/DeleteAllLevel',
            access__pb2.DeleteAllLevelRequest.SerializeToString,
            access__pb2.DeleteAllLevelResponse.FromString,
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
    def DeleteAllLevelMulti(request,
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
            '/gsdk.access.Access/DeleteAllLevelMulti',
            access__pb2.DeleteAllLevelMultiRequest.SerializeToString,
            access__pb2.DeleteAllLevelMultiResponse.FromString,
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
    def GetFloorLevelList(request,
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
            '/gsdk.access.Access/GetFloorLevelList',
            access__pb2.GetFloorLevelListRequest.SerializeToString,
            access__pb2.GetFloorLevelListResponse.FromString,
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
    def AddFloorLevel(request,
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
            '/gsdk.access.Access/AddFloorLevel',
            access__pb2.AddFloorLevelRequest.SerializeToString,
            access__pb2.AddFloorLevelResponse.FromString,
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
    def AddFloorLevelMulti(request,
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
            '/gsdk.access.Access/AddFloorLevelMulti',
            access__pb2.AddFloorLevelMultiRequest.SerializeToString,
            access__pb2.AddFloorLevelMultiResponse.FromString,
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
    def DeleteFloorLevel(request,
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
            '/gsdk.access.Access/DeleteFloorLevel',
            access__pb2.DeleteFloorLevelRequest.SerializeToString,
            access__pb2.DeleteFloorLevelResponse.FromString,
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
    def DeleteFloorLevelMulti(request,
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
            '/gsdk.access.Access/DeleteFloorLevelMulti',
            access__pb2.DeleteFloorLevelMultiRequest.SerializeToString,
            access__pb2.DeleteFloorLevelMultiResponse.FromString,
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
    def DeleteAllFloorLevel(request,
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
            '/gsdk.access.Access/DeleteAllFloorLevel',
            access__pb2.DeleteAllFloorLevelRequest.SerializeToString,
            access__pb2.DeleteAllFloorLevelResponse.FromString,
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
    def DeleteAllFloorLevelMulti(request,
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
            '/gsdk.access.Access/DeleteAllFloorLevelMulti',
            access__pb2.DeleteAllFloorLevelMultiRequest.SerializeToString,
            access__pb2.DeleteAllFloorLevelMultiResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
