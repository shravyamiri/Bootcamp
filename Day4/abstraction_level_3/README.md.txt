 Level 3 – Dynamic Config-Driven Text Processing Pipeline

 Overview

This project builds upon the modular CLI from Level 2 by introducing dynamic configuration via a pipeline.yaml file. Instead of hardcoding transformation logic, the pipeline is now completely configurable — users can specify a list of processors using dotted import paths.

This makes your application extensible, plugin-friendly, and easier to maintain.

Project Structure

abstraction-level-3/
├── main.py               # Entrypoint: input/output handling
├── cli.py                # Typer CLI interface
├── core.py               # Core processing logic
├── pipeline.py           # Loads pipeline steps from YAML config
├── types.py              # Shared ProcessorFn type
├── processors/           # User-defined processors
│   ├── snake.py          # to_snakecase processor
│   └── upper.py          # to_uppercase processor
└── pipeline.yaml         # Config file defining the processor pipeline
Requirements

pip install typer[all] python-dotenv pyyaml
pipeline.yaml Example

pipeline:
  - type: processors.snake.to_snakecase
  - type: processors.upper.to_uppercase
This defines a pipeline that:

Converts spaces to underscores and lowers the text
Converts the result to uppercase
You can easily swap, remove, or add custom processors by editing this file.

processors/ Module

Create your own processing functions inside processors/. Each function must follow the signature:

def my_processor(line: str) -> str:
    ...
CLI Usage

python main.py --input input.txt --config pipeline.yaml
Optional output:

python main.py --input input.txt --output output.txt --config pipeline.yaml
Example

input.txt:

Hello World
Python Scripts
pipeline.yaml:

pipeline:
  - type: processors.snake.to_snakecase
  - type: processors.upper.to_uppercase
Output:

HELLO_WORLD
PYTHON_SCRIPTS
Checklist

 Accepts a --config YAML file instead of --mode
 Dynamically loads processors using dotted import paths
 All processors follow str -> str signature
 Handles bad imports with clear error messages
 Extensible with custom or third-party processors
 Zero code changes needed to modify the pipeline