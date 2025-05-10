# abstraction_level_3/cli.py
import typer
from dotenv import load_dotenv
import os
from .pipeline import load_pipeline_from_config, apply_pipeline
from .utils import read_lines, write_output

load_dotenv()
app = typer.Typer()

@app.command()
def process_file(
    input: str = typer.Option(..., help="Path to the input file"),
    config: str = typer.Option("pipeline.yaml", help="Path to the pipeline configuration file"),
    output: str = typer.Option(None, help="Path to the output file (optional)"),
):
    """
    Processes the input file based on the pipeline defined in the configuration file.
    """
    typer.echo(f"Processing file: {input} using config: {config}")
    if output:
        typer.echo(f"Output will be written to: {output}")

    try:
        lines = read_lines(input)
        pipeline = load_pipeline_from_config(config)
        processed_lines = [apply_pipeline(line, pipeline) for line in lines]
        write_output(processed_lines, output)

    except FileNotFoundError as e:
        typer.echo(f"Error: {e}")
    except ValueError as e:
        typer.echo(f"Error: {e}")
    except ImportError as e:
        typer.echo(f"Error: {e}")
    except AttributeError as e:
        typer.echo(f"Error: {e}")
    except TypeError as e:
        typer.echo(f"Error: {e}")
    except Exception as e:
        typer.echo(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    app()