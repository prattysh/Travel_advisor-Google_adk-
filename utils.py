import datetime
from geopy.geocoders import Nominatim

def get_next_weekend_dates():
    today = datetime.date.today()
    days_until_saturday = (5 - today.weekday()) % 7
    saturday = today + datetime.timedelta(days=days_until_saturday)
    sunday = saturday + datetime.timedelta(days=1)
    return saturday.strftime('%Y-%m-%d'), sunday.strftime('%Y-%m-%d')

def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="travel-planner")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    else:
        raise ValueError(f"Could not locate city: {city_name}")
