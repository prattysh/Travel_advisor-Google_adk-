import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WeatherAgent:
    def run(self, data):
        lat = data["lat"]
        lon = data["lon"]
        api_key = os.getenv("OPENWEATHER_API_KEY")
        print("Loaded API Key:", api_key)

        # Use current weather data endpoint
        url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={api_key}"
        response = requests.get(url)

        print("Weather API URL:", url)
        print("Status Code:", response.status_code)

        if response.status_code != 200:
            print("📩 Response Text:", response.text)
            raise Exception("Failed to fetch weather data")

        data_json = response.json()
        forecast = data_json.get("list", [])[:2] 
        for entry in forecast:
            day_summary = {
                "datetime": entry["dt_txt"],
                "temp": entry["main"]["temp"],
                "weather": entry["weather"][0]["description"]
            }
            summary.append(day_summary)

        data["weather_forecast"] = summary
        return data
