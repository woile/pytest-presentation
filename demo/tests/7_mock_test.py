from unittest import mock


class Serializer:
    def __init__(self, protocol):
        self.protocol = protocol

    def serialize(self, payload):
        return self.protocol.serialize(payload)


def test_serialize():
    mock_protocol = mock.Mock()
    s = Serializer(mock_protocol)
    payload = {"name": "jon"}
    s.serialize(payload)
    mock_protocol.serialize.assert_called_with(payload)
