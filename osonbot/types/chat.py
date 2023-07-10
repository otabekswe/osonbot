from . import Deserializable


class Chat(Deserializable):
    __slots__ = ('id', 'type', 'title', 'username', 'first_name', 'last_name', 'all_members_are_administrators')

    def __init__(self, data, id, type, title, username, first_name, last_name, all_members_are_administrators):
        self.data = data

        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.all_members_are_administrators = all_members_are_administrators

    @classmethod
    def de_json(cls, data) -> 'Chat':
        data = cls.check_json(data)

        id: int = data.get('id')
        type: str = data.get('type')
        title: str = data.get('title')
        username: str = data.get('username')
        first_name: str = data.get('first_name')
        last_name: str = data.get('last_name')
        all_members_are_administrators: bool = data.get('all_members_are_administrators')

        return Chat(data, id, type, title, username, first_name, last_name, all_members_are_administrators)

    async def send_message(self, text):
        self.bot.send_message(self.id, text)

    @property
    def full_name(self):
        if self.type == ChatType.PRIVATE:
            full_name = self.first_name
            if self.last_name:
                full_name += ' ' + self.last_name
            return full_name
        return self.title

    @property
    def mention(self):
        if self.username:
            return '@' + self.username
        if self.type == ChatType.PRIVATE:
            return self.full_name
        return None


class ChatType:
    PRIVATE = 'private'
    GROUP = 'group'
    SUPERGROUP = 'supergroup'
    CHANNEL = 'channel'


