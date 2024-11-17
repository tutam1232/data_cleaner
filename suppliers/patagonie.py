from typing import List
from .base import BaseSupplier
from models.hotel import Hotel
from utils.utils import sanitize_string

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
                "name": hotel.get("name","").strip(),
                "location":{
                    "lat": hotel.get("lat",None),
                    "lng": hotel.get("lng",None),
                    "address": hotel.get("address","").strip(),
                    "city": "",
                    "country": ""
                },
                "description": hotel.get("info","").strip(),
                "amenities": {
                    "general": map(sanitize_string, hotel.get("amenities",[])),
                    "room": []
                },
                "images": {
                    "rooms": [
                        {"link": img["url"], "description": img["description"].strip()} 
                        for img in hotel.get("images", {}).get("rooms", [])
                    ],
                    "site": [
                        {"link": img["url"], "description": img["description"].strip()} 
                        for img in hotel.get("images", {}).get("site", [])
                    ],
                    "amenities": [
                        {"link": img["url"], "description": img["description"].strip()} 
                        for img in hotel.get("images", {}).get("amenities", [])
                    ]
                },
                "booking_conditions": []
            }
            cleaned_data.append(Hotel(cleaned_hotel))
        return cleaned_data