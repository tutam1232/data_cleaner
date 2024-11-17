from dataclasses import dataclass

@dataclass
class Location:
    lat: float 
    lng: float 
    address: str 
    city: str 
    country: str 

    def __init__(self, data: dict):
        self.lng = data.get("lng",None)
        self.lat = data.get("lat",None)
        self.address = data.get("address","")
        self.city = data.get("city","")
        self.country = data.get("country","")
    def get_data(self):
        return {
            "lng": self.lng,
            "lat": self.lat,
            "address": self.address,
            "city": self.city,
            "country": self.country
        }
    
    def merge(self, other: 'Location'):
        if other.lat is not None:
            self.lat = other.lat
        if other.lng is not None:
            self.lng = other.lng
        if len(other.address) > len(self.address):
            self.address = other.address
        if len(other.city) > len(self.city):
            self.city = other.city
        if len(other.country) > len(self.country):
            self.country = other.country
 