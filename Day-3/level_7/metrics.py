from collections import defaultdict, deque
import time
import threading

class Metrics:
    def __init__(self):
        self.counts = defaultdict(int)
        self.times = defaultdict(float)
        self.errors = defaultdict(list)
        self.traces = deque(maxlen=1000)
        self.lock = threading.Lock()

    def record(self, processor, start_time, end_time, error=None):
        with self.lock:
            self.counts[processor] += 1
            self.times[processor] += end_time - start_time
            if error:
                self.errors[processor].append(str(error))

    def add_trace(self, trace):
        with self.lock:
            self.traces.append(trace)

    def get_stats(self):
        with self.lock:
            return {
                p: {
                    'count': self.counts[p],
                    'time': round(self.times[p], 4),
                    'errors': len(self.errors[p])
                } for p in self.counts
            }

    def get_traces(self):
        with self.lock:
            return list(self.traces)

    def get_errors(self):
        with self.lock:
            return self.errors
