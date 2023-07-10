from . import Deserializable


class Diece(Deserializable):
    __slots__ = ('emoji', 'value')

    def __init__(self, emoji, value):
        self.emoji = emoji
        self.value = value

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        emoji: str = raw_data.get('emoji')
        value: int = raw_data.get('value')
        return Diece(emoji, value)
