from typing import Iterator, Callable
import itertools


# === 1. Wrapper: str -> str function to stream processor ===
def str_to_stream_processor(fn: Callable[[str], str]) -> Callable[[Iterator[str]], Iterator[str]]:
    def processor(lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            yield fn(line)

    return processor


# === 2. Stateless Processor Example: Uppercase ===
@str_to_stream_processor
def to_upper(line: str) -> str:
    return line.upper()


# === 3. Stateful Processor Example: Line Counter ===
class LineCounter:
    def __init__(self):
        self.count = 0

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            self.count += 1
            yield f"{self.count}: {line}"


# === 4. Fan-In Processor: Join Every 2 Lines ===
class JoinEveryNLines:
    def __init__(self, n: int):
        self.n = n

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        batch = []
        for line in lines:
            batch.append(line)
            if len(batch) == self.n:
                yield " | ".join(batch)
                batch = []
        if batch:
            yield " | ".join(batch)  # Optional: emit remaining lines


# === 5. Fan-Out Processor: Split by Delimiter ===
class SplitByDelimiter:
    def __init__(self, delimiter: str):
        self.delimiter = delimiter

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            parts = line.strip().split(self.delimiter)
            for part in parts:
                yield part.strip()
