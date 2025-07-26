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
from .prompt import OPTION_SCRAPER_PROMPT
import json
import random

def get_mock_options(product_type: str) -> str:
    """
    Generates 100 mock data points for loan or insurance products.

    Args:
        product_type: The type of product, either "loan" or "insurance".

    Returns:
        A JSON string of 100 mock product options.
    """
    mock_data = []
    if "loan" in product_type.lower():
        providers = ["National Bank", "City Finance", "Home Lenders Inc.", "Secure Credit", "People's Bank"]
        for i in range(100):
            mock_data.append({
                "provider": f"{random.choice(providers)} #{i+1}",
                "product_name": f"{random.choice(['Personal', 'Home', 'Car'])} Loan",
                "interest_rate": f"{random.uniform(8.5, 18.0):.2f}%",
                "max_term_months": random.choice([60, 84, 120, 240, 360]),
                "min_eligibility_score": random.randint(680, 780)
            })
    elif "insurance" in product_type.lower():
        providers = ["SecureLife Insurance", "General Health Co.", "SafeGuard Plus", "Family First Assurance"]
        for i in range(100):
            mock_data.append({
                "provider": f"{random.choice(providers)} #{i+1}",
                "plan_name": f"{random.choice(['Gold', 'Silver', 'Bronze'])} Health Shield",
                "sum_insured": f"{random.choice([5, 10, 15, 20, 50])} Lakhs",
                "annual_premium": f"₹{random.randint(12000, 35000):,}"
            })

    return json.dumps(mock_data, indent=2)

# This agent is a sub-agent and will be called by the orchestrator.
# Its function is passed directly to the orchestrator's tools list.
option_scraper_aggregator_agent = Agent(
    name="option_scraper_aggregator",
    model="gemini-2.0-flash",
    description="Generates mock data for various loan and insurance policies.",
    instruction=OPTION_SCRAPER_PROMPT,
    tools=[get_mock_options]
)