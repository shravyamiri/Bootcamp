import typer
from rich import print

app = typer.Typer()

@app.callback()
def main(name: str):
    """Say hello directly."""
    print(f"[bold green]Hello {name}![/bold green]")

if __name__ == "__main__":
    app()
