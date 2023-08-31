# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import communication_pb2 as communication__pb2


class CommunicationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendRequest = channel.unary_unary(
                '/communication.Communication/SendRequest',
                request_serializer=communication__pb2.Request.SerializeToString,
                response_deserializer=communication__pb2.Response.FromString,
                )


class CommunicationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommunicationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.SendRequest,
                    request_deserializer=communication__pb2.Request.FromString,
                    response_serializer=communication__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'communication.Communication', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Communication(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/communication.Communication/SendRequest',
            communication__pb2.Request.SerializeToString,
            communication__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
