from metrics import Metrics
from importlib import import_module
import time

class RoutingEngine:
    def __init__(self, config, metrics, enable_trace=False):
        self.nodes = {}
        self.metrics = metrics
        self.enable_trace = enable_trace
        for node in config['nodes']:
            tag = node['tag']
            module_path = node['type']
            mod = import_module(module_path)
            self.nodes[tag] = mod.Processor()

    def run(self, lines):
        queue = [("start", line, []) for line in lines]

        while queue:
            tag, line, trace = queue.pop(0)
            processor = self.nodes.get(tag)
            if processor:
                new_trace = trace + [tag]
                start = time.time()
                try:
                    for out_tag, out_line in processor.process([(tag, line)]):
                        if out_tag == "end":
                            if self.enable_trace:
                                self.metrics.add_trace(new_trace + [out_tag])
                            continue
                        queue.append((out_tag, out_line, new_trace))
                    end = time.time()
                    self.metrics.record(tag, start, end)
                except Exception as e:
                    end = time.time()
                    self.metrics.record(tag, start, end, error=e)
