import json


class Serializable:
    def to_json(self):
        raise NotImplementedError


class Deserializable:
    def to_json(self):
        result = {}
        for item in self.__slots__ or list(self.__dict__.keys()):
            attribute = getattr(self, item)
            if not attribute:
                continue
            if hasattr(attribute, 'to_json'):
                attribute = getattr(attribute, 'to_json')
                attribute = attribute()
            result[item] = attribute
        return result

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