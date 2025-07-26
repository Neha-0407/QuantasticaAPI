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

test_data_dir = os.path.join(os.path.dirname(__file__),'..','..','test_data_dir')

def load_json(file_path: str) -> dict:
    """Loads a JSON file from the specified path."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"error": f"Could not load or parse {os.path.basename(file_path)}"}

def fetch_user_financial_data(user_ph: str, requested_files: list) -> str:
    """
    [cite_start]Securely accesses and pre-processes user's provided financial data files. [cite: 208, 209]

    Args:
        user_ph: The user's identifier to locate their data directory.
        requested_files: A list of filenames to fetch.

    Returns:
        A JSON string containing the content of the requested files.
    """
    user_data = {}
    user_dir = os.path.join(test_data_dir, user_ph)
    for filename in requested_files:
        file_path = os.path.join(user_dir, filename)
        user_data[filename] = load_json(file_path)

    return json.dumps(user_data, indent=2)


financial_data_fetcher_agent = Agent(
    name="financial_data_fetcher",
    model="gemini-2.0-flash",
    description="Securely accesses the user's provided financial data.",
    instruction=FINANCIAL_DATA_FETCHER_PROMPT,
    tools=[fetch_user_financial_data],
    output_key="user_financial_data"
)