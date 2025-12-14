import typer
from jcl_validator import validate_jcl
from dataset_checker import check_dataset

app = typer.Typer()

@app.command()
def jcl(file: str):
    validate_jcl(file)

@app.command()
def dataset(name: str):
    check_dataset(name)

if __name__ == "__main__":
    app()