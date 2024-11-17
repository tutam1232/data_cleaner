from .base import BaseSanitizer
from typing import List

class AcmeSanitizer(BaseSanitizer):
    def __init__(self):
        super().__init__()
        self.id_key = "Id"
        self.destination_id_key = "DestinationId"

    def sanitize(self, hotels: List[dict]):
        cleaned_data = []
