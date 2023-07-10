from . import Deserializable


class File(Deserializable):
    __slots__ = ('file_id', 'file_unique_id', 'file_size', 'file_path')

    def __init__(self, data, file_id, file_unique_id, file_size, file_path):
        self.data = data
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_path = file_path

    @classmethod
    def de_json(cls, data):
        data = cls.check_json(data)

        file_id: str = data.get('file_id')
        file_unique_id: str = data.get('file_unique_id')
        file_size: str = data.get('file_size')
        file_path: str = data.get('file_path')
        return File(data, file_id, file_unique_id, file_size, file_path)