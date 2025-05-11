
# Level 2 – Modular Structure and Standardized Processing

In this level, the goal is to refactor the code into a modular and maintainable structure while introducing a standardized interface for text processing functions. This sets the foundation for future dynamic configurations and scalability.

---

## Objectives

* Refactor the CLI-based script into multiple well-organized modules.
* Use a standardized function signature for processors: `str -> str`.
* Create a static pipeline that applies multiple processors in sequence.
* Maintain the same command-line interface as Level 1.

---

## Directory Structure

```
abstraction-level-2/
├── main.py        
├── cli.py          
├── core.py         
├── pipeline.py     
└── types.py 
|----utils.py       
```

---

## Core Concepts

### Processor Function Signature

All processors must follow this format:

```python
def processor(line: str) -> str:
    ...
```

The common type is defined in `types.py`:

```python
ProcessorFn = Callable[[str], str]
```

---

## Implemented Processors

The following processors are implemented in `core.py`:

* `to_uppercase(line: str) -> str`
  Converts the input line to uppercase.

* `to_snakecase(line: str) -> str`
  Converts the input line to snake\_case format.

---

## Static Pipeline

* `pipeline.py` returns a list of processor functions.
* The pipeline is selected based on a `--mode` argument.
* Each line of the input file is passed through all processors in sequence.

---

## Usage

Run the program from the terminal:

```bash
python main.py --input input.txt --output output.txt --mode basic
```

---

## Design Principles

* **Modularity**: Each module handles one responsibility.
* **Reusability**: Adding new processors only requires editing `core.py` and `pipeline.py`.
* **Maintainability**: Clear structure avoids tangled logic.
* **Extensibility**: Designed to easily transition to dynamic loading in future levels.

---

## Checklist

* Folder contains the required 5 modules.
* `ProcessorFn = Callable[[str], str]` is used throughout.
*  Processors can be added without modifying core logic.
* Processors are applied in sequence to each line.
* CLI behavior works as before using Typer.
* `types.py` is used to prevent circular imports.

