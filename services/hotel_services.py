from typing import List
from models.hotel import Hotel
import json

def _merge_hotels(hotels: List[Hotel]) -> Hotel:
    merged_hotel = hotels[0]
    for hotel in hotels[1:]:
        merged_hotel.merge(hotel)
    return merged_hotel

def _get_sort_key(hotel: Hotel, hotel_ids_array: List[str], destination_ids_array: List[int]):
    has_priority_hotel_id = hotel.id in hotel_ids_array
    has_priority_dest_id = hotel.destination_id in destination_ids_array
    
    if has_priority_hotel_id:
        hotel_id_index = hotel_ids_array.index(hotel.id)
    else:
        hotel_id_index = len(hotel_ids_array)

            
    if has_priority_dest_id:
        dest_id_index = destination_ids_array.index(hotel.destination_id)
    else:
        dest_id_index = len(destination_ids_array)


    if has_priority_hotel_id:
        return (hotel_id_index, dest_id_index, hotel.destination_id)
    elif has_priority_dest_id:
        return (dest_id_index, hotel_id_index, hotel.id)
    else:
        return (hotel.id, hotel.destination_id)

def _sort_hotels(hotels: List[Hotel], hotel_ids_array: List[str], destination_ids_array: List[int]) -> List[Hotel]: 
    return sorted(
        hotels,
        key=lambda hotel: _get_sort_key(hotel, hotel_ids_array, destination_ids_array)
    )

def merge_hotels_list(hotels: List[Hotel], hotel_ids_array: List[str], destination_ids_array: List[int]) -> List[Hotel]:

    if not hotels:
        return []    
    
        
    result = []
    current_group = []
    sorted_hotels = _sort_hotels(hotels, hotel_ids_array, destination_ids_array)
    
    for hotel in sorted_hotels:
        if not current_group or (hotel.id == current_group[0].id and hotel.destination_id == current_group[0].destination_id):
            current_group.append(hotel)
        else:
            result.append(_merge_hotels(current_group))
            current_group = [hotel]
            
    result.append(_merge_hotels(current_group))
    return result


def output_hotels_to_json(hotels: List[Hotel]):
    with open("output.json", "w") as file:
        json.dump(hotels, file, default=lambda o: o.get_data(), indent=4)


