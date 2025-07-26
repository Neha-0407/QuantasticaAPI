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
from .prompt import ELIGIBILITY_COMPARISON_PROMPT
import json

def compare_and_check_eligibility(mock_product_data_json: str, user_financial_data_json: str) -> str:
    """
    Compares mock loan/insurance options against a user's profile to determine eligibility.

    Args:
        mock_product_data_json: JSON string of mock products.
        user_financial_data_json: JSON string of the user's financial data.

    Returns:
        A JSON string containing a list of eligible products.
    """
    try:
        products = json.loads(mock_product_data_json)
        user_profile = json.loads(user_financial_data_json)
    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON data provided."})

    eligible_products = []
    user_credit_score = 0
    try:
        user_credit_score = int(user_profile["creditReports"][0]["creditReportData"]["score"]["bureauScore"])
    except (KeyError, IndexError, ValueError, TypeError):
        user_credit_score = 0

    # Before using .get(), ensure product is a dict
    for product in products:
        if isinstance(product, dict):
            min_score_required = product.get("min_eligibility_score")
            if isinstance(min_score_required, int):
                if user_credit_score >= min_score_required:
                    eligible_products.append(product)
            else:  # For insurance products without a score requirement
                eligible_products.append(product)
        else:
            print(f"Unexpected product type: {type(product)}, value: {product}")
            # Handle or skip invalid product


    return json.dumps(eligible_products, indent=2)

eligibility_comparison_agent = Agent(
    name="eligibility_comparison_agent",
    model="gemini-2.0-flash",
    description="Compares available loan/insurance options against the user's financial profile.",
    instruction=ELIGIBILITY_COMPARISON_PROMPT,
    tools=[compare_and_check_eligibility]
)