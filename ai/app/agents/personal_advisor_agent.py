from .base import BaseAgent
from app.services.gcp_ai import gemini_prompt

class PersonalAdvisorAgent(BaseAgent):
    def run(self, user_profile):
        prompt = f"Advise {user_profile['name']} with ₹{user_profile['salary']} salary on financial planning."
        advice = gemini_prompt(prompt)
        return {"personal_advice": advice}
