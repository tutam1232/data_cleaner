from dataclasses import dataclass, field
from typing import Set
from .location import Location
from .amenities import Amenities
from .images import ImageCollection

@dataclass
class Hotel:
    id: str
    destination_id: int
    name: str
    location: Location
    description: str
    amenities: Amenities = field(default_factory=Amenities)
    images: ImageCollection = field(default_factory=ImageCollection)
    booking_conditions: Set[str] = field(default_factory=set)

    def __init__(self, data: dict):
        # get data from dict
        self.id = data.get("id","")
        self.destination_id = data.get("destination_id",None)
        self.name = data.get("name","")
        self.location = Location(data.get("location",{}))
        self.description = data.get("description","")
        self.amenities = Amenities(data.get("amenities",{}))
        self.images = ImageCollection(data.get("images",{}))
        self.booking_conditions = set(data.get("booking_conditions",[]))

        # strip string
        self.name = self.name.strip()
        self.description = self.description.strip()



    def get_data(self):
        return {
            "id": self.id,
            "destination_id": self.destination_id,
            "name": self.name,
            "location": self.location.get_data(),
            "description": self.description,
            "amenities": self.amenities.get_data(),
            "images": self.images.get_data(),
            "booking_conditions": list(self.booking_conditions)
        }
    
    def merge(self, other: 'Hotel'):
        if(self.id != other.id or self.destination_id != other.destination_id):
            return
        if len(other.name) > len(self.name):
            self.name = other.name
        if len(other.description) > len(self.description):
            self.description = other.description
        self.location.merge(other.location)
        self.amenities.merge(other.amenities)
        self.images.merge(other.images)
        self.booking_conditions.update(other.booking_conditions)

