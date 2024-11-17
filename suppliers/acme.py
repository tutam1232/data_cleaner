from .base import BaseSupplier
from models.hotel import Hotel
from utils.utils import sanitize_string
from typing import List

class AcmeSupplier(BaseSupplier):

    def __init__(self):
        super().__init__()
        self.url = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme"
        self.id_key = "Id"
        self.destination_id_key = "DestinationId"

    def parse(self, data: list[dict]) -> List[Hotel]:
        cleaned_data = []
        for hotel in data:
            cleaned_hotel = {
                "id": hotel.get(self.id_key,""),
                "destination_id": hotel.get(self.destination_id_key,None),
                "name": hotel.get("Name",""),
                "location":{
                    "lat": hotel.get("Latitude", None),
                    "lng": hotel.get("Longitude",None),
                    "address": hotel.get("Address",""),
                    "city": hotel.get("City",""),
                    "country": hotel.get("Country",""),
                },
                "description": hotel.get("Description",""),
                "amenities": {
                    "general": map(sanitize_string, hotel.get("Facilities",[])),
                    "room": []
                },
                "images": {
                    "rooms": [],
                    "site": [],
                    "amenities": []
                },
                "booking_conditions": []
            }
            cleaned_data.append(Hotel(cleaned_hotel))
        return cleaned_data