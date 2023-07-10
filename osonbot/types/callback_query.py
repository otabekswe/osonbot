from . import Deserializable
from osonbot.types.user import User
from osonbot.types.message import Message


class CallbackQuery(Deserializable):
    __slots__ = ('id', 'from', 'message', 'inline_message_id', 'chat_instance', 'cq_data', 'game_short_name')

    def __init__(self, data, id, from_user, message, inline_message_id, chat_instance, cq_data, game_short_name):
        self.data = data
        self.id = id
        self.from_user = from_user
        self.message = message
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.cq_data = cq_data
        self.game_short_name = game_short_name

    @classmethod
    def de_json(cls, data):
        data = cls.check_json(data)

        id: str = data.get('id')
        from_user: User = data.get('from_user')
        message: Message = data.get('message')
        inline_message_id: str = data.get('inline_message_id')
        chat_instance: str = data.get('chat_instance')
        cq_data: str = data.get('cq_data')
        game_short_name: str = data.get('game_short_name')
        return CallbackQuery(data, id, from_user, message, inline_message_id, chat_instance, cq_data, game_short_name)