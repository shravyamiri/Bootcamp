
# Level 3 – Dynamic Config-Driven Pipeline

This level introduces configuration-driven pipelines using YAML files and dynamic imports. The goal is to decouple processor logic from the codebase so that users can specify and modify the processing flow without editing source code.

---

## Key Concepts

* **Dynamic Importing**: Load processor functions at runtime using dotted import paths.
* **YAML-based Configuration**: Define the pipeline in a separate `pipeline.yaml` file.
* **Extensibility**: Users can add or remove processors by updating the config file, without touching Python code.
* **Abstraction**: Separates pipeline configuration from implementation for better modularity.

---

## Directory Structure

```
level-3/
├── main.py              
├── cli.py               
├── core.py              
├── pipeline.py          
├── types.py             
├── pipeline.yaml        
└── processors/
    ├── upper.py         
    └── snake.py
    |----__init__.py
```

---

## How It Works

1. **Define Pipeline in YAML**

   The configuration file (`pipeline.yaml`) looks like this:

   ```yaml
   pipeline:
     - type: processors.snake.to_snakecase
     - type: processors.upper.to_uppercase
   ```

2. **Dynamic Loading**

   The `pipeline.py` module:

   * Parses the YAML file.
   * Dynamically imports each function using its dotted path.
   * Composes a list of processor functions.

3. **Run the Program**

   Instead of using `--mode`, the CLI now takes a config file:

   ```bash
   python main.py --input input.txt --output output.txt --config pipeline.yaml
   ```

---

## Processor Format

All processors must follow this function signature:

```python
def processor(line: str) -> str:
    ...
```

Each processor should accept a string and return a transformed string.

---

## Error Handling

* If a processor import path is invalid, a clear error message is shown.
* If the imported object is not callable, an error is raised.
* The pipeline fails fast on configuration errors.

---

## Benefits

* Easy to customize processing steps.
* Enables reuse of processors across projects.
* Allows third-party plugin support through dynamic importing.

---

## Next Steps

* Introduce streaming processors to allow fan-in/fan-out and stateful operations.
* Add input validation for YAML configurations.
* Extend the CLI to include built-in processor listing or debugging tools.

