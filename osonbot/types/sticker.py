from . import Deserializable
from .photo_size import PhotoSize


class Sticker(Deserializable):
    __slots__ = ('data', 'file_id', 'width', 'height', 'thumbnail', 'emoji', 'file_size')

    def __init__(self, data, file_id, width, height, thumbnail, emoji, file_size):
        self.data = data
        self.file_id = file_id
        self.width = width
        self.height = height
        self.thumbnail = thumbnail
        self.emoji = emoji
        self.file_size = file_size

    @classmethod
    def de_json(cls, data):
        data = cls.check_json(data)

        file_id: str = data.get('file_id')
        width: int = data.get('width')
        height: int = data.get('height')
        thumbnail: PhotoSize = data.get('thumbnail')
        emoji: str = data.get('emoji')
        file_size: int = data.get('file_size')
        return Sticker(data, file_id, width, height, thumbnail, emoji, file_size)