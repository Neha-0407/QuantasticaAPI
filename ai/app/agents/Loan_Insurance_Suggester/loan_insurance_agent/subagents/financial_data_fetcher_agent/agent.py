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
from .prompt import FINANCIAL_DATA_FETCHER_PROMPT
import json
import os

test_data_dir = os.path.join(os.path.dirname(__file__),'..','..', 'test_data_dir')

def load_json(file_path: str) -> dict:
    """Loads a JSON file from the specified path."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"error": f"Could not load or parse {os.path.basename(file_path)}"}

def fetch_user_financial_data(user_ph: str) -> str:
    """
    Securely accesses user's credit report, prints the credit score, and returns the data.

    Args:
        user_ph: The user's identifier to locate their data directory.

    Returns:
        A JSON string containing the content of the user's credit report.
    """
    credit_report_path = os.path.join(test_data_dir, user_ph, 'fetch_credit_report.json')
    user_credit_data = load_json(credit_report_path)

    # Extract and print the credit score
    try:
        credit_score = user_credit_data["creditReports"][0]["creditReportData"]["score"]["bureauScore"]
        print(f"User's Credit Score: {credit_score}")
    except (KeyError, IndexError, TypeError):
        print("User's Credit Score: Not Found")

    return json.dumps(user_credit_data, indent=2)

financial_data_fetcher_agent = Agent(
    name="financial_data_fetcher",
    model="gemini-2.0-flash",
    description="Securely accesses the user's provided financial data and prints the credit score.",
    instruction=FINANCIAL_DATA_FETCHER_PROMPT,
    tools=[fetch_user_financial_data]
)