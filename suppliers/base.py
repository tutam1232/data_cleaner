from abc import ABC, abstractmethod
from typing import List, Tuple
import aiohttp
from models.hotel import Hotel

class BaseSupplier(ABC):

    __instances = {}

    def __new__(cls):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__new__(cls)
            cls.__instances[cls].url = ""
            cls.__instances[cls].id_key = ""
            cls.__instances[cls].destination_id_key = ""
        return cls.__instances[cls]


    def _get_sort_key(self, hotel: dict, hotel_ids_array: List[str], destination_ids_array: List[int]) -> Tuple[int, int, int]:
        id = hotel.get(self.id_key,None)
        has_priority_hotel_id = id in hotel_ids_array
        if has_priority_hotel_id:
            hotel_id_index = hotel_ids_array.index(id)
        else:
            hotel_id_index = len(hotel_ids_array)
            

        destination_id = hotel.get(self.destination_id_key,None)
        has_priority_dest_id = destination_id in destination_ids_array
        if has_priority_dest_id:
            dest_id_index = destination_ids_array.index(destination_id)
        else:
            dest_id_index = len(destination_ids_array) 
            
        if has_priority_hotel_id:
            return (hotel_id_index, dest_id_index, destination_id)
        elif has_priority_dest_id:
            return (dest_id_index, hotel_id_index, id)
        else:
            return (id, destination_id, 0)

    async def fetch(self, hotel_ids_array: List[str], destination_ids_array: List[int]) -> List[dict]:
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
    
    @abstractmethod
    def parse(self, hotels: List[dict]) -> List['Hotel']:
        pass
