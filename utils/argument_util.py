from typing import List


def hotel_ids_args_to_list(args: str) -> List[str]:
    if args == "none":
        return []
    return args.split(",") if args else []

def destination_ids_args_to_list(args: str) -> List[int]:
    if args == "none":
        return []
    return _str_arr_to_int_arr(args.split(",")) if args else []

def _str_arr_to_int_arr(str_arr: List[str]) -> List[int]:
    return [int(item) for item in str_arr]
