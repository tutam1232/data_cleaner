from abc import ABC
from typing import List


class BaseSanitizer(ABC):
    def __init__(self):
        self.id_key = ""
        self.destination_id_key = ""

    def sanitize(self, hotels: List[dict]):
        pass
