import asyncio
import aiohttp

from . import api
from .api import ApiMethod
from .types.user import User
from .types.chat import Chat
from .types.update import Update
from .utils.payload import generate_payload


class OsonBot:
    def __init__(self, token, loop=None, connections_limit=10):
        api.check_token(token)
        self._token = token

        if loop is None:
            loop = asyncio.get_event_loop()

        self.loop = loop
        self.session = aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(limit=connections_limit),
            loop=self.loop
        )

    def __del__(self):
        self.session.close()

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

    async def get_chat(self, chat_id) -> User:
        payload = generate_payload(**locals())
        raw = await self.request(ApiMethod.GET_CHAT, payload)
        return Chat.de_json(raw)

    async def get_updates(self, offset=None, limit=None, timeout=None, allowed_updates=None):
        payload = generate_payload(**locals())

        raw = await self.request(ApiMethod.GET_UPDATES, payload)
        return [Update.de_json(raw_update) for raw_update in raw]
