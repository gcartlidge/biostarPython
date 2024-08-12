# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from biostarPython.service import event_pb2 as event__pb2


class EventStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.EnableMonitoring = channel.unary_unary(
                '/gsdk.event.Event/EnableMonitoring',
                request_serializer=event__pb2.EnableMonitoringRequest.SerializeToString,
                response_deserializer=event__pb2.EnableMonitoringResponse.FromString,
                )
        self.EnableMonitoringMulti = channel.unary_unary(
                '/gsdk.event.Event/EnableMonitoringMulti',
                request_serializer=event__pb2.EnableMonitoringMultiRequest.SerializeToString,
                response_deserializer=event__pb2.EnableMonitoringMultiResponse.FromString,
                )
        self.DisableMonitoring = channel.unary_unary(
                '/gsdk.event.Event/DisableMonitoring',
                request_serializer=event__pb2.DisableMonitoringRequest.SerializeToString,
                response_deserializer=event__pb2.DisableMonitoringResponse.FromString,
                )
        self.DisableMonitoringMulti = channel.unary_unary(
                '/gsdk.event.Event/DisableMonitoringMulti',
                request_serializer=event__pb2.DisableMonitoringMultiRequest.SerializeToString,
                response_deserializer=event__pb2.DisableMonitoringMultiResponse.FromString,
                )
        self.SubscribeRealtimeLog = channel.unary_stream(
                '/gsdk.event.Event/SubscribeRealtimeLog',
                request_serializer=event__pb2.SubscribeRealtimeLogRequest.SerializeToString,
                response_deserializer=event__pb2.EventLog.FromString,
                )
        self.GetLog = channel.unary_unary(
                '/gsdk.event.Event/GetLog',
                request_serializer=event__pb2.GetLogRequest.SerializeToString,
                response_deserializer=event__pb2.GetLogResponse.FromString,
                )
        self.GetLogWithFilter = channel.unary_unary(
                '/gsdk.event.Event/GetLogWithFilter',
                request_serializer=event__pb2.GetLogWithFilterRequest.SerializeToString,
                response_deserializer=event__pb2.GetLogWithFilterResponse.FromString,
                )
        self.GetImageLog = channel.unary_unary(
                '/gsdk.event.Event/GetImageLog',
                request_serializer=event__pb2.GetImageLogRequest.SerializeToString,
                response_deserializer=event__pb2.GetImageLogResponse.FromString,
                )
        self.GetImageFilter = channel.unary_unary(
                '/gsdk.event.Event/GetImageFilter',
                request_serializer=event__pb2.GetImageFilterRequest.SerializeToString,
                response_deserializer=event__pb2.GetImageFilterResponse.FromString,
                )
        self.SetImageFilter = channel.unary_unary(
                '/gsdk.event.Event/SetImageFilter',
                request_serializer=event__pb2.SetImageFilterRequest.SerializeToString,
                response_deserializer=event__pb2.SetImageFilterResponse.FromString,
                )
        self.SetImageFilterMulti = channel.unary_unary(
                '/gsdk.event.Event/SetImageFilterMulti',
                request_serializer=event__pb2.SetImageFilterMultiRequest.SerializeToString,
                response_deserializer=event__pb2.SetImageFilterMultiResponse.FromString,
                )
        self.ClearLog = channel.unary_unary(
                '/gsdk.event.Event/ClearLog',
                request_serializer=event__pb2.ClearLogRequest.SerializeToString,
                response_deserializer=event__pb2.ClearLogResponse.FromString,
                )
        self.ClearLogMulti = channel.unary_unary(
                '/gsdk.event.Event/ClearLogMulti',
                request_serializer=event__pb2.ClearLogMultiRequest.SerializeToString,
                response_deserializer=event__pb2.ClearLogMultiResponse.FromString,
                )


