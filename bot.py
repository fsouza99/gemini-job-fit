from google.genai import Client
from google.genai.types import GenerateContentConfig


class Bot:
    """Communicates with Gemini via its API.

    It expects the "GOOGLE_API_KEY" environment variable to be available.
    """
    def __init__(self, model: str):
        self._client = Client()
        self._config = GenerateContentConfig(
            system_instruction='Emule um ATS.',
            temperature=0.3)
        self.model = model
        return

    def send_prompt(self, prompt: str) -> str | None:
        try:
            response = self._client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=self._config)
        except Exception as exc:
            print(exc)
            return None
        return response.text

