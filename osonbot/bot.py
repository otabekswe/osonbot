import asyncio
import aiohttp

from . import api
from .api import ApiMethod
from .types.user import User
from .types.chat import Chat
from .types.update import Update
from .utils.payload import generate_payload
from .types.message import Message


class OsonBot:
    def __init__(self, token, loop=None, connections_limit=10):
        api.check_token(token)
        self._token = token

        if loop is None:
            loop = asyncio.get_event_loop()

        self.loop = loop
        self.session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=connections_limit), loop=self.loop)

    def __on_exit(self):
        self.session.close()

    def prepare_object(self, obj):
        obj.bot = self
        return obj

    @property
    async def me(self) -> User:
        if not hasattr(self, '_me'):
            setattr(self, '_me', await self.get_me())
        return getattr(self, '_me')

    async def request(self, method, data=None):
        return await api.request(self.session, self._token, method, data)

    async def get_me(self) -> User:
        raw = await self.request(ApiMethod.GET_ME)
        return User.de_json(raw)

    async def send_message(self, chat_id, text, parse_mode=None, disable_web_page_preview=None, disable_notification=None,
                           protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None):
        payload = generate_payload(**locals())
        # For replying Markups
        if reply_markup:
            pass

        message = await self.request(ApiMethod.SEND_MESSAGE, payload)
        return self.prepare_object(Message.de_json(message))

    async def delete_message(self, chat_id, message_id):
        payload = generate_payload(**locals())
        await self.request(ApiMethod.DELETE_MESSAGE, payload)
        return True

    async def edit_message(self, chat_id, message_id, text, inline_message_id=None, parse_mode=None,
                           disable_web_page_preview=None, reply_markup=None):
        payload = generate_payload(**locals())
        return self.request(ApiMethod.EDIT_MESSAGE_TEXT, payload)

    async def forward_message(self, from_chat_id, chat_id, message_id, disable_notification=None,
                              protect_content=None):
        payload = generate_payload(**locals())
        message = self.request(ApiMethod.FORWARD_MESSAGE, payload)
        return self.prepare_object(Message.de_json(message))

    async def get_chat(self, chat_id) -> User:
        payload = generate_payload(**locals())
        raw = await self.request(ApiMethod.GET_CHAT, payload)
        return self.prepare_object(Chat.de_json(raw))

    async def get_updates(self, offset=None, limit=None, timeout=None, allowed_updates=None):
        payload = generate_payload(**locals())

        raw = await self.request(ApiMethod.GET_UPDATES, payload)
        return [Update.de_json(raw_update) for raw_update in raw]
