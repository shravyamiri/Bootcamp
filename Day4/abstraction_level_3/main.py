from cli import parse_args
from core import process_lines
from pipeline import load_pipeline
from .types import ProcessorFn

from types import ProcessorFn


def main():
    args = parse_args()

    with open(args.input, 'r') as f:
        lines = f.readlines()

    pipeline = load_pipeline(args.config)
    output_lines = process_lines(lines, pipeline)

    for line in output_lines:
        print(line.strip())

if __name__ == "__main__":
    main()
