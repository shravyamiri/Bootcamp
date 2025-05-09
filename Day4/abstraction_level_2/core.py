# abstraction_level_2/core.py
from .types import ProcessorFn

def to_uppercase(line: str) -> str:
    """Converts a line to uppercase."""
    return line.upper()

def to_snakecase(line: str) -> str:
    """Replaces spaces with underscores and converts to lowercase."""
    return line.lower().replace(" ", "_")

# You can add more processors here as needed