
# Level 4 – Stream Processing and State

This project introduces a more flexible and powerful stream processing model. Instead of processing one line at a time, processors now operate on entire streams of lines. This enables features like emitting multiple lines per input, combining inputs, and maintaining internal state across lines.

---

## Why Stream Processing?

Traditional `str -> str` processors are simple but limited. They:

* Can't drop or emit multiple lines.
* Can't join multiple lines into one.
* Can't keep internal state like counters or buffers.

Stream-based processors solve these limitations by treating the input as an iterator of lines and yielding transformed lines as output.

---

## Project Structure

```
level_4/
│
├── main.py             
├── processors.py        
├── test_processors.py   
├── README.md            
├── output.png           
└── .idea/               
```

---

## Key Features

* **Stream-Based Processing:** Each processor handles a stream of lines and returns a stream.
* **Stateful Processors:** Supports processors with internal state, such as counters or buffers.
* **Configurable Behavior:** Some processors are initialized with parameters.
* **Reusable Decorators:** Wrap existing `str -> str` functions for compatibility with the new stream format.
* **Fan-in and Fan-out:** Processors can merge multiple lines or split one line into many.

---

## How to Run

1. Open `main.py`.
2. Inside, define your list of processors and how data flows.
3. Run the script:

```bash
python main.py
```

4. The results will be printed or written to a file, depending on your implementation.

---

## Example Processors

### Stateless: Trimming Lines

```python
def trim(lines):
    for line in lines:
        yield line.strip()
```

### Stateful: Line Counter

```python
class LineCounter:
    def __init__(self):
        self.count = 0

    def __call__(self, lines):
        for line in lines:
            self.count += 1
            yield f"{self.count}: {line}"
```

### Fan-in: Combine Every Two Lines

```python
class JoinPairs:
    def __call__(self, lines):
        buffer = []
        for line in lines:
            buffer.append(line)
            if len(buffer) == 2:
                yield " | ".join(buffer)
                buffer.clear()
```

### Fan-out: Split by Delimiter

```python
class SplitOnDelimiter:
    def __init__(self, delimiter=","):
        self.delimiter = delimiter

    def __call__(self, lines):
        for line in lines:
            for part in line.split(self.delimiter):
                yield part
```

---

## Reusing str -> str Processors

You can wrap legacy single-line functions like this:

```python
def wrap(fn):
    def processor(lines):
        for line in lines:
            result = fn(line)
            if result is not None:
                yield result
    return processor
```

---

## Testing

All processors are tested in `test_processors.py` using basic unit tests. Example:

```python
def test_line_counter():
    lines = ["first", "second"]
    processor = LineCounter()
    assert list(processor(iter(lines))) == ["1: first", "2: second"]
```

Run your tests with:

```bash
pytest test_processors.py
```

---

## Summary

This level upgrades your processing architecture to support streaming behavior, enabling real-world use cases such as log processing, message transformation, and complex data pipelines. The processors are modular, testable, and support both stateless and stateful operations.


