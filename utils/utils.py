from typing import List
import re

def sanitize_string(string: str) -> str:

    string = string.strip()

    # handle edge cases
    if string == "WiFi":
        return "wifi"

    string = re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

    return string.lower()

def args_to_list(args: str) -> List[str]:
    if args == "none":
        return []
    return args.split(",") if args else []

def str_arr_to_int_arr(str_arr: List[str]) -> List[int]:
    return [int(item) for item in str_arr]
