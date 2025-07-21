from app.agents import (
    SentimentAgent, MarketRiskAgent, TaxAdvisorAgent,
    LoanInsuranceAgent, CreditAnalyzerAgent,
    FamilyFinanceAgent, PersonalAdvisorAgent
)

class Orchestrator:
    def __init__(self, user_context):
        self.context = user_context
        self.agents = [
            SentimentAgent(user_context),
            MarketRiskAgent(user_context),
            TaxAdvisorAgent(user_context),
            LoanInsuranceAgent(user_context),
            CreditAnalyzerAgent(user_context),
            FamilyFinanceAgent(user_context),
            PersonalAdvisorAgent(user_context)
        ]

    def run_all(self, input_data):
        results = {}
        for agent in self.agents:
            results[agent.__class__.__name__] = agent.run(**input_data)
        return results
