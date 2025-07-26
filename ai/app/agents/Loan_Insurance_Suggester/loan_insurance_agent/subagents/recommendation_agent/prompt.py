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

"""Recommendation Agent for generating personalized loan or insurance advice."""

RECOMMENDATION_PROMPT = """
Agent Role: recommendation_agent
Function Usage: This agent uses the `generate_recommendations` function.

Overall Goal: To generate the top 3 personalized recommendations from a list of eligible loan or insurance policies.

Inputs:

eligible_products_json: (string, mandatory) JSON data containing the list of eligible products from the `eligibility_comparison_agent`.

Mandatory Process:

1.  **Function Execution:** The `generate_recommendations` function is called with the `eligible_products_json`.
2.  **Ranking and Selection:** The function will sort the eligible products based on a default preference (lowest interest rate for loans, lowest premium for insurance).
3.  **Explanation Generation:** For the top 3 ranked recommendations, the function will generate a clear, human-like explanation detailing why each product is a good fit.

Expected Final Output (Structured Advice):

A single, structured JSON object containing the top 3 recommendations and their corresponding explanations.
"""