"""Core classes for JuankoOS."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from . import content


@dataclass
class JuankoOS:
    """Primary interface for generating creative content."""

    def lyrics(self, prompt: str) -> str:
        return content.generate_lyrics(prompt)

    def slogan(self, theme: str) -> str:
        return content.generate_slogan(theme)

    def ritual(self, topic: str) -> str:
        return content.generate_ritual(topic)
