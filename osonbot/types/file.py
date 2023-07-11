from . import Deserializable


class File(Deserializable):
    def __init__(self, file_id, file_unique_id, file_size, file_path):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_path = file_path

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        file_id: str = raw_data.get('file_id')
        file_unique_id: str = raw_data.get('file_unique_id')
        file_size: str = raw_data.get('file_size')
        file_path: str = raw_data.get('file_path')
        return File(file_id, file_unique_id, file_size, file_path)