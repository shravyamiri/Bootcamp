import re

def to_snakecase(text: str) -> str:
    text = re.sub(r'[\s\-]+', '_', text)
    return text.lower()
