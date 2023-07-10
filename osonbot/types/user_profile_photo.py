from . import Deserializable


class UserPoriflePhoto(Deserializable):
    __slots__ = ('total_count', 'photos')

    def __init__(self, data, total_count, photos):
        self.data = data
        self.total_count = total_count
        self.photos = photos

    @classmethod
    def de_json(cls, data):
        data = cls.check_json(data)

        total_count: int = data.get('total_count')
        photos: list = data.get('photos')
        return UserPoriflePhoto(data, total_count, photos)