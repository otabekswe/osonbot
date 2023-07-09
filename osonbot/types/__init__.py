import json


class Serializable:
    def to_json(self):
        raise NotImplementedError


class Deserializable:
    def to_json(self):
        return getattr(self, 'data', {})

    @classmethod
    def de_json(cls, data):
        raise NotImplementedError

    @staticmethod
    def check_json(data) -> dict:
        if isinstance(data, dict):
            return data
        elif isinstance(data, str):
            return json.loads(data)
        else:
            raise ValueError('Data should be a json dict or string!')

    def __str__(self):
        return json.dumps(self.to_json())

    def __repr__(self):
        return str(self)