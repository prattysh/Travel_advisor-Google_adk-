from utils import get_next_weekend_dates, get_coordinates

class LocationAgent:
    def run(self, data):
        city = "Tokyo"
        lat, lon = get_coordinates(city)
        start_date, end_date = get_next_weekend_dates()
        
        return {
            "city": city,
            "lat": lat,
            "lon": lon,
            "start_date": start_date,
            "end_date": end_date
        }
