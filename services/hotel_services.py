from typing import List
from models.hotel import Hotel
import json
def merge_hotels(hotels: List[Hotel]) -> Hotel:
    merged_hotel = hotels[0]
    for hotel in hotels[1:]:
        merged_hotel.merge(hotel)
    return merged_hotel

def get_sort_key(hotel: Hotel, hotel_ids_array: List[str], destination_ids_array: List[int]):
    if hotel.id in hotel_ids_array:
        hotel_id_index = hotel_ids_array.index(hotel.id)
    else:
        hotel_id_index = len(hotel_ids_array)
            
    if hotel.destination_id in destination_ids_array:
        dest_id_index = destination_ids_array.index(hotel.destination_id)
    else:
        dest_id_index = len(destination_ids_array) 
            
    return (hotel_id_index, dest_id_index)

def sort_hotels(hotels: List[Hotel], hotel_ids_array: List[str], destination_ids_array: List[int]) -> List[Hotel]:    
    return sorted(
        hotels,
        key=lambda hotel: get_sort_key(hotel, hotel_ids_array, destination_ids_array)
    )

def merge_hotels_list(hotels: List[Hotel]) -> List[Hotel]:
    if not hotels:
        return []
        
    result = []
    current_group = []
    
    for hotel in hotels:
        if not current_group or (hotel.id == current_group[0].id and hotel.destination_id == current_group[0].destination_id):
            current_group.append(hotel)
        else:
            result.append(merge_hotels(current_group))
            current_group = [hotel]
            
    result.append(merge_hotels(current_group))
    return result


def output_hotels_to_json(hotels: List[Hotel]):
    with open("output.json", "w") as file:
        json.dump(hotels, file, default=lambda o: o.get_data(), indent=4)


