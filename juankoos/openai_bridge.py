"""Lightweight wrapper to send JuankoOS™ prompts to OpenAI."""

import os
from typing import Dict

from .config import CONTENT_PREAMBLE, JUANKO_TONE


class JuankoOpenAI:
    """Tiny helper around the OpenAI client."""

    def __init__(self, model: str = "gpt-4o-mini") -> None:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is required to use JuankoOpenAI")

        from openai import OpenAI  # type: ignore

        self.client = OpenAI(api_key=api_key)
        self.model = model

    def craft_prompt(self, task: str, payload: Dict[str, str]) -> str:
        values = ", ".join(JUANKO_TONE["values"])
        core = (
            f"{CONTENT_PREAMBLE}\nTono: {JUANKO_TONE['voice']}. "
            f"Persona: {JUANKO_TONE['persona']}. Valores: {values}."
        )
        details = "\n".join([f"- {k}: {v}" for k, v in payload.items()])
        return f"{core}\nTarea: {task}.\nContexto:\n{details}\nResponde conciso y en dos idiomas cuando aporte claridad."

    def complete(self, prompt: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=[{"role": "user", "content": prompt}],
            temperature=0.8,
        )
        return response.output_text

    def generate(self, task: str, payload: Dict[str, str]) -> str:
        prompt = self.craft_prompt(task, payload)
        return self.complete(prompt)
