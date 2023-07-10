from . import Deserializable


class PhotoSize(Deserializable):
    __slots__ = ('file_id', 'file_unique_id', 'width', 'height', 'file_size')

    def __init__(self, file_id, file_unique_id, width, height, file_size):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        file_id: str = raw_data.get('file_id')
        file_unique_id: str = raw_data.get('file_unique_id')
        width: int = raw_data.get('width')
        height: int = raw_data.get('height')
        file_size: int = raw_data.get('file_size')
        return PhotoSize(file_id, file_unique_id, width, height, file_size)