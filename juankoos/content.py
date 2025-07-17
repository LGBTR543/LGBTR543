"""Content generation utilities for JuankoOS."""

import os
from typing import Optional

import openai

OPENAI_MODEL = os.environ.get("OPENAI_MODEL", "gpt-3.5-turbo")


def _call_openai(prompt: str, *, model: str = OPENAI_MODEL) -> str:
    """Call OpenAI's chat completion API with a basic prompt."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable not set")

    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
    )
    return response.choices[0].message["content"].strip()


def generate_lyrics(topic: str) -> str:
    """Generate mystical lyrics about a topic."""
    prompt = (
        f"Compose short mystical song lyrics about '{topic}'. "
        "Use poetic language."
    )
    return _call_openai(prompt)


def generate_slogan(theme: str) -> str:
    """Generate a catchy slogan."""
    prompt = f"Create an inspiring slogan with a {theme} theme."
    return _call_openai(prompt)


def generate_ritual(intention: str) -> str:
    """Generate a simple spiritual ritual."""
    prompt = (
        f"Describe a short spiritual ritual to manifest '{intention}'. "
        "Keep it uplifting and symbolic."
    )
    return _call_openai(prompt)
