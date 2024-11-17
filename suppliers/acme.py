from .base import BaseSupplier
from typing import List
from models.hotel import Hotel
from utils.utils import sanitize_string

class AcmeSupplier(BaseSupplier):

    def __init__(self):
        super().__init__()
        self.url = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme"
        self.id_key = "Id"
        self.destination_id_key = "DestinationId"

    def parse(self, hotels: List[dict]) -> List['Hotel']:
        cleaned_data = []
        for hotel in hotels:
            cleaned_hotel = {
                "id": hotel.get(self.id_key,""),
                "destination_id": hotel.get(self.destination_id_key,None),
                "name": hotel.get("Name","").strip(),
                "location":{
                    "lat": hotel.get("Latitude", None),
                    "lng": hotel.get("Longitude",None),
                    "address": hotel.get("Address","").strip(),
                    "city": hotel.get("City","").strip(),
                    "country": hotel.get("Country","").strip(),
                },
                "description": hotel.get("Description","").strip(),
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