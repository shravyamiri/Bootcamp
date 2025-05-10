from engine import DAGEngine
from config import pipeline_config

if __name__ == "__main__":
    input_lines = [
        " ERROR: Disk failure",
        " WARN: Low battery",
        "User login successful",
        " ERROR: Network down",
        "System update complete"
    ]

    engine = DAGEngine(pipeline_config)
    engine.run(input_lines)
