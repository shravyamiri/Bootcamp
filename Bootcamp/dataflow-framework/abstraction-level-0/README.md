
# Level-0  Basic Text Processing Script

This is a simple Python script that reads lines from standard input, processes them, and prints the results to standard output. It is intended as a starting point before introducing abstraction or modularity.

## Features

* Reads input line by line from standard input (stdin)
* Strips leading and trailing whitespace from each line
* Converts each line to uppercase
* Prints the processed lines to standard output (stdout)

## File

* `process.py`

## Requirements

* Python 3 (any recent version)
* No external dependencies required

## Usage

You can run the script from the command line and provide input manually or through file redirection.

### Manual Input Example

```bash
python process.py
```

Then type your input, and press `Ctrl+D` (or `Ctrl+Z` on Windows) to end input:

```
hello world    
 this is a test 
```

Output:

```
HELLO WORLD
THIS IS A TEST
```

### Using a File as Input

```bash
python process.py < input.txt
```

## Constraints

* No functions are used; the code runs sequentially from top to bottom.
* Only Python built-in functions and libraries are used.

## Checklist

* The script produces expected output when given input
* It runs without errors from the command line
* No abstraction or refactoring has been applied yet

