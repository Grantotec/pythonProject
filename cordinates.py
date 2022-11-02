import requests
import json
from typing import NamedTuple


class Cordinates(NamedTuple):
    latitude: float
    longitude: float


class GPS:
    __slots__ = ['__latitude', '__longitude']


    def __init__(self):
        send_url = "http://api.ipstack.com/check?access_key=d71baf765e56c2bf54a6e5e30511db30"
        geo_req = requests.get(send_url)
        geo_json = json.loads(geo_req.text)
        self.__latitude = geo_json['latitude']
        self.__longitude = geo_json['longitude']

    @property
    def latitude(self) -> Cordinates:
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude):
        self.__latitude = latitude

send_url = "http://api.ipstack.com/check?access_key=d71baf765e56c2bf54a6e5e30511db30"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']
