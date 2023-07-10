from . import Deserializable
from .location import Location


class Venue(Deserializable):
    __slots__ = ('location', 'title', 'address', 'foursquare_id', 'foursquare_type', 'google_place_id', 'google_place_type')

    def __init__(self, location, title, address, foursquare_id, foursquare_type, google_place_id, google_place_type):
        self.location = location
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        location: Location = raw_data.get('location')
        title: str = raw_data.get('title')
        address: str = raw_data.get('address')
        foursquare_id: str = raw_data.get('foursquare_id')
        foursquare_type: str = raw_data.get('foursquare_type')
        google_place_id: str = raw_data.get('google_place_id')
        google_place_type: str = raw_data.get('google_place_type')
        return Venue(location, title, address, foursquare_id, foursquare_type, google_place_id, google_place_type)