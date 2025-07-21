from .agent import BaseAgent

class CreditAnalyzerAgent(BaseAgent):
    def run(self, credit_report):
        score = self._calculate_score(credit_report)
        return {"score": score, "tips": ["Pay EMIs on time", "Reduce credit usage"]}

    def _calculate_score(self, data):
        # Scoring logic
        return 740
