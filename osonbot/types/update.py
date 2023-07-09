from osonbot.types import Deserializable
from osonbot.types.message import Message


class Update(Deserializable):
    __slots__ = (
        'data', 'update_id', 'message', 'edited_message', 'channel_post', 'edited_channel_post', 'inline_query',
        'chosen_inline_result', 'callback_query', 'shipping_query', 'pre_checkout_query' )

    def __init__(self, data, update_id, message, edited_message, channel_post, edited_channel_post, inline_query,
                 chosen_inline_result, callback_query, shipping_query, pre_checkout_query):
        self.data = data
        self.update_id = update_id
        self.message: Message = message
        self.edited_message: Message = edited_message
        self.channel_post: Message = channel_post
        self.edited_channel_post: Message = edited_channel_post
        self.inline_query = inline_query
        self.chosen_inline_result = chosen_inline_result
        self.callback_query = callback_query
        self.shipping_query = shipping_query
        self.pre_checkout_query = pre_checkout_query

    @classmethod
    def _parse_message(cls, message):
        return Message.de_json(message) if message else None

    @classmethod
    def de_json(cls, data):
        data = cls.check_json(data)

        update_id = data.get('data')
        message = cls._parse_message(data.get('message'))
        edited_message = cls._parse_message(data.get('edited_message'))
        channel_post = cls._parse_message(data.get('channel_post'))
        edited_channel_post = cls._parse_message(data.get('edited_channel_post'))

        inline_query = data.get('inline_query')
        chosen_inline_result = data.get('chosen_inline_result')
        callback_query = data.get('callback_query')
        shipping_query = data.get('shipping_query')
        pre_checkout_query = data.get('pre_checkout_query')

        return Update(data, update_id, message, edited_message, channel_post, edited_channel_post, inline_query,
                      chosen_inline_result, callback_query, shipping_query, pre_checkout_query)

