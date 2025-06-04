import os
from typing import List

try:
    import google.generativeai as genai
except ImportError:
    genai = None


class GeminiClient:
    def __init__(self, api_key: str | None = None):
        api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not provided")
        if genai is None:
            raise RuntimeError("google-generativeai package not installed")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")

    def chat(self, messages: List[dict]) -> str:
        # messages is list of {role, content}
        response = self.model.generate_content(messages)
        return response.text
