import re

def sanitize_string(string: str) -> str:
    
    # Remove redundant spaces
    string = string.strip()

    # Handle edge cases
    if string == "WiFi":
        return "wifi"

    # Add spaces between words that are capitalized, except for the first word
    string = re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

    # Convert to lowercase and return
    return string.lower()