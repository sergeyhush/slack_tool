from slackclient import SlackClient
from slack_utils import Channel


def test_channel_creation(token):
    with Channel.create(SlackClient(token)) as channel:
        assert channel
