from .base import BaseSanitizer
from typing import List
from utils.amenities_util import sanitize_string



class PaperfliesSanitizer(BaseSanitizer):
    def __init__(self):
        super().__init__()
        self.id_key = "hotel_id"
        self.destination_id_key = "destination_id"

    def execute(self, hotels: List[dict]):
        cleaned_data = []
        for hotel in hotels:
            cleaned_hotel = {
                "id": hotel.get(self.id_key,""),
                "destination_id": hotel.get(self.destination_id_key,None),
                "name": hotel.get("hotel_name","").strip(),
                "location":{    
                    "lat": None,
                    "lng": None,
                    "address": hotel.get("location", {}).get("address", "").strip(),
                    "country": hotel.get("location", {}).get("country", "").strip(),
                    "city": hotel.get("location", {}).get("city", "").strip()
                },
                "description": hotel.get("details","").strip(),
                "amenities": {
                    "general": map(sanitize_string, hotel.get("amenities",{}).get("general",[])),
                    "room": map(sanitize_string, hotel.get("amenities",{}).get("room",[]))
                },
                "images": {
                    "rooms": [
                        {"link": img["link"], "description": img["caption"].strip()} 
                        for img in hotel.get("images", {}).get("rooms", [])
                    ],
                    "site": [
                        {"link": img["link"], "description": img["caption"].strip()} 
                        for img in hotel.get("images", {}).get("site", [])
                    ],
                    "amenities": [
                        {"link": img["link"], "description": img["caption"].strip()} 
                        for img in hotel.get("images", {}).get("amenities", [])
                    ]

                },
                "booking_conditions": [condition.strip() for condition in hotel.get("booking_conditions", [])]
            }
            cleaned_data.append(cleaned_hotel)
        return cleaned_data