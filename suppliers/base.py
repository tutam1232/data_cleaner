from abc import ABC
from typing import List
import aiohttp
from models.hotel import Hotel

class BaseSupplier(ABC):

    def __init__(self):
        self.url = ""
        self.id_key = ""
        self.destination_id_key = ""

    def _get_sort_key(self, hotel: dict, hotel_ids_array: List[str], destination_ids_array: List[int]):
        id = hotel.get(self.id_key,None)
        if id in hotel_ids_array:
            hotel_id_index = hotel_ids_array.index(id)
        else:
            hotel_id_index = len(hotel_ids_array)
            

        destination_id = hotel.get(self.destination_id_key,None)
        if destination_id in destination_ids_array:
            dest_id_index = destination_ids_array.index(destination_id)
        else:
            dest_id_index = len(destination_ids_array) 
            
        return (hotel_id_index, dest_id_index)

    async def fetch(self, hotel_ids_array: List[str], destination_ids_array: List[int]):
        results = None
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                results = await response.json()

        result_alter_filter = sorted(
            [hotel for hotel in results if (len(hotel_ids_array) == 0 or hotel.get(self.id_key,None) in hotel_ids_array) and 
             (len(destination_ids_array) == 0 or hotel.get(self.destination_id_key,None) in destination_ids_array)],
            key=lambda hotel: self._get_sort_key(hotel, hotel_ids_array, destination_ids_array)
        )

        return result_alter_filter
    
    def parse(self, hotels: List[dict]) -> List['Hotel']:
        pass
