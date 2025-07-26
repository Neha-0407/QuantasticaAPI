from google.adk.agents import Agent
from .prompt import PORTFOLIO_ANALYSIS_PROMPT

portfolio_analysis_agent = Agent(
    name="portfolio_analysis_agent",
    model="gemini-2.0-flash",
    description="Analyzes asset allocation and investment performance.",
    instruction=PORTFOLIO_ANALYSIS_PROMPT,
    output_key="portfolio_summary"
)
