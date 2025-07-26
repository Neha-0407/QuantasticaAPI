from google.adk.agents import Agent
from .prompt import ANOMALY_PROMPT

anomaly_detector_agent = Agent(
    name="anomaly_detector_agent",
    model="gemini-2.0-flash",
    description="Flags anomalous or risky financial transactions.",
    instruction=ANOMALY_PROMPT,
    output_key="anomalies_detected"
)
