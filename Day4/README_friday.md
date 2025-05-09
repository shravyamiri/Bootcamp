Friday 09/05/25 checkin
# Level 0 - Basic Script (No Abstraction)

This level focuses on creating a simple, single-purpose Python script without any functions or external libraries. It serves as the starting point for refactoring and improvement in later levels.

## Task

Write a Python script named `process.py` that:

* Reads the stdin line by line.
* Strips leading and trailing whitespace from each line.
* Converts the result to uppercase.
* Prints the processed lines to stdout.

Put everything in a single file named `process.py`.

## Constraints

* No functions allowed. The code should be purely sequential, top-to-bottom.
* Use only Python built-in tools. Do not import any external libraries.

## Running the Script

1.  Save the code in a file named `process.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved `process.py`.
4.  You can provide input to the script in a couple of ways:

    * **Piping from another command:**
        ```bash
        echo "  hello world  " | python process.py
        ```
    * **Typing input directly (press Enter after each line, Ctrl+D or Ctrl+Z then Enter to end input):**
        ```bash
        python process.py
        this is a line
          with spaces
        another one
        ```

## Expected Output

For the input:
hello world

with spaces
another one
The script should produce the following output:

HELLO WORLD
WITH SPACES
ANOTHER ONE


# Level 1 - Parameters and CLI Interface

This level focuses on turning a one-off script into a basic parameterized command-line tool. The goal is to make the script more configurable and reusable by accepting command-line arguments and using environment defaults.

Refactor your script to:

* Use `typer` to define a command-line interface.
* Accept the following command-line arguments:
    * `--input`: input file path (required)
    * `--output`: output file path (optional)
    * `--mode`: processing mode (optional, defaults via `.env`)
* Load default values (specifically for the `mode`) from a `.env` file using `python-dotenv`.
* Implement different processing behaviors based on the `mode`.

## Supported Modes

The script should support the following processing modes:

* `uppercase`: convert each line of the input file to uppercase.
* `snakecase`: replace spaces in each line with underscores and convert the line to lowercase.

## Guidance: Start Thinking in Functions

Even though you are still allowed to keep everything in one file, you should begin to break up your logic into small functions such as:

* `read_lines(path: str) -> Iterator[str]`
* `transform_line(line: str, mode: str) -> str`
* `write_output(lines: Iterator[str], output_path: Optional[str]) -> None`

These don't need to be in separate modules yet, but the idea is to prepare for that in the next level.

## Example Usage

```bash
python your_script_name.py --input input.txt
python your_script_name.py --input input.txt --mode snakecase
python your_script_name.py --input input.txt --output output.txt

![Screenshot 2025-05-09 142730](https://github.com/user-attachments/assets/fb5237c3-5f3e-47c8-b686-7e0d776314c3)

# Level 2 - Modular Structure and Standardized Processing

This level focuses on refactoring a simple command-line script into a more modular and structured program. The goal is to achieve a clean separation of concerns and define a standard interface for processing functions, laying the groundwork for future extensibility.

## Project Structure

The project is organized into the following modules within the `abstraction_level_2` directory:

Markdown

# Level 2 - Modular Structure and Standardized Processing

This level focuses on refactoring a simple command-line script into a more modular and structured program. The goal is to achieve a clean separation of concerns and define a standard interface for processing functions, laying the groundwork for future extensibility.

## Project Structure

The project is organized into the following modules within the `abstraction_level_2` directory:

abstraction_level_2/
├── main.py     # Entry point: Imports and runs the Typer app
├── cli.py      # Command-line interface definition using Typer
├── core.py     # Implementation of the processing functions (transformations)
├── pipeline.py # Logic for creating and applying a pipeline of processors
└── types.py    # Definition of custom types (e.g., ProcessorFn)
└── utils.py    # Utility functions (e.g., file reading and writing)

![Screenshot 2025-05-09 143653](https://github.com/user-attachments/assets/781d6d77-2b85-469e-8266-26acf3a346c9)
