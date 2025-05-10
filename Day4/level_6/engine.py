# engine.py
from typing import Iterator, Tuple, Dict, Callable
import importlib
from collections import defaultdict

TaggedLine = Tuple[str, str]

class StateRouter:
    def __init__(self, config: dict):
        self.graph: Dict[str, Callable[[Iterator[str]], Iterator[TaggedLine]]] = {}
        self.load_config(config)

    def load_config(self, config: dict):
        for node in config["nodes"]:
            tag = node["tag"]
            module_path = node["type"]
            module_parts = module_path.split(".")
            mod = importlib.import_module(".".join(module_parts[:-1]))
            processor = getattr(mod, module_parts[-1])()
            self.graph[tag] = processor

    def run(self, input_lines: Iterator[str]) -> Iterator[str]:
        queue = [("start", line) for line in input_lines]
        results = []

        while queue:
            tag, line = queue.pop(0)
            if tag == "end":
                results.append(line)
                continue
            if tag not in self.graph:
                raise ValueError(f"Unknown tag: {tag}")

            processor = self.graph[tag]
            for next_tag, next_line in processor.process(iter([line])):
                queue.append((next_tag, next_line))

        return iter(results)
