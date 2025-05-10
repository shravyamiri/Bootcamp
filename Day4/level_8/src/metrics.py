# metrics.py
class Metrics:
    def __init__(self):
        # Initialize any attributes you need
        self.processed_files = 0

    def update(self, filename):
        # You can update the processing metrics here
        self.processed_files += 1
        print(f"File processed: {filename}")

    def get_stats(self):
        return {"processed_files": self.processed_files}
