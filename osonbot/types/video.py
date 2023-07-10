from . import Deserializable
from .photo_size import PhotoSize


class Video(Deserializable):
    __slots__ = ('file_id', 'file_unique_id', 'width', 'height', 'duration', 'thumbnail', 'file_name', 'mime_type',
                 'file_size')

    def __init__(self, file_id, file_unique_id, width, height, duration, thumbnail, file_name, mime_type,
                 file_size):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        file_id: str = raw_data.get('file_id')
        file_unique_id: str = raw_data.get('file_unique_id')
        width: int = raw_data.get('width')
        height: int = raw_data.get('height')
        duration: int = raw_data.get('duration')
        thumbnail: PhotoSize = raw_data.get('thumbnail')
        file_name: str = raw_data.get('file_name')
        mime_type: str = raw_data.get('mime_type')
        file_size: int = raw_data.get('file_size')
        return Video(file_id, file_unique_id, width, height, duration, thumbnail, file_name, mime_type, file_size)