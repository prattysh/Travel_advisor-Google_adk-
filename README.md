#  Multi-Agent AI Travel Advisor System

##  Overview

This project is a **Multi-Agent AI System** built using Python that collaborates to answer the user goal:

> “Can I safely travel to **Los Angeles** next weekend, and what should I pack?”

It uses a **planner agent** to define the agent sequence, and multiple **enrichment agents** to gather weather, news, and contextual data before generating a decision and packing recommendation.

---

##  Agents Used

1. **PlannerAgent**:  
   Decides the optimal sequence of agents based on the user's goal. This ensures that agents work in dependency order (e.g., weather agent needs location first).

2. **LocationAgent**:  
   Resolves the city name to geographic coordinates (latitude and longitude) using the `geopy` geocoder.

3. **WeatherAgent**:  
   Fetches upcoming weather forecasts using the **OpenWeatherMap API** and enriches the context with temperature and condition data.

4. **NewsAgent**:  
   Retrieves recent news articles from **NewsAPI** for safety/risk evaluation.

5. **EvaluatorAgent**:  
   Analyzes weather and news data to decide whether it is **safe to travel** or not.

6. **PackingAgent**:  
   Suggests items to pack based on weather (e.g., jackets for cold weather).

---

##  APIs Used

- [OpenWeatherMap API](https://openweathermap.org/)
- [NewsAPI](https://newsapi.org/)
- [Geopy (Nominatim)](https://geopy.readthedocs.io/en/stable/)

---

##  Project Structure

```
Travel_advisor/
│
├── main.py                 # Main runner that calls the planner and executes agents
├── .env                    # Contains API keys (not pushed to GitHub)
├── planner_agent.py        # Plans agent sequence
├── utils.py                # Utility functions like date helpers
│
├── location_agent.py
├── weather_agent.py
├── news_agent.py
├── evaluator_agent.py
└── packing_agent.py
```

---

##  Setup Instructions

### 1. Clone the Repository or Download ZIP

```bash
git clone https://github.com/your-username/travel-advisor-agents.git
cd travel-advisor-agents
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure your environment includes:
- `requests`
- `python-dotenv`
- `geopy`

### 3. Create `.env` File

Create a `.env` file in the root directory and add your API keys:

```
OPENWEATHER_API_KEY=your_openweathermap_key
NEWS_API_KEY=your_newsapi_key
```

---

##  Running the Project

```bash
python main.py
```

You’ll see the agent sequence being executed step by step with printed context outputs and final evaluation.

---

##  Evaluation Examples

### Goal 1: Travel to Los Angeles Next Weekend

```
Input:
"Can I safely travel to Los Angeles next weekend, and what should I pack?"

Output:
{
  "safe_to_travel": true,
  "evaluation_result": " It is safe to travel to the destination next weekend.",
  "packing_advice": {
    "average_temp": 17.59,
    "recommended_items": ["Sweater", "Jeans", "Light jacket"]
  }
}
```

---

##  Evaluation Criteria

| Criterion                        | Achieved |
|----------------------------------|----------|
| Agent chaining & dependency flow | Yes      |
| Enrichment of data at each step  | Yes      |
| Planner determines routing       | Yes      |
| Iterative context refinement     | Yes      |
| Modular, testable codebase       | Yes      |

---

##  Future Improvements

- Add flight search & delay prediction agent.
- Support for multiple city comparisons.
- GUI using Streamlit or Gradio.

---

##  License

This project is licensed under the MIT License.
