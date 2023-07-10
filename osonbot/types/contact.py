from . import Deserializable


class Contact(Deserializable):
    __slots__ = ('phone_number', 'first_name', 'last_name', 'user_id', 'vcard')

    def __init__(self, data, phone_number, first_name, last_name, user_id, vcard):
        self.data = data
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard

    @classmethod
    def de_json(cls, data):
        data = cls.check_json(data)

        phone_number: str = data.get('phone_number')
        first_name: str = data.get('first_name')
        last_name: str = data.get('last_name')
        user_id: int = data.get('user_id')
        vcard: str = data.get('vcard')
        return Contact(data, phone_number, first_name, last_name, user_id, vcard)
