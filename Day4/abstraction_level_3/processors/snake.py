# abstraction_level_3/processors/snake.py
from ..types import ProcessorFn

def to_snakecase(line: str) -> str:
    """Replaces spaces with underscores and converts to lowercase."""
    return line.lower().replace(" ", "_")