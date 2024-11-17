from dataclasses import dataclass, field
from typing import List

@dataclass
class Image:
    link: str
    description: str

    def __init__(self, data: dict):
        self.link = data.get("link","")
        self.description = data.get("description","")

    def get_data(self):
        return {
            "link": self.link,
            "description": self.description
        }
    def is_the_same(self, other: 'Image'):
        return self.link == other.link;

@dataclass
class ImageCollection:
    rooms: List[Image] = field(default_factory=list)
    site: List[Image] = field(default_factory=list)
    amenities: List[Image] = field(default_factory=list)

    def __init__(self, data: dict):
        self.rooms = [Image(img) for img in data.get('rooms', [])]
        self.site = [Image(img) for img in data.get('site', [])]
        self.amenities = [Image(img) for img in data.get('amenities', [])]

    def get_data(self):
        return {
            "rooms": [img.get_data() for img in self.rooms],
            "site": [img.get_data() for img in self.site],
            "amenities": [img.get_data() for img in self.amenities]
        }
    
    def merge(self, other: 'ImageCollection'):
        for room in other.rooms:
            if not any(img.is_the_same(room) for img in self.rooms):
                self.rooms.append(room)
        for site in other.site:
            if not any(img.is_the_same(site) for img in self.site):
                self.site.append(site)
        for amenity in other.amenities:
            if not any(img.is_the_same(amenity) for img in self.amenities):
                self.amenities.append(amenity)

