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

def scrape_loan_insurance_options(product_type: str) -> str:
    """
    Collects and aggregates data on loan or insurance products.
    NOTE: This is a mock implementation. A real-world scenario would involve
    complex web scraping logic (e.g., using Beautiful Soup, Scrapy) and would need to
    be mindful of website terms of service.

    Args:
        product_type: The type of product, either "loan" or "insurance".

    Returns:
        A JSON string of aggregated product information.
    """
    mock_data = {
        "loan": [
            {"provider": "National Bank", "product_name": "Personal Loan", "interest_rate": "11.2%", "max_term_months": 60, "min_eligibility_score": 740},
            {"provider": "City Finance", "product_name": "Car Loan", "interest_rate": "9.5%", "max_term_months": 84, "min_eligibility_score": 700},
            {"provider": "Home Lenders Inc.", "product_name": "Home Loan", "interest_rate": "8.9%", "max_term_months": 360, "min_eligibility_score": 720}
        ],
        "insurance": [
            {"provider": "SecureLife Insurance", "product_name": "Term Life Plan", "coverage": "1 Crore", "annual_premium": "15000", "key_exclusions": "Pre-existing conditions in first 2 years"},
            {"provider": "General Health Co.", "product_name": "Family Health Shield", "coverage": "10 Lakhs", "annual_premium": "22000", "key_exclusions": "Maternity in first year"}
        ]
    }
    return json.dumps(mock_data.get(product_type, []), indent=2)


aggregator_agent = Agent(
    name="option_scraper_aggregator",
    model="gemini-2.0-flash",
    description="Collects data on various loan and insurance policies from public websites.",
    instruction=OPTION_SCRAPER_PROMPT,
    tools=[scrape_loan_insurance_options],
    output_key="scraped_product_data"
)