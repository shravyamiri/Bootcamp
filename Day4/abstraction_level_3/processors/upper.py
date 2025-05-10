# abstraction_level_3/processors/upper.py
from ..types import ProcessorFn

def to_uppercase(line: str) -> str:
    """Converts a line to uppercase."""
    return line.upper()