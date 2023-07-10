from . import Deserializable


class Location(Deserializable):
    __slots__ = ('longitude', 'latitude', 'horizontal_accuracy', 'live_period', 'heading', 'proximity_alert_radius')

    def __init__(self, data, longitude, latitude, horizontal_accuracy, live_period, heading, proximity_alert_radius):
        self.data = data
        self.longitude = longitude
        self.latitude = latitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius

    @classmethod
    def de_json(cls, data):
        data = cls.check_json(data)

        longitude: float = data.get('longitude')
        latitude: float = data.get('latitude')
        horizontal_accuracy: float = data.get('horizontal_accuracy')
        live_period: int = data.get('live_period')
        heading: int = data.get('heading')
        proximity_alert_radius: int = data.get('proximity_alert_radius')
        return Location(data, longitude, latitude, horizontal_accuracy, live_period, heading, proximity_alert_radius)