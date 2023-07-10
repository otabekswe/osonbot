from . import Deserializable
from .photo_size import PhotoSize


class Sticker(Deserializable):
    __slots__ = ('file_id', 'width', 'height', 'thumbnail', 'emoji', 'file_size')

    def __init__(self, file_id, width, height, thumbnail, emoji, file_size):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.thumbnail = thumbnail
        self.emoji = emoji
        self.file_size = file_size

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        file_id: str = raw_data.get('file_id')
        width: int = raw_data.get('width')
        height: int = raw_data.get('height')
        thumbnail: PhotoSize = raw_data.get('thumbnail')
        emoji: str = raw_data.get('emoji')
        file_size: int = raw_data.get('file_size')
        return Sticker(file_id, width, height, thumbnail, emoji, file_size)