# abstraction_level_2/cli.py
import typer
from dotenv import load_dotenv
import os
from .pipeline import create_pipeline, apply_pipeline
from .utils import read_lines, write_output  # We'll create utils.py next

load_dotenv()
app = typer.Typer()

@app.command()
def process_file(
    input: str = typer.Option(..., help="Path to the input file"),
    output: str = typer.Option(None, help="Path to the output file (optional)"),
    mode: str = typer.Option(
        os.getenv("PROCESSING_MODE", "uppercase"),
        help="Processing mode (uppercase or snakecase)",
    ),
):
    """
    Processes the input file based on the specified mode.
    """
    typer.echo(f"Processing file: {input} with mode: {mode}")

    try:
        lines = read_lines(input)
        pipeline = create_pipeline(mode)
        processed_lines = [apply_pipeline(line, pipeline) for line in lines]
        write_output(processed_lines, output)

    except FileNotFoundError:
        typer.echo(f"Error: Input file not found at '{input}'")
    except ValueError as ve:
        typer.echo(f"Error: {ve}")
    except Exception as e:
        typer.echo(f"An error occurred: {e}")

if __name__ == "__main__":
    app()