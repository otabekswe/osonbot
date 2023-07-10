from . import Deserializable


class Diece(Deserializable):
    __slots__ = ('emoji', 'value')

    def __init__(self, data, emoji, value):
        self.data = data
        self.emoji = emoji
        self.value = value

    @classmethod
    def de_json(cls, data):
        data = cls.check_json(data)

        emoji: str = data.get('emoji')
        value: int = data.get('value')
        return Diece(data, emoji, value)
