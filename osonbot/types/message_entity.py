from . import Deserializable
from .user import User


class MessageEntity(Deserializable):
    def __init__(self, type, offset, length, url, user):
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user

    @classmethod
    def _parse_user(cls, user):
        return User.de_json(user) if user else None

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        type = raw_data.get('type')
        offset = raw_data.get('offset')
        length = raw_data.get('length')
        url = raw_data.get('url')
        user = cls._parse_user(raw_data.get('user'))

        return MessageEntity(type, offset, length, url, user)


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