class EventServicer(object):
    """Missing associated documentation comment in .proto file."""

    def EnableMonitoring(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableMonitoringMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableMonitoring(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableMonitoringMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeRealtimeLog(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLog(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLogWithFilter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetImageLog(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetImageFilter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetImageFilter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetImageFilterMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearLog(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearLogMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'EnableMonitoring': grpc.unary_unary_rpc_method_handler(
                    servicer.EnableMonitoring,
                    request_deserializer=event__pb2.EnableMonitoringRequest.FromString,
                    response_serializer=event__pb2.EnableMonitoringResponse.SerializeToString,
            ),
            'EnableMonitoringMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.EnableMonitoringMulti,
                    request_deserializer=event__pb2.EnableMonitoringMultiRequest.FromString,
                    response_serializer=event__pb2.EnableMonitoringMultiResponse.SerializeToString,
            ),
            'DisableMonitoring': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableMonitoring,
                    request_deserializer=event__pb2.DisableMonitoringRequest.FromString,
                    response_serializer=event__pb2.DisableMonitoringResponse.SerializeToString,
            ),
            'DisableMonitoringMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableMonitoringMulti,
                    request_deserializer=event__pb2.DisableMonitoringMultiRequest.FromString,
                    response_serializer=event__pb2.DisableMonitoringMultiResponse.SerializeToString,
            ),
            'SubscribeRealtimeLog': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeRealtimeLog,
                    request_deserializer=event__pb2.SubscribeRealtimeLogRequest.FromString,
                    response_serializer=event__pb2.EventLog.SerializeToString,
            ),
            'GetLog': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLog,
                    request_deserializer=event__pb2.GetLogRequest.FromString,
                    response_serializer=event__pb2.GetLogResponse.SerializeToString,
            ),
            'GetLogWithFilter': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLogWithFilter,
                    request_deserializer=event__pb2.GetLogWithFilterRequest.FromString,
                    response_serializer=event__pb2.GetLogWithFilterResponse.SerializeToString,
            ),
            'GetImageLog': grpc.unary_unary_rpc_method_handler(
                    servicer.GetImageLog,
                    request_deserializer=event__pb2.GetImageLogRequest.FromString,
                    response_serializer=event__pb2.GetImageLogResponse.SerializeToString,
            ),
            'GetImageFilter': grpc.unary_unary_rpc_method_handler(
                    servicer.GetImageFilter,
                    request_deserializer=event__pb2.GetImageFilterRequest.FromString,
                    response_serializer=event__pb2.GetImageFilterResponse.SerializeToString,
            ),
            'SetImageFilter': grpc.unary_unary_rpc_method_handler(
                    servicer.SetImageFilter,
                    request_deserializer=event__pb2.SetImageFilterRequest.FromString,
                    response_serializer=event__pb2.SetImageFilterResponse.SerializeToString,
            ),
            'SetImageFilterMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.SetImageFilterMulti,
                    request_deserializer=event__pb2.SetImageFilterMultiRequest.FromString,
                    response_serializer=event__pb2.SetImageFilterMultiResponse.SerializeToString,
            ),
            'ClearLog': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearLog,
                    request_deserializer=event__pb2.ClearLogRequest.FromString,
                    response_serializer=event__pb2.ClearLogResponse.SerializeToString,
            ),
            'ClearLogMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearLogMulti,
                    request_deserializer=event__pb2.ClearLogMultiRequest.FromString,
                    response_serializer=event__pb2.ClearLogMultiResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gsdk.event.Event', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Event(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def EnableMonitoring(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.event.Event/EnableMonitoring',
            event__pb2.EnableMonitoringRequest.SerializeToString,
            event__pb2.EnableMonitoringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableMonitoringMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.event.Event/EnableMonitoringMulti',
            event__pb2.EnableMonitoringMultiRequest.SerializeToString,
            event__pb2.EnableMonitoringMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableMonitoring(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.event.Event/DisableMonitoring',
            event__pb2.DisableMonitoringRequest.SerializeToString,
            event__pb2.DisableMonitoringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableMonitoringMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.event.Event/DisableMonitoringMulti',
            event__pb2.DisableMonitoringMultiRequest.SerializeToString,
            event__pb2.DisableMonitoringMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeRealtimeLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/gsdk.event.Event/SubscribeRealtimeLog',
            event__pb2.SubscribeRealtimeLogRequest.SerializeToString,
            event__pb2.EventLog.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.event.Event/GetLog',
            event__pb2.GetLogRequest.SerializeToString,
            event__pb2.GetLogResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLogWithFilter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.event.Event/GetLogWithFilter',
            event__pb2.GetLogWithFilterRequest.SerializeToString,
            event__pb2.GetLogWithFilterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetImageLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.event.Event/GetImageLog',
            event__pb2.GetImageLogRequest.SerializeToString,
            event__pb2.GetImageLogResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetImageFilter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.event.Event/GetImageFilter',
            event__pb2.GetImageFilterRequest.SerializeToString,
            event__pb2.GetImageFilterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetImageFilter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.event.Event/SetImageFilter',
            event__pb2.SetImageFilterRequest.SerializeToString,
            event__pb2.SetImageFilterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetImageFilterMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.event.Event/SetImageFilterMulti',
            event__pb2.SetImageFilterMultiRequest.SerializeToString,
            event__pb2.SetImageFilterMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.event.Event/ClearLog',
            event__pb2.ClearLogRequest.SerializeToString,
            event__pb2.ClearLogResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearLogMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.event.Event/ClearLogMulti',
            event__pb2.ClearLogMultiRequest.SerializeToString,
            event__pb2.ClearLogMultiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
