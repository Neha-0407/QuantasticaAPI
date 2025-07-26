from google.adk.agents import Agent
from .prompt import GOAL_PROMPT

goal_projection_agent = Agent(
    name="goal_projection_agent",
    model="gemini-2.0-flash",
    description="Projects feasibility of long-term financial goals.",
    instruction=GOAL_PROMPT,
    output_key="goal_projection"
)
