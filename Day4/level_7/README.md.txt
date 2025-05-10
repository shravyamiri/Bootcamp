Level 7: Observability and System Introspection

Welcome to Level 7 of your modular, processor-based pipeline system. This level introduces real-time observability via metrics collection, tracing, and a live FastAPI dashboard.

Features

Metrics & Stats
Track number of lines received/emitted per processor.
Measure processing time per processor.
Count of errors raised in each node.
Execution Tracing
Track the route taken by each line as a list of tags (e.g., ["start", "warn", "end"]).
Store a window of the last N traces for inspection.
Enabled via --trace flag in CLI.
Live Web Dashboard
Hosted via FastAPI on http://localhost:8000
Endpoints:
/stats: Real-time metrics per processor.
/trace: List of last N traced lines (if tracing is enabled).
/errors: Recent processor-level errors.
Concurrency Safe
Dashboard runs in a background thread
Shared state for metrics, traces, and errors is protected using locks.
🏗 Directory Structure

level-7-observability/
├── main.py
├── cli.py
├── core.py
├── pipeline.py
├── router.py
├── types.py
├── processors/
│   ├─unprocessed,processes,underproccesed
 
├── config.yaml
├── observability/
│   ├── metrics.py      # Tracks counts, timings, and errors
│   ├── trace.py        # Stores traces of lines
│   ├── dashboard.py    # FastAPI app running in background
└── README.md
Example Usage

python main.py --input input.txt --config config.yaml --trace
Then visit:
 http://localhost:8000/stats
 http://localhost:8000/trace
 http://localhost:8000/errors
http://localhost:8000/health

 Configuration File (config.yaml)

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
 Observability Internals

