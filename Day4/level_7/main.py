import yaml
import sys
from engine import RoutingEngine
from metrics import Metrics
from dashboard import start_dashboard

if __name__ == "__main__":
    # Check if '--trace' flag is passed in the command line arguments
    trace_flag = "--trace" in sys.argv

    # Load configuration from YAML file
    with open("config.yaml") as f:
        config = yaml.safe_load(f)

    # Initialize metrics and start the dashboard
    metrics = Metrics()
    start_dashboard(metrics)  # Starts the FastAPI dashboard in a separate thread

    # Define the lines to be processed by the routing engine
    lines = [
        "ERROR: Disk full",
        "WARN: CPU high",
        "INFO: Server started"
    ]

    # Initialize and run the routing engine
    engine = RoutingEngine(config, metrics, enable_trace=trace_flag)
    engine.run(lines)
