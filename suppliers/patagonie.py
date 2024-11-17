from typing import List
from .base import BaseSupplier
from models.hotel import Hotel
from utils.amenities_util import sanitize_string

class PatagonieSupplier(BaseSupplier):

    def __init__(self):
        super().__init__()
        self.url = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia"
        self.id_key = "id"
        self.destination_id_key = "destination"

    def parse(self, hotels: List[dict]) -> List['Hotel']:
        cleaned_data = []
        for hotel in hotels:
            cleaned_hotel = {
                "id": hotel.get(self.id_key,""),
                "destination_id": hotel.get(self.destination_id_key,None),
                "name": (hotel.get("name") or "").strip(),
                "location":{
                    "lat": hotel.get("lat",None),
                    "lng": hotel.get("lng",None),
                    "address": (hotel.get("address") or "").strip(),
                    "city": "",
                    "country": ""
                },
                "description": (hotel.get("info") or "").strip(),
                "amenities": {
                    "general": map(sanitize_string, hotel.get("amenities") or []),
                    "room": []
                },
                "images": {
                    "rooms": [
                        {"link": img["url"], "description": (img["description"] or "").strip()} 
                        for img in (hotel.get("images") or {}).get("rooms", [])
                    ],
                    "site": [
                        {"link": img["url"], "description": (img["description"] or "").strip()} 
                        for img in (hotel.get("images") or {}).get("site", [])
                    ],
                    "amenities": [
                        {"link": img["url"], "description": (img["description"] or "").strip()} 
                        for img in (hotel.get("images") or {}).get("amenities", [])
                    ]
                },
                "booking_conditions": []
            }
            cleaned_data.append(Hotel(cleaned_hotel))
        return cleaned_data