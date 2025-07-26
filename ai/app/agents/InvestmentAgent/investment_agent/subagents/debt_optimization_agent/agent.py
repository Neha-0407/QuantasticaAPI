from google.adk.agents import Agent
from .prompt import DEBT_OPTIMIZATION_PROMPT

debt_optimizer_agent = Agent(
    name="debt_optimizer_agent",
    model="gemini-2.0-flash",
    description="Optimizes debt repayment strategy based on user obligations.",
    instruction=DEBT_OPTIMIZATION_PROMPT,
    output_key="debt_strategy"
)
