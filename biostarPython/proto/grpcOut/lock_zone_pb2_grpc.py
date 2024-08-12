# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import lock_zone_pb2 as lock__zone__pb2

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
        + f' but the generated code in lock_zone_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class LockZoneStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/gsdk.lock_zone.LockZone/Get',
                request_serializer=lock__zone__pb2.GetRequest.SerializeToString,
                response_deserializer=lock__zone__pb2.GetResponse.FromString,
                _registered_method=True)
        self.GetStatus = channel.unary_unary(
                '/gsdk.lock_zone.LockZone/GetStatus',
                request_serializer=lock__zone__pb2.GetStatusRequest.SerializeToString,
                response_deserializer=lock__zone__pb2.GetStatusResponse.FromString,
                _registered_method=True)
        self.Add = channel.unary_unary(
                '/gsdk.lock_zone.LockZone/Add',
                request_serializer=lock__zone__pb2.AddRequest.SerializeToString,
                response_deserializer=lock__zone__pb2.AddResponse.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/gsdk.lock_zone.LockZone/Delete',
                request_serializer=lock__zone__pb2.DeleteRequest.SerializeToString,
                response_deserializer=lock__zone__pb2.DeleteResponse.FromString,
                _registered_method=True)
        self.DeleteAll = channel.unary_unary(
                '/gsdk.lock_zone.LockZone/DeleteAll',
                request_serializer=lock__zone__pb2.DeleteAllRequest.SerializeToString,
                response_deserializer=lock__zone__pb2.DeleteAllResponse.FromString,
                _registered_method=True)
        self.SetAlarm = channel.unary_unary(
                '/gsdk.lock_zone.LockZone/SetAlarm',
                request_serializer=lock__zone__pb2.SetAlarmRequest.SerializeToString,
                response_deserializer=lock__zone__pb2.SetAlarmResponse.FromString,
                _registered_method=True)


class LockZoneServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
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

    def SetAlarm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LockZoneServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=lock__zone__pb2.GetRequest.FromString,
                    response_serializer=lock__zone__pb2.GetResponse.SerializeToString,
            ),
            'GetStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStatus,
                    request_deserializer=lock__zone__pb2.GetStatusRequest.FromString,
                    response_serializer=lock__zone__pb2.GetStatusResponse.SerializeToString,
            ),
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=lock__zone__pb2.AddRequest.FromString,
                    response_serializer=lock__zone__pb2.AddResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=lock__zone__pb2.DeleteRequest.FromString,
                    response_serializer=lock__zone__pb2.DeleteResponse.SerializeToString,
            ),
            'DeleteAll': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAll,
                    request_deserializer=lock__zone__pb2.DeleteAllRequest.FromString,
                    response_serializer=lock__zone__pb2.DeleteAllResponse.SerializeToString,
            ),
            'SetAlarm': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAlarm,
                    request_deserializer=lock__zone__pb2.SetAlarmRequest.FromString,
                    response_serializer=lock__zone__pb2.SetAlarmResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gsdk.lock_zone.LockZone', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('gsdk.lock_zone.LockZone', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class LockZone(object):
    """Missing associated documentation comment in .proto file."""

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
            '/gsdk.lock_zone.LockZone/Get',
            lock__zone__pb2.GetRequest.SerializeToString,
            lock__zone__pb2.GetResponse.FromString,
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
            '/gsdk.lock_zone.LockZone/GetStatus',
            lock__zone__pb2.GetStatusRequest.SerializeToString,
            lock__zone__pb2.GetStatusResponse.FromString,
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
            '/gsdk.lock_zone.LockZone/Add',
            lock__zone__pb2.AddRequest.SerializeToString,
            lock__zone__pb2.AddResponse.FromString,
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
            '/gsdk.lock_zone.LockZone/Delete',
            lock__zone__pb2.DeleteRequest.SerializeToString,
            lock__zone__pb2.DeleteResponse.FromString,
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
            '/gsdk.lock_zone.LockZone/DeleteAll',
            lock__zone__pb2.DeleteAllRequest.SerializeToString,
            lock__zone__pb2.DeleteAllResponse.FromString,
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
            '/gsdk.lock_zone.LockZone/SetAlarm',
            lock__zone__pb2.SetAlarmRequest.SerializeToString,
            lock__zone__pb2.SetAlarmResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
