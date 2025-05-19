import typer

app = typer.Typer()

@app.command()
def hello(name: str = "world"):
    """Say hello to someone, or 'world' by default."""
    print(f"Hello {name} 👋")

if __name__ == "__main__":
    app()
