"""Shared helpers for Groq API usage."""
import os


def get_api_key() -> str:
    return os.environ["GROQ_API_KEY"]
