from . import Deserializable


class ReplyKeyboardMarkup(Deserializable):
    __slots__ = ('keyboard', 'is_persistent', 'resize_keyboard', 'one_time_keyboard', 'input_field_placeholder', 'selective')

    def __init__(self, data, keyboard, is_persistent, resize_keyboard, one_time_keyboard, input_field_placeholder, selective):
        self.data = data
        self.keyboard = keyboard
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective

    @classmethod
    def de_json(cls, data):
        data = cls.check_json(data)

        keyboard: list = data.get('keyboard')
        is_persistent: bool = data.get('is_persistent')
        resize_keyboard: bool = data.get('resize_keyboard')
        one_time_keyboard: bool = data.get('one_time_keyboard')
        input_field_placeholder: str = data.get('input_field_placeholder')
        selective: bool = data.get('selective')
        return ReplyKeyboardMarkup(data, keyboard, is_persistent, resize_keyboard, one_time_keyboard,
                                   input_field_placeholder, selective)