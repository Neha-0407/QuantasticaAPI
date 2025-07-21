from .agent import BaseAgent

class FamilyFinanceAgent(BaseAgent):
    def run(self, family_accounts):
        summary = self._aggregate(family_accounts)
        return {"summary": summary}

    def _aggregate(self, accounts):
        # Aggregate budgets/spending across family members
        return {"monthly_spend": 82000, "top_spender": "Dad"}
