from google.adk.agents import Agent
from .prompt import INVESTMENT_ORCHESTRATOR_PROMPT
from .subagents.portfolio_analysis_agent.agent import portfolio_analysis_agent
from .subagents.debt_optimization_agent.agent import debt_optimizer_agent
from .subagents.long_term_goal_projection_agent.agent import goal_projection_agent
from .subagents.anomaly_detection_agent.agent import anomaly_detector_agent

# Import the new data fetching function
from .data_fetcher import fetch_all_financial_data

root_agent = Agent(
    name="investment_orchestrator",
    model="gemini-2.0-flash",
    description="Provides investment analysis, optimization, and financial forecasting.",
    instruction=INVESTMENT_ORCHESTRATOR_PROMPT,
    sub_agents=[
        portfolio_analysis_agent,
        debt_optimizer_agent,
        goal_projection_agent,
        anomaly_detector_agent
    ],
    # Register the function as a tool for this agent
    tools=[fetch_all_financial_data],
    output_key="final_investment_advice"
)
