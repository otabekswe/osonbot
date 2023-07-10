from . import Deserializable
from .photo_size import PhotoSize


class Audio(Deserializable):
    __slots__ = ('field_id', 'file_unique_id', 'duration', 'performer', 'title', 'file_name', 'mime_type', 'file_size',
                 'thumbnail')

    def __init__(self, data, field_id, file_unique_id, duration, performer, title, file_name, mime_type, file_size,
                 thumbnail):
        self.data = data
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
    def de_json(cls, data):
        data = cls.check_json(data)

        field_id: str = data.get('field_id')
        file_unique_id: str = data.get('file_unique_id')
        duration: int = data.get('duration')
        performer: str = data.get('performer')
        title: str = data.get('title')
        file_name: str = data.get('file_name')
        mime_type: str = data.get('mime_type')
        file_size: int = data.get('file_size')
        thumbnail: PhotoSize = data.get('thumbnail')

        return Audio(data, field_id, file_unique_id, duration, performer, title, file_name, mime_type, file_size,
                     thumbnail)