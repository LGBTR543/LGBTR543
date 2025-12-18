"""Deterministic content generators to keep JuankoOS™ creative."""

from datetime import datetime
from typing import Dict, List

from .config import BRAND_SYMBOLS, CONTENT_PREAMBLE, JUANKO_TONE


def generate_lyrics(theme: str, mood: str, language: str = "es") -> str:
    """Create short, bilingual-friendly lyrics with a mystical tone."""
    moon_phase = BRAND_SYMBOLS["emoji"]
    stamp = datetime.utcnow().strftime("%Y-%m-%d")
    bridge = " / " if language == "es" else " – "
    opening = f"{CONTENT_PREAMBLE} {moon_phase}"
    verse = f"{theme.title()} en {mood.lower()}" if language == "es" else f"{theme.title()} in {mood.lower()}"
    outro = (
        "Somos brasa y luz, danzando con las sombras." if language == "es" else "We are ember and light, dancing with the shadows."
    )
    return f"{opening}\n[{stamp}] {verse}{bridge}{outro}"


def generate_slogan(seed: str) -> str:
    """Propose a brand-ready slogan for campaigns and product drops."""
    return (
        f"{BRAND_SYMBOLS['sigil']} {seed.strip().title()} → oro vivo, comunidad despierta."
    )


def design_ritual(intention: str, duration_minutes: int = 11) -> Dict[str, str]:
    """Blueprint for a symbolic ritual session."""
    return {
        "intention": intention,
        "duration": f"{duration_minutes} minutos de presencia dorada",
        "steps": (
            "1) Respira en 4-4-4-4. 2) Escribe tu visión en dos idiomas. "
            "3) Afirma en voz alta. 4) Cierra con agua y luz violeta."
        ),
        "closing": BRAND_SYMBOLS["mantra"],
    }


def craft_membership_tier(name: str, benefits: List[str], price: str) -> Dict[str, str]:
    """Describe a membership tier for monetization."""
    formatted_benefits = "; ".join(benefits)
    return {
        "name": name.title(),
        "price": price,
        "benefits": formatted_benefits,
        "energy": "Círculo íntimo para artistas conscientes",
    }


def create_shop_item(title: str, format_hint: str, value: str) -> Dict[str, str]:
    """Describe a digital product slot for the store."""
    return {
        "title": title.title(),
        "format": format_hint,
        "value": value,
        "call_to_action": f"Descarga y desbloquea {BRAND_SYMBOLS['sigil']} en tu proceso creativo.",
    }
