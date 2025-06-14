from planner_agent import PlannerAgent
from location_agent import LocationAgent
from weather_agent import WeatherAgent
from news_agent import NewsAgent
from packing_agent import PackingAgent
from evaluator_agent import EvaluatorAgent

def main():
    print("🎯 Starting Multi-Agent AI System...")
    user_goal = "Can I safely travel to Los Angeles next weekend, and what should I pack?"

    # Initialize agents
    planner = PlannerAgent()
    location_agent = LocationAgent()
    weather_agent = WeatherAgent()
    news_agent = NewsAgent()
    packing_agent = PackingAgent()
    evaluator = EvaluatorAgent()

    # Initial empty context
    context = {
        "goal": user_goal,
        "city": "Los Angeles"
    }

    # Plan the route
    agent_sequence = planner.plan(user_goal)
    print("📌 Agent sequence planned:", agent_sequence)

    for agent_name in agent_sequence:
        print(f"➡️ Running {agent_name}...")
        if agent_name == "LocationAgent":
            context = location_agent.run(context)
        elif agent_name == "WeatherAgent":
            context = weather_agent.run(context)
        elif agent_name == "NewsAgent":
            context = news_agent.run(context)
        elif agent_name == "PackingAgent":
            context = packing_agent.run(context)

    print("✅ Agent execution complete.")
    
    # Evaluate final result
    final_output = evaluator.run(context)

    print("\n🎯 Final Summary:")
    print(final_output)

if __name__ == "__main__":
    main()
