from . import Deserializable
from .user import User


class ChatMember(Deserializable):
    def __init__(self, status, user, is_anonymous, custom_title):
        self.status = status
        self.user = user
        self.is_anonymous = is_anonymous
        self.custom_title = custom_title

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        status: str = raw_data.get('status')
        user: User = raw_data.get('user')
        is_anonymous: bool = raw_data.get('is_anonymous')
        custom_title: str = raw_data.get('custom_title')
        return ChatMember(status, user, is_anonymous, custom_title)


class ChatMemberStatus:
    OWNER = 'creator'
    ADMINISTRATOR = 'administrator'
    MEMBER = 'member'
    RESTRICTED = 'restricted'
    LEFT = 'left'
    BANNED = 'kicked'

    @classmethod
    def is_admin(cls, status):
        return status in (cls.ADMINISTRATOR, cls.OWNER)

    @classmethod
    def is_member(cls, status):
        return status in (cls.MEMBER, cls.OWNER, cls.ADMINISTRATOR)
