# Vertex AI Financial Advisor Agent

This project is a modular, multi-agent system designed to provide comprehensive financial advice. It is built using the *Google Agent Development Kit (ADK)* and leverages various *Google Cloud Platform (GCP)* services to create a scalable and intelligent financial advisory tool. The architecture is based on the "Vertex AI Agent Team Map for Financial Advisory" document.

## 📋 Features

The project is divided into specialized agent teams, each with a distinct role:

  * *Financial News Analyzer:* Analyzes news articles to gauge market sentiment for specific stocks or entities.
  * *Chart Analyzer:* Performs technical analysis on market data to identify trends, patterns, and simulate scenarios.
  * *Loan/Insurance Advisor:* Scrapes and compares loan and insurance options, checks user eligibility, and provides personalized recommendations.
  * *Investment Advisor:* Analyzes investment portfolios, suggests debt optimization strategies, and projects long-term financial goals.
  * *Tax Advisor:* Provides tax-saving strategies based on a comprehensive knowledge base of tax laws and the user's financial data.
  * *Wealth Management:* Offers a conversational interface for users to ask natural language questions about their finances, such as net worth and affordability.

## 🏛️ Architecture

The system is designed with a modular, multi-agent architecture where a central *Orchestrator Agent* delegates tasks to specialized sub-agents. It is built on serverless components like *Cloud Run* and *Cloud Functions* for cost-effectiveness and scalability. *Vertex AI Generative AI Studio* is used for integrating Large Language Models (LLMs) like Gemini for natural language understanding and generation.

## 🚀 Getting Started

### Prerequisites

  * Python 3.10+
  * Google Cloud SDK
  * Google Agent Development Kit (ADK)
  * Access to a Google Cloud Platform project with the Vertex AI API enabled.

### Installation

1.  *Clone the repository:*

    bash
    git clone <your-repository-url>
    cd <your-repository-directory>
    

2.  *Install dependencies:*

    bash
    pip install -r requirements.txt
    

### Project Structure

The project is organized into directories for each agent team. Inside each team's directory, there is an orchestrator agent (root_agent) and several sub-agents, each with its own prompt.py and agent.py.


<pre lang="markdown"> <code> ``` ├── team_3_loan_insurance_advisor │ ├── orchestrator_agent │ │ ├── prompt.py │ │ └── agent.py │ ├── financial_data_fetcher_agent │ │ ├── prompt.py │ │ └── agent.py │ └── ... (other sub-agents) ├── team_6_wealth_management │ └── ... (modules or agents for wealth management) └── test_data_dir └── 3333333333 ├── fetch_bank_transactions.json ├── fetch_credit_report.json └── ... (other test files) ``` </code> </pre>

## ⚙️ Usage

### 1\. Set Up User Data

Place the user's financial data files (e.g., fetch_credit_report.json, fetch_bank_transactions.json) inside the test_data_dir in a subdirectory named after the user's phone number (e.g., 3333333333).

### 2\. Run the Agent

You can interact with the agent using the ADK's built-in web interface or API server.

*Using the Web UI:*

bash
adk web team_3_loan_insurance_advisor/orchestrator_agent


*Using the API Server:*

bash
adk api_server team_3_loan_insurance_advisor/orchestrator_agent --allow_origins="*"


### 3\. Example Query

To get loan recommendations, you would send a request to the orchestrator agent with the following parameters:

  * *user\_ph:* "3333333333"
  * *product\_type:* "loan"

The agent will then execute its workflow: print the user's credit score to the console and return a JSON object with the top 3 recommended loan options.
