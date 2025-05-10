Level 4 – Stream-Based Text Processing with Stateful and Configurable Processors

Overview

This level transforms the pipeline from simple line-by-line functions (str -> str) into stream-based processors (Iterator[str] -> Iterator[str]), unlocking the power of:

Emitting multiple output lines per input line (fan-out)
Merging multiple input lines into one output (fan-in)
Maintaining internal state across the stream
Accepting custom configuration per processor
This design mimics real-world data processing frameworks and paves the way for routing and branching in future levels.

Project Structure

abstraction-level-4/
├── main.py               # Orchestrates reading, processing, writing
├── cli.py                # Handles CLI arguments via Typer
├── core.py               # Stream-based processor interface & adapters
├── pipeline.py           # Dynamically loads processor classes from config
├── types.py              # Shared types (e.g., ProcessorFn)
├── processors/
│   ├── snake.py          # Stateless wrapper: to_snakecase
│   ├── upper.py          # Stateless wrapper: to_uppercase
│   ├── counter.py        # Stateful: Adds line numbers
│   └── splitter.py       # Fan-out: Splits line on delimiter
└── pipeline.yaml         # Processor config with optional parameters
🔧 Requirements

pip install typer[all] python-dotenv pyyaml
Processor Interface (NEW)

All processors now implement:

def process(stream: Iterator[str]) -> Iterator[str]
For stateful or configurable processors, use a class-based approach:

class LineCounter:
    def _init_(self, start: int = 1):
        self.count = start

    def _call_(self, stream: Iterator[str]) -> Iterator[str]:
        for line in stream:
            yield f"{self.count}: {line}"
            self.count += 1
Reusing str -> str Processors

A decorator or wrapper is used to adapt str -> str functions to stream-based processors:

def adapt_line_processor(fn: Callable[[str], str]) -> Callable[[Iterator[str]], Iterator[str]]:
    def wrapped(stream: Iterator[str]) -> Iterator[str]:
        for line in stream:
            yield fn(line)
    return wrapped
Example pipeline.yaml

pipeline:
  - type: processors.splitter.Splitter
    config:
      delimiter: ","
  - type: processors.upper.to_uppercase
  - type: processors.counter.LineCounter
    config:
      start: 100
Usage

python main.py --input input.txt --config pipeline.yaml
Optional:

python main.py --input input.txt --output output.txt --config pipeline.yaml
Example Input

input.txt:

one,two
three,four
Output (based on pipeline above):

100: ONE
101: TWO
102: THREE
103: FOUR
Checklist

 All processors now accept Iterator[str] and return Iterator[str]
 Stateless str -> str functions adapted via wrapper
 Fan-out processor: Splitter emits multiple lines
 Stateful processor: LineCounter keeps track of line numbers
 Configurable processors use constructor config from YAML
 System is extensible with minimal boilerplate
 Processors are testable in isolation
Processor Types

Name	Type	Description
to_uppercase	Stateless	Uppercases each line
to_snakecase	Stateless	Converts to lowercase and replaces spaces
Splitter	Fan-out	Splits a line by a delimiter and emits many lines
LineCounter	Stateful	Prepends line numbers, keeps internal state