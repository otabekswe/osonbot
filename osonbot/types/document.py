from . import Deserializable


class Document(Deserializable):
    __slots__ = ('file_id', 'file_unique_id', 'thumbnail', 'file_name', 'mime_type', 'file_size')

    def __init__(self, data, file_id, file_unique_id, thumbnail, file_name, mime_type, file_size):
        self.data = data
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @classmethod
    def de_json(cls, data):
        data = cls.check_json(data)

        file_id: str = data.get('file_id')
        file_unique_id: str = data.get('file_unique_id')
        thumbnail: PhotoSize = data.get('thumbnail')
        file_name: str = data.get('file_name')
        mime_type: str = data.get('mime_type')
        file_size: str = data.get('file_size')

        return Document(data, file_id, file_unique_id, thumbnail, file_name, mime_type, file_size)
