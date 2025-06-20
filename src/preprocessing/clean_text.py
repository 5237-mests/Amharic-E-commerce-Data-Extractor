# src/preprocessing/clean_text.py

import re

def normalize_amharic(text: str) -> str:
    """Normalize common Amharic punctuation & whitespace"""
    text = re.sub(r"[።፡]", " ", text)  # Replace Ethiopian punctuation with space
    text = re.sub(r"\s+", " ", text)    # Collapse multiple spaces
    return text.strip()

def remove_emojis(text: str) -> str:
    return re.sub(r'[^\w\s,፡።ብር]', '', text)

def clean_text(text: str) -> str:
    if not text:
        return ""
    text = normalize_amharic(text)
    text = remove_emojis(text)
    return text
