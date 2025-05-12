

# Level 7 – Observability and System Introspection

This level adds real-time observability to your file processing engine. It allows system operators, developers, and data engineers to view metrics, execution traces, and errors live through a web dashboard.

---

## Key Objectives

* Add real-time metrics tracking per processor
* Enable optional execution tracing for each line
* Serve metrics, traces, and error logs via a FastAPI web dashboard
* Run the dashboard concurrently with the processing engine

---

## Real-World Motivation

* Data engineers monitor how many lines each processor handles
* Developers debug issues by tracing the path of a record
* Operators identify performance bottlenecks and error-prone processors
* Dashboards are essential for transparency, diagnostics, and alerts

---

## Core Features

### 1. Metrics Layer

* Track number of lines processed per processor
* Record total processing time per processor
* Count number of exceptions or retries per processor

### 2. Execution Tracing (Optional)

* Each line carries a trace list showing the path it followed (e.g., `["start", "warn", "end"]`)
* Last N (e.g., 1000) traces stored in memory
* Tracing enabled with `--trace` command-line flag

### 3. Web Dashboard (FastAPI)

* Runs in a background thread alongside the processor
* Exposes these endpoints:

  * `/stats`: Processor metrics (count, time, errors)
  * `/trace`: List of recent execution traces
  * `/errors`: Recent error logs with processor names and messages

### 4. Concurrency Design

* Dashboard accesses shared memory (e.g., dictionaries, queues, counters)
* Uses thread-safe data structures or locks as needed
* Main processing remains responsive under load

---

## Command-Line Usage

```bash
# Run with tracing disabled (default)
python main.py

# Run with tracing enabled
python main.py --trace
```

---

## API Endpoints (Localhost Default)

* `GET /stats` – Returns metrics per processor:

  ```json
  {
    "filter_errors": { "count": 120, "time": 1.23, "errors": 2 },
    "tag_router": { "count": 300, "time": 2.55, "errors": 0 }
  }
  ```

* `GET /trace` – Returns last N execution traces:

  ```json
  [
    ["start", "info", "end"],
    ["start", "warn", "retry", "end"]
  ]
  ```

* `GET /errors` – Returns recent errors:

  ```json
  [
    { "processor": "tag_router", "message": "KeyError: 'tag'" },
    { "processor": "filter_errors", "message": "ValueError: empty line" }
  ]
  ```

---

## Implementation Notes

* Metrics and traces are stored in shared Python data structures (e.g., `collections.Counter`, `deque`)
* FastAPI server runs in a background thread using `uvicorn`
* Optional logging or log rotation may be added for persistence

---

## Checklist

* Shared metrics store is updated by processors
* Execution traces are collected if tracing is enabled
* FastAPI server exposes `/stats`, `/trace`, and `/errors`
* Dashboard runs in parallel without blocking the main engine
* CLI flag allows tracing to be toggled
* Errors are captured and visible through the API

---

## Reflection

* Observability enables real-time introspection, making the system easier to debug and maintain
* In a distributed setup, centralized metrics collection (e.g., Prometheus, Grafana, or ELK stack) would be needed
* A full production dashboard might include graphs, filters, alerting rules, uptime monitoring, and logs from multiple nodes

