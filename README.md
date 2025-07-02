# ScriptMonkey 🐒

ScriptMonkey is a simple CLI utility that helps developers quickly copy files and directory structures to their clipboard in a formatted way. Perfect for sharing code context with LLMs, creating documentation, or getting help with your projects.

## Features
- **File Copying**: Copy one or multiple files to clipboard with clean formatting
- **Directory Tree**: Generate and copy directory structure to clipboard  
- **Combined Output**: Copy both files and directory tree together
- **Smart Filtering**: Intelligent directory tree that filters out build artifacts, dependencies, and other non-essential files
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Installation

To install ScriptMonkey, simply run:

```bash
pip install scriptmonkey
```

## Usage

### Copy Files to Clipboard

Copy one or more files to your clipboard with clean formatting:

```bash
scriptmonkey --files path/to/file1.py path/to/file2.js
```

The files will be copied to your clipboard in this format:
```
- - - - - - - - - -
Here are some details about the project.

# path/to/file1.py
<content from file1.py>

- - - - - - - - - -

# path/to/file2.js
<content from file2.js>

- - - - - - - - - -
```

### Copy Directory Tree to Clipboard

Generate and copy a clean directory tree structure:

```bash
scriptmonkey --tree
```

This creates an intelligent directory tree that:
- Filters out build artifacts (`node_modules`, `__pycache__`, `.git`, etc.)
- Excludes temporary files (`*.log`, `*.pyc`, `.DS_Store`, etc.)
- Shows important directories as shallow entries (`vendor/`, `build/ [...]`)
- Provides special handling for Rust `target` directories

### Copy Both Files and Tree

Combine file contents with directory structure:

```bash
scriptmonkey --files src/main.py src/utils.py --tree
```

This copies both the specified files and the directory tree to your clipboard, giving you complete context for sharing with LLMs or documentation.

## Smart Directory Filtering

ScriptMonkey uses intelligent filtering to show you only the important parts of your project:

**Shallow Directories** (shown but contents hidden):
- `node_modules`, `.git`, `build`, `dist`
- `__pycache__`, `.venv`, `vendor`
- `test`, `tests`, `assets`, `img`

**Excluded Files** (completely hidden):
- `*.log`, `*.pyc`, `*.swp`, `.DS_Store`
- `*.class`, `*.o`, `*.dll`, `*.so`
- Build artifacts and temporary files

**Special Handling**:
- Rust `target/release` directories show filtered contents
- Model directories are treated as shallow
- Test directories are marked but not expanded

## Use Cases

- **LLM Assistance**: Quickly share your code context with ChatGPT, Claude, or other AI assistants
- **Code Reviews**: Copy relevant files for review discussions  
- **Documentation**: Generate clean file listings for documentation
- **Project Sharing**: Share project structure and key files with teammates
- **Debugging Help**: Include relevant code and project structure when asking for help

## Requirements
- Python 3.6 or later
- Cross-platform clipboard support (automatic)

## Examples

**Copy a single Python file:**
```bash
scriptmonkey --files main.py
```

**Copy multiple configuration files:**
```bash  
scriptmonkey --files config.json requirements.txt .env.example
```

**Just the directory tree:**
```bash
scriptmonkey --tree
```

**Everything together:**
```bash
scriptmonkey --files src/*.py --tree
```

## Legacy Compatibility

For users upgrading from ScriptMonkey 1.x: The `scriptmonkey.run()` function is still available but no longer provides error handling functionality. It exists only for backward compatibility and does nothing.

---

**Version 2.0.0** - Simplified for focus and reliability. No more AI dependencies, just pure clipboard utility goodness! 🐒
