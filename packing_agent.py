class PackingAgent:
    def run(self, data):
        print("📦 Weather Forecast Data:", data.get("weather_forecast", []))

        try:
            temps = [day["temp"] for day in data.get("weather_forecast", [])]
        except KeyError as e:
            raise Exception(f"❌ Missing expected key in weather data: {e}")

        if not temps:
            raise Exception("❌ No temperature data available for packing advice")

        avg_temp = sum(temps) / len(temps)

        if avg_temp < 10:
            packing_list = ["Warm jacket", "Gloves", "Beanie", "Thermal wear"]
        elif avg_temp < 20:
            packing_list = ["Sweater", "Jeans", "Light jacket"]
        elif avg_temp < 30:
            packing_list = ["T-shirts", "Shorts", "Cap", "Sunglasses"]
        else:
            packing_list = ["Very light clothing", "Sunscreen", "Hat", "Water bottle"]

        data["packing_advice"] = {
            "average_temp": round(avg_temp, 2),
            "recommended_items": packing_list
        }

        print("🧳 Packing Advice:", data["packing_advice"])
        return data
