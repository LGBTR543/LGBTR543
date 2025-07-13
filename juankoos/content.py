"""Content generation helpers for JuankoOS."""

from __future__ import annotations

import openai
from typing import Dict

from .config import openai_api_key

_api_key = openai_api_key()
if _api_key:
    openai.api_key = _api_key


def generate_lyrics(prompt: str) -> str:
    """Generate mystical lyrics based on a prompt."""
    if _api_key:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate mystical song lyrics about {prompt} in Spanish:",
            max_tokens=150,
        )
        return response.choices[0].text.strip()
    return f"[Demo lyrics about {prompt}]"


def generate_slogan(theme: str) -> str:
    """Generate a short slogan related to the given theme."""
    if _api_key:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Create a short inspirational slogan about {theme} in Spanish:",
            max_tokens=20,
        )
        return response.choices[0].text.strip()
    return f"Slogan: {theme} infinito"


def generate_ritual(topic: str) -> str:
    """Generate a symbolic ritual for the given topic."""
    if _api_key:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Describe a brief spiritual ritual themed around {topic} in Spanish:",
            max_tokens=120,
        )
        return response.choices[0].text.strip()
    return f"Un ritual sencillo para {topic}."
