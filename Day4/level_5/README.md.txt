Level 5 – DAG-Based Routing and Conditional Line Processing

Overview

In this level, we evolve from linear, static pipelines to a fully dynamic DAG-based (Directed Acyclic Graph) processing engine. This allows lines to follow different paths based on content, tags, or type — supporting conditional routing, fan-in/fan-out behavior, and multi-stage workflows.

What This Unlocks
Route different line types (e.g., errors, warnings, info) through different logic
Build branching logic via config
Enable line classification and routing
Scale to real-world log and data stream use cases
Project Structure

abstraction-level-5/
├── main.py                  # DAG engine entrypoint
├── cli.py                   # CLI interface with Typer
├── dag_engine.py            # DAG processor runner and router logic
├── processor_loader.py      # Loads processors dynamically
├── types.py                 # TaggedLine, ProcessorFn types
├── config.yaml              # DAG configuration
└── processors/
    ├── trim.py              # Trims whitespace
    ├── taggers.py           # Tagging processors (e.g. tag_error)
    ├── counters.py          # Stateful counters
    └── printer.py           # Prints to stdout
🔧 Key Concepts

Processor Output Format
Processors now yield (tag, line) pairs:

yield ("errors", "Disk error at block 23")
yield ("general", "All systems operational")
DAG Nodes
Each node in the DAG has:

A name
A processor (import path)
A list of routes (tag → destination nodes)
Defined in config.yaml.

Example Use Case

Input Lines
ERROR: Disk full
WARNING: High memory usage
INFO: System booted
Flow (defined in config)
trim → strips whitespace
tagger → emits tags: error, warning, general
Router sends:
error → counter, then archive
warning → counter
general → printer
Example config.yaml

nodes:
  - name: trim
    processor: processors.trim.strip_whitespace
    routes:
      "*": tagger

  - name: tagger
    processor: processors.taggers.route_by_prefix
    routes:
      error: error_counter
      warning: warning_counter
      general: printer

  - name: error_counter
    processor: processors.counters.CountProcessor
    routes:
      "*": archiver

  - name: warning_counter
    processor: processors.counters.CountProcessor

  - name: archiver
    processor: processors.printer.archive_to_file

  - name: printer
    processor: processors.printer.print_to_console
Usage

python main.py --input logs.txt --config config.yaml
Checklist

 Processors now yield (tag, line) instead of just line
 DAG is defined in YAML with named nodes, processors, and routing rules
 Lines can take different paths based on their tags
 Fan-out (1 → N) and fan-in (N → 1) supported
 Support for stateful processors (e.g., counters)
 Configurable routing and dynamic import of processors
Example Output

[printer] INFO: System booted
[archiver] ERROR: Disk full
(Plus internal counters logged/stored as needed.)

Extensibility

This architecture supports:

Third-party processors
Arbitrary DAGs
Conditional branching
Parallel and independent routes
Future: DAG visualization, Web UI, plugin system
Developer Tips

Each processor should implement:
def process(stream: Iterator[TaggedLine]) -> Iterator[TaggedLine]
Use the TaggedLine = Tuple[str, str] alias from types.py
Create stateful processors as classes (with _call_)