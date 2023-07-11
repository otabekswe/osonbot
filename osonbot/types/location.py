from . import Deserializable


class Location(Deserializable):
    def __init__(self, longitude, latitude, horizontal_accuracy, live_period, heading, proximity_alert_radius):
        self.longitude = longitude
        self.latitude = latitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        longitude: float = raw_data.get('longitude')
        latitude: float = raw_data.get('latitude')
        horizontal_accuracy: float = raw_data.get('horizontal_accuracy')
        live_period: int = raw_data.get('live_period')
        heading: int = raw_data.get('heading')
        proximity_alert_radius: int = raw_data.get('proximity_alert_radius')
        return Location(longitude, latitude, horizontal_accuracy, live_period, heading, proximity_alert_radius)