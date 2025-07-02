import os

import pyperclip
from rich.console import Console

from .tree import create_tree


console = Console()


def copy_to_clipboard(file_paths, include_tree=False):
    """
    Reads content from specified files and/or directory tree and copies to clipboard.
    Also prints the output to terminal.
    """
    if not file_paths and not include_tree:
        console.print("[bold red]❌ No files or tree specified to copy.[/bold red]")
        return

    formatted_output = ""

    # Handle files if provided
    if file_paths:
        formatted_output += "- - - - - - - - - -\nHere are some details about the project.\n\n"

        for path in file_paths:
            try:
                content = read_file(path)
                formatted_output += f"# {path}\n{content}\n\n- - - - - - - - - -\n\n"
            except FileNotFoundError:
                console.print(f"[bold yellow]Warning: {path} not found. Skipping this file.[/bold yellow]")
            except Exception as e:
                console.print(f"[bold red]Error reading {path}: {e}[/bold red]")

    # Include the directory tree if requested
    if include_tree:
        start_directory = os.getcwd()
        dir_name = os.path.basename(start_directory)
        tree = create_tree(start_directory)
        if file_paths:
            formatted_output += "# PROJECT TREE\n"
        formatted_output += f"{dir_name}\n{tree}"

    # Copy the formatted output to the clipboard and print to terminal
    if formatted_output:
        pyperclip.copy(formatted_output.strip())

        # Print the output to terminal
        print(formatted_output.strip())
        print()  # Add some spacing

        # Show what was copied
        if file_paths and include_tree:
            console.print(f"[green]🐒 Copied {len(file_paths)} file(s) and directory tree to clipboard.[/green]")
        elif file_paths:
            console.print(f"[green]🐒 Copied {len(file_paths)} file(s) to clipboard.[/green]")
        elif include_tree:
            console.print("[green]🐒 Copied directory tree to clipboard.[/green]")
    else:
        console.print("[bold red]❌ Nothing to copy.[/bold red]")


def read_file(path: str) -> str:
    """Loads a file and returns the content.

    Args:
        path (str): Path to the file

    Returns:
        str: The content of the file
    """
    with open(path, "r") as file:
        return file.read()


def write_file(path: str, content: str) -> None:
    """Writes string content to a file.

    Args:
        path (str): Path to the file.
        content (str): Content to write to file.
    """
    with open(path, "w") as file:
        file.write(content)
