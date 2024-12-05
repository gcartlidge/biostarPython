# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from biostarPython.service import lift_pb2 as lift__pb2

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
        + f' but the generated code in lift_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class LiftStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetList = channel.unary_unary(
                '/gsdk.lift.Lift/GetList',
                request_serializer=lift__pb2.GetListRequest.SerializeToString,
                response_deserializer=lift__pb2.GetListResponse.FromString,
                _registered_method=True)
        self.GetStatus = channel.unary_unary(
                '/gsdk.lift.Lift/GetStatus',
                request_serializer=lift__pb2.GetStatusRequest.SerializeToString,
                response_deserializer=lift__pb2.GetStatusResponse.FromString,
                _registered_method=True)
        self.Add = channel.unary_unary(
                '/gsdk.lift.Lift/Add',
                request_serializer=lift__pb2.AddRequest.SerializeToString,
                response_deserializer=lift__pb2.AddResponse.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/gsdk.lift.Lift/Delete',
                request_serializer=lift__pb2.DeleteRequest.SerializeToString,
                response_deserializer=lift__pb2.DeleteResponse.FromString,
                _registered_method=True)
        self.DeleteAll = channel.unary_unary(
                '/gsdk.lift.Lift/DeleteAll',
                request_serializer=lift__pb2.DeleteAllRequest.SerializeToString,
                response_deserializer=lift__pb2.DeleteAllResponse.FromString,
                _registered_method=True)
        self.Activate = channel.unary_unary(
                '/gsdk.lift.Lift/Activate',
                request_serializer=lift__pb2.ActivateRequest.SerializeToString,
                response_deserializer=lift__pb2.ActivateResponse.FromString,
                _registered_method=True)
        self.Deactivate = channel.unary_unary(
                '/gsdk.lift.Lift/Deactivate',
                request_serializer=lift__pb2.DeactivateRequest.SerializeToString,
                response_deserializer=lift__pb2.DeactivateResponse.FromString,
                _registered_method=True)
        self.Release = channel.unary_unary(
                '/gsdk.lift.Lift/Release',
                request_serializer=lift__pb2.ReleaseRequest.SerializeToString,
                response_deserializer=lift__pb2.ReleaseResponse.FromString,
                _registered_method=True)
        self.SetAlarm = channel.unary_unary(
                '/gsdk.lift.Lift/SetAlarm',
                request_serializer=lift__pb2.SetAlarmRequest.SerializeToString,
                response_deserializer=lift__pb2.SetAlarmResponse.FromString,
                _registered_method=True)


class LiftServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStatus(self, request, context):
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

    def DeleteAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Activate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deactivate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Release(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAlarm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LiftServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetList,
                    request_deserializer=lift__pb2.GetListRequest.FromString,
                    response_serializer=lift__pb2.GetListResponse.SerializeToString,
            ),
            'GetStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStatus,
                    request_deserializer=lift__pb2.GetStatusRequest.FromString,
                    response_serializer=lift__pb2.GetStatusResponse.SerializeToString,
            ),
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=lift__pb2.AddRequest.FromString,
                    response_serializer=lift__pb2.AddResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=lift__pb2.DeleteRequest.FromString,
                    response_serializer=lift__pb2.DeleteResponse.SerializeToString,
            ),
            'DeleteAll': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAll,
                    request_deserializer=lift__pb2.DeleteAllRequest.FromString,
                    response_serializer=lift__pb2.DeleteAllResponse.SerializeToString,
            ),
            'Activate': grpc.unary_unary_rpc_method_handler(
                    servicer.Activate,
                    request_deserializer=lift__pb2.ActivateRequest.FromString,
                    response_serializer=lift__pb2.ActivateResponse.SerializeToString,
            ),
            'Deactivate': grpc.unary_unary_rpc_method_handler(
                    servicer.Deactivate,
                    request_deserializer=lift__pb2.DeactivateRequest.FromString,
                    response_serializer=lift__pb2.DeactivateResponse.SerializeToString,
            ),
            'Release': grpc.unary_unary_rpc_method_handler(
                    servicer.Release,
                    request_deserializer=lift__pb2.ReleaseRequest.FromString,
                    response_serializer=lift__pb2.ReleaseResponse.SerializeToString,
            ),
            'SetAlarm': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAlarm,
                    request_deserializer=lift__pb2.SetAlarmRequest.FromString,
                    response_serializer=lift__pb2.SetAlarmResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gsdk.lift.Lift', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('gsdk.lift.Lift', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Lift(object):
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
            '/gsdk.lift.Lift/GetList',
            lift__pb2.GetListRequest.SerializeToString,
            lift__pb2.GetListResponse.FromString,
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
    def GetStatus(request,
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
            '/gsdk.lift.Lift/GetStatus',
            lift__pb2.GetStatusRequest.SerializeToString,
            lift__pb2.GetStatusResponse.FromString,
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
            '/gsdk.lift.Lift/Add',
            lift__pb2.AddRequest.SerializeToString,
            lift__pb2.AddResponse.FromString,
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
            '/gsdk.lift.Lift/Delete',
            lift__pb2.DeleteRequest.SerializeToString,
            lift__pb2.DeleteResponse.FromString,
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
            '/gsdk.lift.Lift/DeleteAll',
            lift__pb2.DeleteAllRequest.SerializeToString,
            lift__pb2.DeleteAllResponse.FromString,
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
    def Activate(request,
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
            '/gsdk.lift.Lift/Activate',
            lift__pb2.ActivateRequest.SerializeToString,
            lift__pb2.ActivateResponse.FromString,
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
    def Deactivate(request,
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
            '/gsdk.lift.Lift/Deactivate',
            lift__pb2.DeactivateRequest.SerializeToString,
            lift__pb2.DeactivateResponse.FromString,
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
    def Release(request,
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
            '/gsdk.lift.Lift/Release',
            lift__pb2.ReleaseRequest.SerializeToString,
            lift__pb2.ReleaseResponse.FromString,
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
    def SetAlarm(request,
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
            '/gsdk.lift.Lift/SetAlarm',
            lift__pb2.SetAlarmRequest.SerializeToString,
            lift__pb2.SetAlarmResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
