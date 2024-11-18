from dataclasses import dataclass, field
from typing import  Set
from utils.amenities_util import sanitize_string

@dataclass
class Amenities:
    general: Set[str] = field(default_factory=set)
    room: Set[str] = field(default_factory=set)

    def __init__(self, data: dict):
        self.general = set(map(sanitize_string, data.get("general", [])))
        self.room = set(map(sanitize_string, data.get("room", [])))

    def get_data(self) -> dict:
        return {
            "general": list(self.general),
            "room": list(self.room)
        }
    
    def merge(self, other: 'Amenities') -> None:
        self.general.update(other.general)
        self.room.update(other.room)
        self.general = set(self.general) - set(self.room)
  