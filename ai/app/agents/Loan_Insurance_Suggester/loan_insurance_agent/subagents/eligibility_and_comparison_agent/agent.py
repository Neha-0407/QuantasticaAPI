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
import os

# Assume a directory named 'test_data_dir' is present inside this agent's directory
test_data_dir = os.path.join(os.path.dirname(__file__), 'test_data_dir')

def load_json(file_path: str) -> dict:
    """Loads a JSON file from the specified path."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"error": f"Could not load or parse {os.path.basename(file_path)}"}

def compare_and_check_eligibility(user_ph: str, requested_files: list, scraped_product_data_json: str) -> str:
    """
    Compares loan/insurance options against a user's profile to determine eligibility.
    This tool now fetches the user's financial data directly using the user_ph.

    Args:
        user_ph: The user's identifier to locate their data directory.
        requested_files: A list of filenames to fetch (e.g., "fetch_credit_report.json").
        scraped_product_data_json: A JSON string containing available product data.

    Returns:
        A JSON string with a comparative list of products and their eligibility status.
    """
    # --- Load Product Data ---
    try:
        products = json.loads(scraped_product_data_json)
    except json.JSONDecodeError:
        return json.dumps({"error": "Could not parse the available product data."})

    # --- Load User Financial Data ---
    user_profile = {}
    user_dir = os.path.join(test_data_dir, user_ph)
    for filename in requested_files:
        if "credit_report" in filename: # Specifically look for the credit report
            file_path = os.path.join(user_dir, filename)
            user_profile = load_json(file_path)
            break # Stop after finding the credit report

    # --- Extract User's Credit Score ---
    user_credit_score = 0
    if "error" not in user_profile:
        try:
            user_credit_score = int(user_profile.get("creditReports", [{}])[0]
                                    .get("creditReportData", {})
                                    .get("score", {})
                                    .get("bureauScore", "0"))
        except (KeyError, IndexError, ValueError, TypeError):
            print("Warning: Could not extract a valid credit score. Defaulting to 0.")
            user_credit_score = 0
    else:
         print("Warning: Credit report file could not be loaded.")


    # --- Process Each Product for Eligibility ---
    comparison_results = []
    for product in products:
        result = product.copy()
        min_score_required = result.get("min_eligibility_score")

        if isinstance(min_score_required, int):
            if user_credit_score >= min_score_required:
                result["eligibility_status"] = "Eligible"
                if "loan" in result.get("product_name", "").lower():
                    result["calculated_metrics"] = {"estimated_emi": "₹25,345"}
            else:
                result["eligibility_status"] = "Not Eligible"
                result["reason"] = f"Your credit score of {user_credit_score} is below the minimum requirement of {min_score_required}."
        else:
            result["eligibility_status"] = "Eligible"

        comparison_results.append(result)

    return json.dumps(comparison_results, indent=2)

# Create the Tool for the ADK

# Create the Agent instance
eligibility_and_comparison_agent = Agent(
    name="eligibility_comparison_agent",
    model="gemini-2.0-flash",
    description="Compares available loan/insurance options against the user's financial profile.",
    instruction=ELIGIBILITY_COMPARISON_PROMPT,
    tools=[compare_and_check_eligibility],
    output_key="comparison_results"
)