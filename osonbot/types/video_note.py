from . import Deserializable
from .photo_size import PhotoSize


class VideoNote(Deserializable):
    def __init__(self, file_id, file_unique_id, length, duration, thumbnail, file_size):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_size = file_size

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        file_id: str = raw_data.get('file_id')
        file_unique_id: str = raw_data.get('file_unique_id')
        length: int = raw_data.get('length')
        duration = raw_data.get('duration')
        thumbnail: PhotoSize = raw_data.get('thumbnail')
        file_size: int = raw_data.get('file_size')
        return VideoNote(file_id, file_unique_id, length, duration, thumbnail, file_size)