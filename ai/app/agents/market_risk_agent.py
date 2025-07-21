from .base import BaseAgent
from app.services.gcp_ai import analyze_portfolio_risk

class MarketRiskAgent(BaseAgent):
    def run(self, portfolio):
        risk_metrics = analyze_portfolio_risk(portfolio)
        return {"risk": risk_metrics}
