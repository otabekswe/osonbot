from . import Deserializable
from .user import User
from .message import Message


class CallbackQuery(Deserializable):
    __slots__ = ('id', 'from', 'message', 'inline_message_id', 'chat_instance', 'cq_data', 'game_short_name')

    def __init__(self, id, from_user, message, inline_message_id, chat_instance, cq_data, game_short_name):
        self.id = id
        self.from_user = from_user
        self.message = message
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.cq_data = cq_data
        self.game_short_name = game_short_name

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        id: str = raw_data.get('id')
        from_user: User = raw_data.get('from_user')
        message: Message = raw_data.get('message')
        inline_message_id: str = raw_data.get('inline_message_id')
        chat_instance: str = raw_data.get('chat_instance')
        cq_data: str = raw_data.get('cq_data')
        game_short_name: str = raw_data.get('game_short_name')
        return CallbackQuery(id, from_user, message, inline_message_id, chat_instance, cq_data, game_short_name)