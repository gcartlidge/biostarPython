# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from biostarPython.service import timed_apb_zone_pb2 as timed__apb__zone__pb2


class TimedAPBZoneStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/gsdk.timed_apb_zone.TimedAPBZone/Get',
                request_serializer=timed__apb__zone__pb2.GetRequest.SerializeToString,
                response_deserializer=timed__apb__zone__pb2.GetResponse.FromString,
                )
        self.GetStatus = channel.unary_unary(
                '/gsdk.timed_apb_zone.TimedAPBZone/GetStatus',
                request_serializer=timed__apb__zone__pb2.GetStatusRequest.SerializeToString,
                response_deserializer=timed__apb__zone__pb2.GetStatusResponse.FromString,
                )
        self.Add = channel.unary_unary(
                '/gsdk.timed_apb_zone.TimedAPBZone/Add',
                request_serializer=timed__apb__zone__pb2.AddRequest.SerializeToString,
                response_deserializer=timed__apb__zone__pb2.AddResponse.FromString,
                )
        self.Clear = channel.unary_unary(
                '/gsdk.timed_apb_zone.TimedAPBZone/Clear',
                request_serializer=timed__apb__zone__pb2.ClearRequest.SerializeToString,
                response_deserializer=timed__apb__zone__pb2.ClearResponse.FromString,
                )
        self.ClearAll = channel.unary_unary(
                '/gsdk.timed_apb_zone.TimedAPBZone/ClearAll',
                request_serializer=timed__apb__zone__pb2.ClearAllRequest.SerializeToString,
                response_deserializer=timed__apb__zone__pb2.ClearAllResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/gsdk.timed_apb_zone.TimedAPBZone/Delete',
                request_serializer=timed__apb__zone__pb2.DeleteRequest.SerializeToString,
                response_deserializer=timed__apb__zone__pb2.DeleteResponse.FromString,
                )
        self.DeleteAll = channel.unary_unary(
                '/gsdk.timed_apb_zone.TimedAPBZone/DeleteAll',
                request_serializer=timed__apb__zone__pb2.DeleteAllRequest.SerializeToString,
                response_deserializer=timed__apb__zone__pb2.DeleteAllResponse.FromString,
                )
        self.SetAlarm = channel.unary_unary(
                '/gsdk.timed_apb_zone.TimedAPBZone/SetAlarm',
                request_serializer=timed__apb__zone__pb2.SetAlarmRequest.SerializeToString,
                response_deserializer=timed__apb__zone__pb2.SetAlarmResponse.FromString,
                )


class TimedAPBZoneServicer(object):
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

    def Clear(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearAll(self, request, context):
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


def add_TimedAPBZoneServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=timed__apb__zone__pb2.GetRequest.FromString,
                    response_serializer=timed__apb__zone__pb2.GetResponse.SerializeToString,
            ),
            'GetStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStatus,
                    request_deserializer=timed__apb__zone__pb2.GetStatusRequest.FromString,
                    response_serializer=timed__apb__zone__pb2.GetStatusResponse.SerializeToString,
            ),
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=timed__apb__zone__pb2.AddRequest.FromString,
                    response_serializer=timed__apb__zone__pb2.AddResponse.SerializeToString,
            ),
            'Clear': grpc.unary_unary_rpc_method_handler(
                    servicer.Clear,
                    request_deserializer=timed__apb__zone__pb2.ClearRequest.FromString,
                    response_serializer=timed__apb__zone__pb2.ClearResponse.SerializeToString,
            ),
            'ClearAll': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearAll,
                    request_deserializer=timed__apb__zone__pb2.ClearAllRequest.FromString,
                    response_serializer=timed__apb__zone__pb2.ClearAllResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=timed__apb__zone__pb2.DeleteRequest.FromString,
                    response_serializer=timed__apb__zone__pb2.DeleteResponse.SerializeToString,
            ),
            'DeleteAll': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAll,
                    request_deserializer=timed__apb__zone__pb2.DeleteAllRequest.FromString,
                    response_serializer=timed__apb__zone__pb2.DeleteAllResponse.SerializeToString,
            ),
            'SetAlarm': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAlarm,
                    request_deserializer=timed__apb__zone__pb2.SetAlarmRequest.FromString,
                    response_serializer=timed__apb__zone__pb2.SetAlarmResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gsdk.timed_apb_zone.TimedAPBZone', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TimedAPBZone(object):
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
        return grpc.experimental.unary_unary(request, target, '/gsdk.timed_apb_zone.TimedAPBZone/Get',
            timed__apb__zone__pb2.GetRequest.SerializeToString,
            timed__apb__zone__pb2.GetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/gsdk.timed_apb_zone.TimedAPBZone/GetStatus',
            timed__apb__zone__pb2.GetStatusRequest.SerializeToString,
            timed__apb__zone__pb2.GetStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/gsdk.timed_apb_zone.TimedAPBZone/Add',
            timed__apb__zone__pb2.AddRequest.SerializeToString,
            timed__apb__zone__pb2.AddResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Clear(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.timed_apb_zone.TimedAPBZone/Clear',
            timed__apb__zone__pb2.ClearRequest.SerializeToString,
            timed__apb__zone__pb2.ClearResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.timed_apb_zone.TimedAPBZone/ClearAll',
            timed__apb__zone__pb2.ClearAllRequest.SerializeToString,
            timed__apb__zone__pb2.ClearAllResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/gsdk.timed_apb_zone.TimedAPBZone/Delete',
            timed__apb__zone__pb2.DeleteRequest.SerializeToString,
            timed__apb__zone__pb2.DeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/gsdk.timed_apb_zone.TimedAPBZone/DeleteAll',
            timed__apb__zone__pb2.DeleteAllRequest.SerializeToString,
            timed__apb__zone__pb2.DeleteAllResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/gsdk.timed_apb_zone.TimedAPBZone/SetAlarm',
            timed__apb__zone__pb2.SetAlarmRequest.SerializeToString,
            timed__apb__zone__pb2.SetAlarmResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
