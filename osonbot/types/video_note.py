from . import Deserializable
from .photo_size import PhotoSize


class VideoNote(Deserializable):
    __slots__ = ('file_id', 'file_unique_id', 'length', 'duration', 'thumbnail', 'file_size')

    def __init__(self, data, file_id, file_unique_id, length, duration, thumbnail, file_size):
        self.data = data
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_size = file_size

    @classmethod
    def de_json(cls, data):
        data = cls.check_json(data)

        file_id: str = data.get('file_id')
        file_unique_id: str = data.get('file_unique_id')
        length: int = data.get('length')
        duration = data.get('duration')
        thumbnail: PhotoSize = data.get('thumbnail')
        file_size: int = data.get('file_size')
        return VideoNote(data, file_id, file_unique_id, length, duration, thumbnail, file_size)