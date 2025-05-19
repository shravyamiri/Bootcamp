import typer
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def hello(name: str = "World"):
    """Say hello with rich formatting"""
    console.print(f"[bold green]Hello {name}! 👋[/bold green]")

def main():
    app()
