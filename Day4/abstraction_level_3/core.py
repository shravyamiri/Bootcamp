from .types import ProcessorFn
from typing import List

def process_lines(lines: List[str], pipeline: List[ProcessorFn]) -> List[str]:
    processed = []
    for line in lines:
        for processor in pipeline:
            line = processor(line)
        processed.append(line)
    return processed
