import argparse
from processor import process_file, watch_directory

def main():
    parser = argparse.ArgumentParser(description="File Processor CLI")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--input', type=str, help="Process a single file and exit")
    group.add_argument('--watch', action='store_true', help="Watch directory and process incoming files")
    parser.add_argument('--debug', action='store_true', help="Enable debug logging")

    args = parser.parse_args()

    if args.debug:
        import logging
        logging.basicConfig(level=logging.DEBUG)

    if args.input:
        process_file(args.input)
    elif args.watch:
        watch_directory("watch_dir/unprocessed")

if __name__ == '__main__':
    main()
