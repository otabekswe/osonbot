from . import Deserializable


class Contact(Deserializable):
    __slots__ = ('phone_number', 'first_name', 'last_name', 'user_id', 'vcard')

    def __init__(self, phone_number, first_name, last_name, user_id, vcard):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        phone_number: str = raw_data.get('phone_number')
        first_name: str = raw_data.get('first_name')
        last_name: str = raw_data.get('last_name')
        user_id: int = raw_data.get('user_id')
        vcard: str = raw_data.get('vcard')
        return Contact(phone_number, first_name, last_name, user_id, vcard)
