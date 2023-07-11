from . import Deserializable


class ReplyKeyboardMarkup(Deserializable):
    def __init__(self, keyboard, is_persistent, resize_keyboard, one_time_keyboard, input_field_placeholder, selective):
        self.keyboard = keyboard
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        keyboard: list = raw_data.get('keyboard')
        is_persistent: bool = raw_data.get('is_persistent')
        resize_keyboard: bool = raw_data.get('resize_keyboard')
        one_time_keyboard: bool = raw_data.get('one_time_keyboard')
        input_field_placeholder: str = raw_data.get('input_field_placeholder')
        selective: bool = raw_data.get('selective')
        return ReplyKeyboardMarkup(keyboard, is_persistent, resize_keyboard, one_time_keyboard, input_field_placeholder,
                                   selective)