from . import Deserializable
from .user import User


class MessageEntity(Deserializable):
    __slots__ = ('data', 'type', 'offset', 'length', 'url', 'user')

    def __init__(self, data, type, offset, length, url, user):
        self.data = data
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user

    @classmethod
    def _parse_user(cls, user):
        return User.de_json(user) if user else None

    @classmethod
    def de_json(cls, data):
        data = cls.check_json(data)

        type = data.get('type')
        offset = data.get('offset')
        length = data.get('length')
        url = data.get('url')
        user = cls._parse_user(data.get('user'))

        return MessageEntity(data, type, offset, length, url, user)


class MessageEntityType:
    MENTION = 'mention'
    HASHTAG = 'hashtag'
    BOT_COMMAND = 'bot_command'
    URL = 'url'
    EMAIL = 'email'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    PRE = 'pre'
    TEXT_LINK = 'text_link'
    TEXT_MENTION = 'text_mention'


class ChatAction:
    TYPING = 'typing'
    UPLOAD_PHOTO = 'upload_photo'
    RECORD_VIDEO = 'record_video'
    UPLOAD_VIDEO = 'upload_video'
    RECORD_AUDIO = 'record_audio'
    UPLOAD_AUDIO = 'upload_audio'
    UPLOAD_DOCUMENT = 'upload_document'
    FIND_LOCATION = 'find_location'
    RECORD_VIDEO_NOTE = 'record_video_note'
    UPLOAD_VIDEO_NOTE = 'upload_video_note'