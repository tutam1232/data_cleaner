import argparse
import asyncio
from suppliers.acme import AcmeSupplier 
from suppliers.patagonie import PatagonieSupplier
from suppliers.paperflies import PaperfliesSupplier

from services.hotel_services import  merge_hotels_list, output_hotels_to_json
from utils.argument_util import hotel_ids_args_to_list, destination_ids_args_to_list
    
async def main():

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("hotel_ids")
    parser.add_argument("destination_ids")
    args = parser.parse_args()
    hotel_ids = hotel_ids_args_to_list(args.hotel_ids)
    destination_ids = destination_ids_args_to_list(args.destination_ids)


    # Fetch hotels and sanitize data
    all_hotels = []
    suppliers = [AcmeSupplier(), PaperfliesSupplier(), PatagonieSupplier()]
    for supplier in suppliers:
        fetched_hotels = await supplier.fetch(hotel_ids, destination_ids)
        parsed_hotels = supplier.parse(fetched_hotels)
        all_hotels.extend(parsed_hotels)

    # Merge hotels
    merged_hotels = merge_hotels_list(all_hotels, hotel_ids, destination_ids)

    # Output to json
    output_hotels_to_json(merged_hotels)



if __name__ == "__main__":
    asyncio.run(main())