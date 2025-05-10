from typing import Iterator, Callable, Dict, Any
from collections.abc import Iterable

# 1. Redesign the processor interface: Iterator[str] -> Iterator[str]
Processor = Callable[[Iterator[str]], Iterator[str]]

# 2. Convert simple processors using a decorator or wrapper
def simple_processor_wrapper(func: Callable[[str], str]) -> Processor:
    """Wraps a simple str -> str function to work with the stream interface."""
    def wrapper(lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            yield func(line)
    return wrapper

# Example of a simple processor (reused)
def uppercase_processor(line: str) -> str:
    return line.upper()

# Applying the wrapper
uppercase_stream_processor = simple_processor_wrapper(uppercase_processor)

# 3. Stream-aware processor: Keeps a count of lines
def line_counting_processor(lines: Iterator[str]) -> Iterator[str]:
    """Keeps a count of lines and emits the count with each line."""
    count = 0
    for line in lines:
        count += 1
        yield f"{count}: {line}"

# 4. Stream-aware processor with fan-in: Joins every two lines
def join_pairs_processor(lines: Iterator[str]) -> Iterator[str]:
    """Joins every two consecutive lines."""
    line1 = None
    for line in lines:
        if line1 is None:
            line1 = line
        else:
            yield f"{line1} {line}"
            line1 = None
    if line1 is not None:
        # Handle odd number of lines, maybe emit the last one as is or with a marker
        yield f"孤立行: {line1}"

# 5. Stream-aware processor with fan-out and initialization: Splits lines on a delimiter
class SplitByDelimiterProcessor:
    def __init__(self, delimiter: str):
        self.delimiter = delimiter

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            for part in line.split(self.delimiter):
                yield part.strip()

# Example of initializing the splitting processor
comma_splitter = SplitByDelimiterProcessor(delimiter=",")

# 6. Stateful processor: Counts occurrences of a specific word
class WordCounterProcessor:
    def __init__(self, target_word: str):
        self.target_word = target_word.lower()
        self.word_counts = 0

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            self.word_counts += line.lower().split().count(self.target_word)
            yield f"'{self.target_word}' count in this line: {line.lower().split().count(self.target_word)}, Total count: {self.word_counts}, Line: {line}"

# Example of initializing the stateful word counter
python_counter = WordCounterProcessor(target_word="python")

# --- Pipeline Implementation ---

def process_pipeline(data: Iterable[str], processors: list[Processor]) -> Iterator[str]:
    """Processes data through a pipeline of stream processors."""
    stream = iter(data)
    for processor in processors:
        stream = processor(stream)
    return stream

# --- Example Usage ---
if __name__ == "__main__":
    input_data = [
        "hello world",
        "this is a test,string with,commas",
        "another line",
        "python is fun",
        "learning python"
    ]

    pipeline = [
        uppercase_stream_processor,
        comma_splitter,
        line_counting_processor,
        join_pairs_processor,
        python_counter
    ]

    output_stream = process_pipeline(input_data, pipeline)
    for output_line in output_stream:
        print(output_line)