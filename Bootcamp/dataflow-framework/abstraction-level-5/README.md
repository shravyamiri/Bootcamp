# Level 5 – DAG Routing and Conditional Flows

This project builds a **content-aware, DAG-based processing engine** for line-based inputs such as logs. Instead of processing all lines uniformly, this engine **routes each line through different processing paths** based on its content or dynamically assigned tags.

---

## Problem This Solves

In real-world data pipelines, not every line of input should be processed the same way. Some may require archiving, others may need counting, while others may just be printed. A **static pipeline fails** in such cases.

This engine introduces:

* Conditional processing
* DAG-based routing
* Modular processors
* Fully configurable flow behavior

---

##  How It Works

### 1. Each line is processed as a `(tag, line)` pair

Processors emit tagged lines. Tags determine which processor(s) the line goes to next.

### 2. The DAG routing is defined in `config.py`

* You define available processors
* You define routing rules as Python dictionaries
* No need for external YAML/JSON

### 3. The main components:

| File           | Purpose                                                  |
| -------------- | -------------------------------------------------------- |
| `main.py`      | Entry point. Reads input, runs engine, writes output     |
| `engine.py`    | Core DAG engine that routes tagged lines to processors   |
| `processor.py` | All processor functions (e.g., trim, tag, count, format) |
| `config.py`    | Routing rules and processor map                          |
| `input.txt`    | Input data lines                                         |
| `output.txt`   | Final output file                                        |

---

## Example Scenario

### Input lines (in `input.txt`):

```
ERROR: Disk space low
WARNING: High memory usage
INFO: Job completed successfully
```

### Desired flow:

1. **All lines →** `trim` processor
2. **Then →** `tagger` processor (applies: `errors`, `warnings`, or `general`)
3. **Routing based on tags:**

   * `errors → count → archive`
   * `warnings → tally`
   * `general → format → output`

---

## Running the Code

Make sure you are in the `level_5` directory. Then run:

```bash
python main.py
```

This will:

* Read `input.txt`
* Route and process each line using the DAG engine
* Write results to `output.txt`

---


##  Key Features

* Modular processors – easy to extend
* Content-based routing via tags
* Fan-out and conditional flows supported
* Pure Python config (no YAML or JSON required)
* Clean separation of logic

---



