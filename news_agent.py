import os
import requests
from dotenv import load_dotenv

load_dotenv()

class NewsAgent:
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")
        self.safety_keywords = [
            "protest", "riot", "violence", "crime", "shooting", "storm",
            "earthquake", "flood", "outbreak", "disease", "heatwave", "emergency", "evacuation"
        ]

    def run(self, data):
        city = data.get("city", "Los Angeles")
        url = f"https://newsapi.org/v2/everything?q={city}&pageSize=10&sortBy=publishedAt&apiKey={self.api_key}"

        try:
            response = requests.get(url)
            articles = response.json().get("articles", [])
        except Exception as e:
            print("News API Error:", e)
            return { "safe_to_travel": None, "reason": "News fetch failed." }

        safety_flags = []
        relevant_articles = []

        for article in articles:
            title = article["title"].lower()
            description = (article.get("description") or "").lower()
            content = title + " " + description

            for keyword in self.safety_keywords:
                if keyword in content:
                    safety_flags.append(keyword)
                    relevant_articles.append(article["title"])
                    break  # Avoid duplicate alerts for one article

        data["news_articles"] = [a["title"] for a in articles]
        data["relevant_risks"] = relevant_articles
        data["safe_to_travel"] = len(safety_flags) == 0

        return data
