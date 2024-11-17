from typing import List
from .base import BaseSupplier
from models.hotel import Hotel
from utils.utils import sanitize_string

class PaperfliesSupplier(BaseSupplier):

    def __init__(self):
        super().__init__()
        self.url = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies"
        self.id_key = "hotel_id"
        self.destination_id_key = "destination_id"

    def parse(self, hotels: List[dict]) -> List['Hotel']:
        cleaned_data = []
        for hotel in hotels:
            cleaned_hotel = {
                "id": hotel.get(self.id_key,""),
                "destination_id": hotel.get(self.destination_id_key,None),
                "name": (hotel.get("hotel_name") or "").strip(),
                "location":{    
                    "lat": None,
                    "lng": None,
                    "address": (hotel.get("location", {}).get("address") or "").strip(),
                    "country": (hotel.get("location", {}).get("country") or "").strip(),
                    "city": (hotel.get("location", {}).get("city") or "").strip()
                },
                "description": (hotel.get("details") or "").strip(),
                "amenities": {
                    "general": map(sanitize_string, (hotel.get("amenities") or {}).get("general",[])),
                    "room": map(sanitize_string, (hotel.get("amenities") or {}).get("room",[]))
                },
                "images": {
                    "rooms": [
                        {"link": img["link"], "description": (img["caption"] or "").strip()} 
                        for img in (hotel.get("images") or {}).get("rooms", [])
                    ],
                    "site": [
                        {"link": img["link"], "description": (img["caption"] or "").strip()} 
                        for img in (hotel.get("images") or {}).get("site", [])
                    ],
                    "amenities": [
                        {"link": img["link"], "description": (img["caption"] or "").strip()} 
                        for img in (hotel.get("images") or {}).get("amenities", [])
                    ]

                },
                "booking_conditions": [condition.strip() for condition in hotel.get("booking_conditions", [])]
            }
            cleaned_data.append(Hotel(cleaned_hotel))
        return cleaned_data