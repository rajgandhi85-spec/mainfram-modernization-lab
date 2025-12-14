import re
from rich import print

def validate_jcl(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    errors = []
    for i, line in enumerate(lines, start=1):
        if not line.startswith("//"):
            errors.append(f"Line {i}: Missing // prefix")

    if errors:
        print("[red]Validation Failed[/red]")
        for e in errors:
            print(f"- {e}")
    else:
        print("[green]JCL Validation Passed[/green]")

if __name__ == "__main__":
    validate_jcl("jcl-templates\sample-job.jcl")