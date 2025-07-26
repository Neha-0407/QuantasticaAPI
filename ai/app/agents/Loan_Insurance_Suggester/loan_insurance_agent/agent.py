# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.agents import Agent
from .prompt import LOAN_INSURANCE_ORCHESTRATOR_PROMPT
from .subagents.option_scrapper_aggregator_agent.agent import option_scraper_aggregator_agent
from .subagents.financial_data_fetcher_agent.agent import financial_data_fetcher_agent
from .subagents.eligibility_comparison_agent.agent import eligibility_comparison_agent
from .subagents.recommendation_agent.agent import recommendation_agent

# The root_agent for this team is the orchestrator.
root_agent = Agent(
    name="loan_insurance_orchestrator",
    model="gemini-2.0-flash",
    description="Analyzes loan and insurance options to suggest the best one as per a user's finances.",
    instruction=LOAN_INSURANCE_ORCHESTRATOR_PROMPT,
    sub_agents=[
        option_scraper_aggregator_agent,
        financial_data_fetcher_agent,
        eligibility_comparison_agent,
        recommendation_agent
    ],
    output_key="final_loan_insurance_advice"
)