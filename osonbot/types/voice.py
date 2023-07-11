from . import Deserializable


class Voice(Deserializable):
    def __init__(self, file_id, file_unique_id, duration, mime_type, file_size):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        file_id: str = raw_data.get('file_id')
        file_unique_id: str = raw_data.get('file_unique_id')
        duration: int = raw_data.get('duration')
        mime_type: str = raw_data.get('mime_type')
        file_size: int = raw_data.get('file_size')
        return Voice(file_id, file_unique_id, duration, mime_type, file_size)