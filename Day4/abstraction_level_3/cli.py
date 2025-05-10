import argparse
# Import ProcessorFn from your custom types.py file (not from the built-in types)
from types import ProcessorFn
from .types import ProcessorFn

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to input file")
    parser.add_argument("--config", required=True, help="Path to YAML config file")
    return parser.parse_args()
