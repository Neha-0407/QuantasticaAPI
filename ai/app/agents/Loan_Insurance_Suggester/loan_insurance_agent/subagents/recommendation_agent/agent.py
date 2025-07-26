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
from .prompt import RECOMMENDATION_PROMPT
import json


def generate_recommendations(comparison_results_json: str, user_preferences_json: str) -> str:
    """
    [cite_start]Generates personalized recommendations based on comparison results and user preferences. [cite: 237, 238]

    Args:
        comparison_results_json: JSON string of comparison results.
        user_preferences_json: JSON string of user preferences.

    Returns:
        A JSON string containing personalized recommendations.
    """
    comparison_results = json.loads(comparison_results_json)
    user_preferences = json.loads(user_preferences_json)

    eligible_products = [p for p in comparison_results if p.get("eligibility_status") == "Eligible"]
    preference = user_preferences.get("preference", "lowest interest")

    # Simple sorting based on preference
    if "lowest interest" in preference and eligible_products:
        eligible_products.sort(key=lambda x: float(x.get("interest_rate", "99").strip('%')))
    elif "flexible terms" in preference and eligible_products:
        eligible_products.sort(key=lambda x: x.get("max_term_months", 0), reverse=True)

    # Generate recommendations for the top 2 products
    recommendations = []
    for i, product in enumerate(eligible_products[:2]):
        reason = (f"This product is recommended as it aligns with your preference for '{preference}'. "
                  f"It offers a competitive interest rate of {product.get('interest_rate', 'N/A')}.")

        recommendations.append({
            "rank": i + 1,
            "provider": product.get("provider"),
            "product_name": product.get("product_name"),
            "interest_rate": product.get("interest_rate"),
            "recommendation_reason": reason
        })

    return json.dumps({"recommendations": recommendations}, indent=2)




recommendation_agent = Agent(
    name="recommendation_agent",
    model="gemini-2.0-flash",
    description="Generates personalized recommendations for loans or insurance policies.",
    instruction=RECOMMENDATION_PROMPT,
    tools=[generate_recommendations],
    output_key="final_recommendations"
)