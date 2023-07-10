from . import Deserializable
from .photo_size import PhotoSize


class Audio(Deserializable):
    __slots__ = ('field_id', 'file_unique_id', 'duration', 'performer', 'title', 'file_name', 'mime_type', 'file_size',
                 'thumbnail')

    def __init__(self, field_id, file_unique_id, duration, performer, title, file_name, mime_type, file_size,
                 thumbnail):
        self.field_id = field_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumbnail = thumbnail

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        field_id: str = raw_data.get('field_id')
        file_unique_id: str = raw_data.get('file_unique_id')
        duration: int = raw_data.get('duration')
        performer: str = raw_data.get('performer')
        title: str = raw_data.get('title')
        file_name: str = raw_data.get('file_name')
        mime_type: str = raw_data.get('mime_type')
        file_size: int = raw_data.get('file_size')
        thumbnail: PhotoSize = raw_data.get('thumbnail')

        return Audio(field_id, file_unique_id, duration, performer, title, file_name, mime_type, file_size,
                     thumbnail)