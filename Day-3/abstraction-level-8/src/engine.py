class RoutingEngine:
    def __init__(self, config, metrics, enable_trace=False):
        self.config = config
        self.metrics = metrics
        self.enable_trace = enable_trace

    def run(self, lines):
        """ Process the lines in the file """
        for line in lines:
            # Implement your line processing logic here (e.g., tagging or routing)
            print(f"Processing line: {line.strip()}")
        # Optionally, add trace for debugging
        if self.enable_trace:
            print("Tracing enabled.")

class Metrics:
    def __init__(self):
        self.processed_files = []

    def update(self, file_name):
        """ Track the file processed """
        self.processed_files.append(file_name)

    def get_processed_files(self):
        """ Return the list of processed files """
        return self.processed_files
