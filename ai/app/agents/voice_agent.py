from .base import BaseAgent
from app.services.gcp_ai import transcribe_audio, synthesize_speech

class VoiceAgent(BaseAgent):
    def run(self, audio_blob):
        text = transcribe_audio(audio_blob)
        return {"text": text}

    def speak(self, response_text, lang="en"):
        audio = synthesize_speech(response_text, lang)
        return audio
