Level 6 – State-Based Routing System

Overview

This level introduces a state-machine-style routing engine where processors are not hard-wired in pipelines or DAGs but instead registered under tag names. Each line carries a tag that determines which processor should handle it next, enabling dynamic routing, cycles, retries, and flexible logic paths.

You're now building a general-purpose stream processor and router, suitable for real-world systems like:

Log classification and filtering
Data enrichment workflows
Feedback and retry loops
Conditional multi-stage transformations
Key Concepts

Tags = States: Each line is tagged, and its tag determines where it goes.
Processors = State Handlers: Each processor is registered to handle a specific tag.
Transitions = Output Tags: A processor emits (tag, line) pairs.
Router: Receives lines and routes them to processors based on their tag.
Fan-out/Fan-in: One tag can emit multiple tags, and one tag can receive from multiple tags.
Entry Point: All lines start with tag start.
Exit Point: When a processor emits tag end, that line exits the system.
Project Structure

abstraction-level-6/
├── main.py                 # Entry point
├── router.py               # Routing engine and line dispatch
├── processor_registry.py   # Maps tags to processor callables
├── types.py                # TaggedLine = Tuple[str, str]
├── config.yaml             # Tag → processor mapping
└── processors/
    ├── start.py            # Emits lines with initial tags
    ├── filters.py          # Filters by tag or content
    ├── formatters.py       # Formatting processors
    └── output.py           # End processors like terminal output or archiving
Example config.yaml

nodes:
  - tag: start
    type: processors.start.tag_lines

  - tag: error
    type: processors.filters.only_error

  - tag: warn
    type: processors.filters.only_warn

  - tag: general
    type: processors.formatters.snakecase

  - tag: end
    type: processors.output.terminal
How It Works

Initialization
Load processors from config.yaml
Create a map: tag -> processor function
Execution Loop
Start with all input lines tagged start
For each (tag, line):
Look up the corresponding processor for tag
Run processor, yielding new (tag, line) pairs
If tag == end, the line exits the system
Fan-Out and Fan-In
A processor can emit multiple tags for a line (e.g. "warn", line and "general", line)
Multiple processors may emit lines with the same tag
Run the Program

python main.py --input input.txt --config config.yaml
Features Checklist

 Tag-based routing system
 start as entry point and end as termination
 Dynamic processor registration via config
 Fan-in / Fan-out supported
 Supports cycles and repeated tags
 Clear separation of routing logic and processors
 Guards against infinite loops (configurable or capped)
 Modular and extensible design
Example Line Flow

Input line: "WARNING: CPU spike"
 → start → tag_lines → ("warn", line)
 → warn → only_warn → ("end", formatted_line)
 → end → terminal → outputs result
Design Notes

All processors implement:
def process(lines: Iterator[TaggedLine]) -> Iterator[TaggedLine]
TaggedLine is a Tuple[str, str], where the first element is the tag/state.
Each tag maps to a single processor in the config file.
Lines can revisit the same processor if re-tagged accordingly.