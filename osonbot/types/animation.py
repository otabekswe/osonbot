from . import Deserializable


class Animation(Deserializable):
    __slots__ = ('file_id', 'file_unique_id', 'width', 'height', 'duration', 'thumbnail', 'file_name', 'mime_type',
                 'file_size')

    def __init__(self, data, file_id, file_unique_id, width, height, duration, thumbnail, file_name, mime_type,
                 file_size):
        self.data = data
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
    def de_json(cls, data):
        data = cls.check_json(data)

        file_id: str = data.get('file_id')
        file_unique_id: str = data.get('file_unique_id')
        width: int = data.get('width')
        height: int = data.get('height')
        duration: int = data.get('duration')
        thumbnail: PhotoSize = data.get('thumbnail')
        file_name: str = data.get('file_name')
        mime_type: str = data.get('mime_type')
        file_size = data.get('file_size')

        return Animation(data, file_id, file_unique_id, width, height, duration, thumbnail, file_name, mime_type,
                         file_size)