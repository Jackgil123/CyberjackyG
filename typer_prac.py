import typer

app = typer.Typer()

name = "jack"

@app.command()
def hello(name: str):
    """Greet a person with their name."""
    print(f"Hello, {name}!")

def goodbye(name: str):
    print(f"Goodbye, {name}!")

if __name__ == "__main__":
    app()

    