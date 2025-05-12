
# Level 6 – State-Based Routing System

This level focuses on implementing a **dynamic, tag-based routing engine** where each line of input moves through processors based on associated tags, similar to a state machine. This enables advanced workflows such as conditional logic, loops, and fan-out/fan-in processing.

---

## Features

* Dynamic routing based on tags.
* Each processor handles a specific tag.
* Processors can emit one or more `(tag, line)` outputs.
* Supports:

  * **Fan-out**: a line can go to multiple next tags.
  * **Fan-in**: multiple previous tags can direct lines to the same tag.
  * **Loops**: cycles in processing flow are supported.
* Execution ends when lines are tagged as `'end'`.

---

## How It Works

* The system starts by reading lines tagged `'start'`.

* A routing engine maintains a registry of tag-to-processor mappings.

* Processors are Python functions or classes implementing:

  ```python
  def process(lines: Iterator[str]) -> Iterator[Tuple[str, str]]:
      ...
  ```

* The routing engine maintains a processing queue and pushes lines through the appropriate processor based on the current tag.

* The system stops when no more lines are left, or all have reached `'end'`.

---

## Example Execution

Assume you have the following processors implemented in `processors/start.py`, `processors/filters.py`, and `processors/output.py`.

You can run the routing engine with the following steps:

### 1. Create your configuration file (e.g., `config.yaml`)

Create a yaml file

### 2. Run the system from the command line

```bash
python router.py --config config.json --input input.txt
```



## Directory Structure

```
project/
│
├── processors/
│   ├── start.py             
│   ├── filters.py           
│   └── output.py 
|   |----formatters.py
│
├── main.py                
├── config.yaml             
├── input.txt 
|----engine.py 
             
```

---

## Sample Command Outputs

You might see command-line prints such as:

```
[INFO] Processing line: "Disk full on server01"
[DEBUG] Tagging line with: error
[INFO] Routing line to: only_error
[DEBUG] Emitting line with tag: end
[INFO] Line completed.
```

Or errors like:

```
[ERROR] No processor registered for tag: unknown
[ERROR] Infinite loop detected for line: ...
```

---

## Checklist

* Routes lines dynamically based on tag.
* Supports start and end tags to manage flow boundaries.
* Validates tag-to-processor mappings on startup.
* Allows fan-out and fan-in behavior.
* Handles cycles and prevents infinite processing.
* Clean CLI execution with `--config` and `--input` flags.

---

## Reflections

* This abstraction allows complex workflows, retries, and dynamic paths.
* In a production or multi-node setup, you'd use queues or brokers to pass lines between nodes.
* The routing logic separates control flow from processing logic, improving maintainability and reusability.

