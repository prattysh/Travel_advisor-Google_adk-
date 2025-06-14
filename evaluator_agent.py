class EvaluatorAgent:
    def run(self, data):
        weather_forecast = data.get("weather_forecast", [])
        news_articles = data.get("news_articles", [])

        issues = []

        # Check for bad weather conditions
        bad_weather_keywords = ["storm", "snow", "rain", "thunder", "hail", "extreme"]
        for day in weather_forecast:
            if any(keyword in day["weather"].lower() for keyword in bad_weather_keywords):
                issues.append(f"⚠️ Weather alert: {day['weather']} on {day['datetime']}")

        # Check for safety issues in news
        danger_keywords = ["protest", "violence", "accident", "disaster", "alert", "emergency", "evacuate"]
        for article in news_articles:
            title = article.get("title", "").lower()
            description = article.get("description", "").lower()
            if any(keyword in title or keyword in description for keyword in danger_keywords):
                issues.append(f"📰 News alert: {article['title']}")

        # Form the final recommendation
        if not issues:
            decision = "✅ It is safe to travel to the destination next weekend."
        else:
            decision = "⚠️ Caution advised. Please review the following issues before making travel plans:\n" + "\n".join(issues)

        data["evaluation_result"] = decision
        print("📋 Evaluation Summary:\n" + decision)

        return data
