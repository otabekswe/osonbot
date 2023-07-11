import datetime
import time
import json


class Serializable:
    def to_json(self):
        raise NotImplementedError


class Deserializable:
    def to_json(self):
        result = {}
        for key, value in self.__dict__.keys():
            if not value or key == '_bot':
                continue
            if hasattr(value, 'to_json'):
                value = getattr(value, 'to_json')()
            elif isinstance(value, datetime.datetime):
                value = int(time.mktime(value.timetuple()))
            result[key] = value
        return result

    @property
    def bot(self):
        if not hasattr(self, '_bot'):
            raise AttributeError(f"{self.__class__.__name__} isn't configured!")
        return getattr(self, '_bot')

    @bot.setter
    def bot(self, bot):
        setattr(self, '_bot', bot)
        for key, value in self.__dict__.items():
            if isinstance(value, Deserializable):
                value.bot = bot

    @classmethod
    def de_json(cls, raw_data):
        raise NotImplementedError

    @staticmethod
    def check_json(raw_data) -> dict:
        if isinstance(raw_data, dict):
            return raw_data
        elif isinstance(raw_data, str):
            return json.loads(raw_data)
        else:
            raise ValueError('Data should be a json dict or string!')

    def __str__(self):
        return json.dumps(self.to_json())

    def __repr__(self):
        return str(self)