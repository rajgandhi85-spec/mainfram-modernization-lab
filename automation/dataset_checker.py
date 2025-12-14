import re
from rich import print

PATTERN = r"^[A-Z0-9\.]{1,44}$"

def check_dataset(name):
    if re.match(PATTERN, name):
        print(f"[green]{name} is valid[/green]")
    else:
        print(f"[red]{name} is invalid[/red]")

if __name__ == "__main__":
    check_dataset("USER.DATA.FILE")
    check_dataset("invalid-dataset-name")