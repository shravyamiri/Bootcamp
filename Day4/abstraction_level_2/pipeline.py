# abstraction_level_2/pipeline.py
from typing import List
from .core import to_uppercase, to_snakecase
from .types import ProcessorFn

def create_pipeline(mode: str) -> List[ProcessorFn]:
    """Creates a pipeline of processor functions based on the mode."""
    pipeline: List[ProcessorFn] = []
    if mode == "uppercase":
        pipeline.append(to_uppercase)
    elif mode == "snakecase":
        pipeline.append(to_snakecase)
    else:
        raise ValueError(f"Unsupported mode: {mode}")
    return pipeline

def apply_pipeline(line: str, pipeline: List[ProcessorFn]) -> str:
    """Applies a list of processor functions to a single line."""
    processed_line = line
    for processor in pipeline:
        processed_line = processor(processed_line)
    return processed_line