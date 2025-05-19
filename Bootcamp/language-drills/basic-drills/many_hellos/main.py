import typer
import logging

from helloworld.sayhello import say_hello

app = typer.Typer()

@app.command()
def many(names: list[str], log_config: bool = False, log_all: bool = False):
    if log_all:
        logging.getLogger().setLevel(logging.DEBUG)
    elif log_config:
        logging.getLogger("helloworld.config").setLevel(logging.DEBUG)

    for name in names:
        typer.echo(say_hello(name))

if __name__ == "__main__":
    app()
