"""Configuration module for JuankoOS."""

import os

class Theme:
    """Visual theme colors in hexadecimal."""
    BACKGROUND = "#0c0b16"  # dark purple/black
    FOREGROUND = "#ffd700"  # gold
    ACCENT = "#7a1fa2"      # purple

def openai_api_key() -> str:
    """Get OpenAI API key from environment variable."""
    return os.getenv("OPENAI_API_KEY", "")
