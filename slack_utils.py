import string
import random

__version__ = '0.1'


# Thanks to https://goo.gl/xhaVJ2
def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))


class Channel(object):
    """Slack channel wrapper"""

    @staticmethod
    def create(client, name=None):
        """Create channel"""
        if not name:
            name = 'channel-' + randomword(8)
        resp = client.api_call('channels.create', name=name)
        return Channel(client, resp['channel']['id'])

    def __init__(self, client, channel_id):
        self.client = client
        self.channel_id = channel_id

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.archive()

    def archive(self):
        """Archive channel"""
        return self.client.api_call('channels.archive', channel=self.channel_id)

    def history(self):
        """Channel history"""
        return self.client.api_call('channels.history', channel=self.channel_id)
