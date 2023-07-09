from osonbot.types import Deserializable
from osonbot.utils.user_language import get_language


class User(Deserializable):
    __slots__ = ('data', 'id', 'first_name', 'last_name', 'username', 'language_code')

    def __init__(self, data, id, first_name, last_name, username, language_code):
        self.data: dict = data
        self.id: int = id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.username: str = username
        self.language_code: str = language_code

    @classmethod
    def de_json(cls, data: str or dict) -> 'User':
        data = cls.check_json(data)

        id = data.get('id')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        language_code = data.get('language_code')

        return User(data, id, first_name, last_name, username, language_code)

    @property
    def full_name(self):
        full_name = self.first_name
        if self.last_name:
            full_name += ' ' + self.last_name
        return full_name

    @property
    def mention(self):
        if self.username:
            return '@' + self.username
        return self.full_name

    @property
    def language(self):
        if not self.language_code:
            return None
        return get_language(self.language_code)
