
# Level-1 Command-Line Text Processor

This project is a basic, parameterized command-line tool for processing text files. It uses `typer` for the CLI and supports configurable processing modes via a `.env` file.

## Features

* Accepts command-line arguments for input, output, and processing mode
* Loads default values (like mode) from a `.env` file using `python-dotenv`
* Supports multiple processing modes:

  * `uppercase`: Converts each line to uppercase
  * `snakecase`: Replaces spaces with underscores and converts to lowercase
* Can print results to stdout or write to an output file
* Logic is modular and organized into functions

## Installation

1. Clone the repository or copy the script.

2. Install required dependencies:

   ```
   pip install typer[all] python-dotenv
   ```

3. Create a `.env` file in the same directory with the following content:

   ```
   MODE=uppercase
   ```

## Usage

Run the script from the command line:

* Process a file with default settings (mode from `.env` and print to stdout):

  ```
  python process.py --input input.txt
  ```

* Specify a different mode:

  ```
  python process.py --input input.txt --mode snakecase
  ```

* Write the output to a file:

  ```
  python process.py --input input.txt --output out.txt
  ```

## Functions

* `read_lines(path: str) -> Iterator[str]`: Reads lines from the input file
* `transform_line(line: str, mode: str) -> str`: Applies the transformation based on mode
* `write_output(lines: Iterator[str], output_path: Optional[str]) -> None`: Writes transformed lines to a file or stdout

## Requirements

* Python 3.7+
* typer
* python-dotenv

## Next Steps

* Break the functions into separate modules for better organization
* Add unit tests for each function

