import typer
from dotenv import load_dotenv
import os

app = typer.Typer()

@app.command()
def process_file(
    input: str = typer.Option(..., help="Path to the input file"),
    output: str = typer.Option(None, help="Path to the output file (optional)"),
    mode: str = typer.Option("uppercase", help="Processing mode (uppercase or snakecase)"),
):
    """
    Processes the input file based on the specified mode.
    """
    typer.echo(f"Processing file: {input} with mode: {mode}")
    if output:
        typer.echo(f"Output will be written to: {output}")
    else:
        typer.echo("Output will be printed to stdout.")

    # Your main processing logic will go here based on the 'mode'
    # and reading from the 'input' file. If 'output' is provided,
    # write to it; otherwise, print to the console.

if __name__ == "__main__":
    app()