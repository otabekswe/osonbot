from . import Deserializable
from .location import Location


class Venue(Deserializable):
    __slots__ = ('location', 'title', 'address', 'foursquare_id', 'foursquare_type', 'google_place_id', 'google_place_type')

    def __init__(self, data, location, title, address, foursquare_id, foursquare_type, google_place_id, google_place_type):
        self.data = data
        self.location = location
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type

    @classmethod
    def de_json(cls, data):
        data = cls.check_json(data)

        location: Location = data.get('location')
        title: str = data.get('title')
        address: str = data.get('address')
        foursquare_id: str = data.get('foursquare_id')
        foursquare_type: str = data.get('foursquare_type')
        google_place_id: str = data.get('google_place_id')
        google_place_type: str = data.get('google_place_type')
        return Venue(data, location, title, address, foursquare_id, foursquare_type, google_place_id, google_place_type)