import grpc

from discordproxy.discord_api_pb2 import (
    SendDirectMessageRequest,
    GetGuildChannelsRequest,
    Embed,
)
from discordproxy.discord_api_pb2_grpc import DiscordApiStub


def send_direct_message(user_id):
    with grpc.insecure_channel("localhost:50051") as channel:
        client = DiscordApiStub(channel)
        request = SendDirectMessageRequest(
            user_id=user_id,
            content="Hey, stranger!",
            embed=Embed(
                description="more info!",
                thumbnail=Embed.Thumbnail(
                    url="https://images.evetech.net/characters/93330670/portrait?size=128"
                ),
            ),
        )
        try:
            message = client.SendDirectMessage(request)
        except grpc.RpcError as e:
            print(f"Code: {e.code()}")
            print(f"Details: {e.details()}")
        else:
            print(message)


def get_channels(guild_id):
    with grpc.insecure_channel("localhost:50051") as channel:
        client = DiscordApiStub(channel)
        request = GetGuildChannelsRequest(guild_id=197097249610661888)
        try:
            channels = client.GetGuildChannels(request)
        except grpc.RpcError as e:
            print(f"Code: {e.code()}")
            print(f"Details: {e.details()}")
        else:
            print(channels)


if __name__ == "__main__":
    send_direct_message(152878250039705600)  # 152878250039705600
