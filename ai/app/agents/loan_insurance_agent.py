from .base import BaseAgent

class LoanInsuranceAgent(BaseAgent):
    def run(self, credit_score, income, assets):
        # Logic for eligibility
        return {
            "loan_eligibility": credit_score > 700,
            "insurance_suggestions": ["Health + Term Plan combo"]
        }
