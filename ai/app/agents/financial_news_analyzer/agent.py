from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from .subagents.news_fetcher_agent.agent import news_fetcher_agent
from .subagents.sentiment_analysis_agent.agent import sentiment_analysis_agent
from .subagents.entity_linker_agent.agent import entity_linker_agent
from .prompt import financial_news_analyzer_instruction
from dotenv import load_dotenv
import os
import google.generativeai as genai
# from google.adk.config import load_config


# Load environment variables from .env file
# Your .env file should contain:
# GCP_PROJECT="your-gcp-project-id"
# GCP_REGION="your-region"
# GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
load_dotenv()

root_agent = Agent(
    name="financial_news_analyzer",
    model="gemini-2.0-flash",
    description="Analyzes financial news for a given market entity by coordinating sub-agents.",
    instruction=financial_news_analyzer_instruction,
    tools=[
        AgentTool(agent=news_fetcher_agent),
        AgentTool(agent=sentiment_analysis_agent),
        AgentTool(agent=entity_linker_agent),
    ],
)
