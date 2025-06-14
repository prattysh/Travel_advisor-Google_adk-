class PlannerAgent:
    def __init__(self):
        self.agents = []

    def plan(self, goal):
        # Define the chain of agents to achieve the goal
        print(f"🎯 User Goal: {goal}")
        
        if "travel" in goal.lower() and "pack" in goal.lower():
            self.agents = [
                "LocationAgent",
                "WeatherAgent",
                "NewsAgent",
                "EvaluatorAgent",
                "PackingAgent"
            ]
        else:
            raise ValueError("Unsupported goal")

        return self.agents

    def execute_plan(self, agents, goal_data):
        data = goal_data
        for agent in agents:
            print(f"🚀 Executing {agent}...")
            module = __import__(agent.lower())
            agent_class = getattr(module, agent)
            agent_instance = agent_class()
            data = agent_instance.run(data)
        return data
