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

def generate_recommendations(eligible_products_json: str) -> str:
    """
    Generates the top 3 recommendations from a list of eligible products.

    Args:
        eligible_products_json: JSON string of eligible products.

    Returns:
        A JSON string containing the top 3 personalized recommendations.
    """
    try:
        eligible_products = json.loads(eligible_products_json)
    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON data for eligible products."})

    if not eligible_products:
        return json.dumps({"recommendations": [{"message": "No eligible products found based on your profile."}]})

    # Determine if products are loans or insurance to sort correctly
    if "interest_rate" in eligible_products[0]:
        # Sort by lowest interest rate for loans
        eligible_products.sort(key=lambda x: float(x.get("interest_rate", "99").strip('%')))
        sort_key = "interest_rate"
    elif "annual_premium" in eligible_products[0]:
        # Sort by lowest premium for insurance
        eligible_products.sort(key=lambda x: int(x.get("annual_premium", "999999").replace('₹', '').replace(',', '')))
        sort_key = "annual_premium"
    else:
        sort_key = "N/A"


    recommendations = []
    for i, product in enumerate(eligible_products[:3]): # Get top 3
        reason = f"This product is a top recommendation based on its competitive {sort_key.replace('_', ' ')} of {product.get(sort_key, 'N/A')}."
        recommendations.append({
            "rank": i + 1,
            "provider": product.get("provider"),
            "product_name": product.get("plan_name") or product.get("product_name"),
            sort_key: product.get(sort_key),
            "recommendation_reason": reason
        })

    return json.dumps({"recommendations": recommendations}, indent=2)

recommendation_agent = Agent(
    name="recommendation_agent",
    model="gemini-2.0-flash",
    description="Generates personalized recommendations for loans or insurance policies.",
    instruction=RECOMMENDATION_PROMPT,
    tools=[generate_recommendations]
)