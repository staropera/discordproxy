# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import discord_api_pb2 as discord__api__pb2


class DiscordApiStub(object):
    """Provides access to the Discord API
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendDirectMessage = channel.unary_unary(
                '/discord_api.DiscordApi/SendDirectMessage',
                request_serializer=discord__api__pb2.SendDirectMessageRequest.SerializeToString,
                response_deserializer=discord__api__pb2.SendDirectMessageResponse.FromString,
                )
        self.GetGuildChannels = channel.unary_unary(
                '/discord_api.DiscordApi/GetGuildChannels',
                request_serializer=discord__api__pb2.GetGuildChannelsRequest.SerializeToString,
                response_deserializer=discord__api__pb2.GetGuildChannelsResponse.FromString,
                )


class DiscordApiServicer(object):
    """Provides access to the Discord API
    """

    def SendDirectMessage(self, request, context):
        """Send a direct message to a user
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGuildChannels(self, request, context):
        """Get the list of channel for a guild
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DiscordApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendDirectMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendDirectMessage,
                    request_deserializer=discord__api__pb2.SendDirectMessageRequest.FromString,
                    response_serializer=discord__api__pb2.SendDirectMessageResponse.SerializeToString,
            ),
            'GetGuildChannels': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGuildChannels,
                    request_deserializer=discord__api__pb2.GetGuildChannelsRequest.FromString,
                    response_serializer=discord__api__pb2.GetGuildChannelsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'discord_api.DiscordApi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DiscordApi(object):
    """Provides access to the Discord API
    """

    @staticmethod
    def SendDirectMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/discord_api.DiscordApi/SendDirectMessage',
            discord__api__pb2.SendDirectMessageRequest.SerializeToString,
            discord__api__pb2.SendDirectMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGuildChannels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/discord_api.DiscordApi/GetGuildChannels',
            discord__api__pb2.GetGuildChannelsRequest.SerializeToString,
            discord__api__pb2.GetGuildChannelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
