from . import Deserializable


class PhotoSize(Deserializable):
    __slots__ = ('file_id', 'file_unique_id', 'width', 'height', 'file_size')

    def __init__(self, data, file_id, file_unique_id, width, height, file_size):
        self.data = data
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size

    @classmethod
    def de_json(cls, data):
        data = cls.check_json(data)

        file_id: str = data.get('file_id')
        file_unique_id: str = data.get('file_unique_id')
        width: int = data.get('width')
        height: int = data.get('height')
        file_size: int = data.get('file_size')
        return PhotoSize(data, file_id, file_unique_id, width, height, file_size)