import os
import sys
import argparse

from rich.console import Console

from .utils.tree import create_tree
from .utils.file_handler import read_file, copy_to_clipboard

console = Console()


def main():
    parser = argparse.ArgumentParser(description="ScriptMonkey - Copy files and directory trees to clipboard")
    parser.add_argument("--files", nargs="*", help="Paths to files to copy to clipboard", type=str)
    parser.add_argument("--tree", help="Include directory tree in clipboard", action="store_true")
    args = parser.parse_args()

    print(f"\n🐒 ScriptMonkey - File & Tree Clipboard Utility\n")

    # Check if any valid arguments were provided
    if not args.files and not args.tree:
        console.print("[bold red]❌ Please specify --files, --tree, or both.[/bold red]")
        parser.print_help()
        return

    # Handle the clipboard functionality
    file_paths = args.files if args.files else []
    include_tree = args.tree

    # Validate that files exist if provided
    if file_paths:
        for file_path in file_paths:
            if not os.path.exists(file_path):
                console.print(f"[bold red]❌ File not found: {file_path}[/bold red]")
                return

    copy_to_clipboard(file_paths, include_tree)


# Legacy function for backward compatibility (now does nothing)
def run():
    """Legacy function - no longer provides error handling."""
    pass
