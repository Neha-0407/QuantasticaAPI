from .base import BaseAgent
from app.services.scraping_service import fetch_news_sentiment

class SentimentAgent(BaseAgent):
    def run(self, topic):
        sentiment_report = fetch_news_sentiment(topic)
        return {"sentiment": sentiment_report}
