import os

# SHALLOW DIRECTORIES (Non-Recursive Scan)
# These directories are shown but their contents are not scanned
SHALLOW_DIRS = {
    "node_modules",
    ".git",
    "build",
    "dist",
    "vendor",
    "__pycache__",
    "venv",
    ".venv",
    ".bundle",
    "DerivedData",
    "site",
    "assets",
    "img",
    "fonts",
    ".cache",
    # Vendored dependency rules
    "deps",
    "google",
    "pyasn1_modules",
    "babel",
    "espeak-ng-data",
    "templates",
    "migrations",
    "lib",
    "meta",
    # Model directory rules
    "embedding_models",
    "imagegen_models",
    "textgen_models",
    "tts_models",
    "whisper_models",
    # Test directory rules
    "test",
    "tests",
    "__tests__",
    # Project-specific config/output rules
    ".erb",
    ".vscode",
    ".github",
    "release",
    # Rust-specific rules
    "debug",
    "incremental",
}

# FULL EXCLUSION (Completely Hidden)
# These files/directories are completely hidden from the tree
EXCLUDE_PATTERNS = [
    ".DS_Store",
    "*.log",
    "*.swp",
    "*.swo",
    "*~",
    "#*#",
    "*.pyc",
    "*.class",
    "*.o",
    "*.dylib",
    "*.so",
    "*.dll",
    "*.a",
    ".eslintcache",
    ".prettiercache",
    "Thumbs.db",
    ".gitkeep",
    "*.ico",
    "*.icns",
    "*.patch",
    "*.metadata",
    "sitemap.xml",
    "sitemap.xml.gz",
    "*.gguf.lock",
    "CACHEDIR.TAG",
    # Generated & vendor file rules
    "*_pb2.py",
    "*_pb2.pyi",
    "cacerts.txt",
    "*.dat",
    "*_dict",
]

# RUST RELEASE EXCLUSION (For target/release)
# These items are hidden within the 'release' directory
RELEASE_EXCLUDE_PATTERNS = {
    ".cargo-lock",
    ".fingerprint",
    "build",
    "deps",
    "examples",
    "incremental",
}


def create_tree(start_path, prefix="", max_depth=None, current_depth=0):
    """
    Generates a directory tree as a string with intelligent filtering for source code projects.
    Mimics the codetree bash script behavior with shallow directories, exclusions, and special handling.
    """
    # If max_depth is defined and the current depth exceeds it, stop recursion
    if max_depth is not None and current_depth > max_depth:
        return ""

    tree = ""

    try:
        all_items = sorted(os.listdir(start_path))
    except (OSError, PermissionError):
        return ""

    # Filter out excluded items
    items_to_process = []
    for item in all_items:
        if not is_excluded(item):
            items_to_process.append(item)

    count = len(items_to_process)

    for i, item in enumerate(items_to_process):
        full_path = os.path.join(start_path, item)
        connector = "└── " if i == count - 1 else "├── "
        next_prefix = prefix + ("    " if i == count - 1 else "│   ")

        if os.path.isdir(full_path):
            # Special handling for Rust target directory
            if item == "target":
                tree += prefix + connector + item + "\n"
                tree += handle_target_directory(full_path, next_prefix)
            elif is_shallow(item):
                tree += prefix + connector + item + "/ [...]" + "\n"
            else:
                tree += prefix + connector + item + "\n"
                tree += create_tree(
                    full_path,
                    next_prefix,
                    max_depth=max_depth,
                    current_depth=current_depth + 1,
                )
        else:
            tree += prefix + connector + item + "\n"

    return tree


def handle_target_directory(target_path, prefix):
    """Special handling for Rust target directories"""
    tree = ""
    release_path = os.path.join(target_path, "release")
    debug_path = os.path.join(target_path, "debug")

    sub_items = []
    if os.path.isdir(release_path):
        sub_items.append("release")
    if os.path.isdir(debug_path):
        sub_items.append("debug")

    sub_count = len(sub_items)
    j = 0

    if os.path.isdir(release_path):
        j += 1
        release_connector = "└── " if j == sub_count else "├── "
        release_next_prefix = prefix + ("    " if j == sub_count else "│   ")
        tree += prefix + release_connector + "release" + "\n"

        # Filter release directory contents
        try:
            release_contents = sorted(os.listdir(release_path))
            release_filtered = []
            for r_item in release_contents:
                if not is_release_excluded(r_item):
                    release_filtered.append(r_item)

            r_count = len(release_filtered)
            for k, r_item in enumerate(release_filtered):
                r_item_path = os.path.join(release_path, r_item)
                r_connector = "└── " if k == r_count - 1 else "├── "

                display_name = r_item
                if os.path.isdir(r_item_path):
                    display_name += "/ [...]"
                tree += release_next_prefix + r_connector + display_name + "\n"
        except (OSError, PermissionError):
            pass

    if os.path.isdir(debug_path):
        j += 1
        debug_connector = "└── " if j == sub_count else "├── "
        tree += prefix + debug_connector + "debug/ [...]" + "\n"

    return tree


def is_shallow(dir_name):
    """Check if directory should be shown as shallow (contents not scanned)"""
    if dir_name in SHALLOW_DIRS:
        return True

    # Check for wildcard patterns
    if dir_name.endswith(".egg-info"):
        return True
    if dir_name.endswith(".dist-info"):
        return True

    return False


def is_excluded(item_name):
    """Check if item should be completely excluded"""
    for pattern in EXCLUDE_PATTERNS:
        if pattern.startswith("*") and pattern.endswith("*"):
            # Contains pattern
            if pattern[1:-1] in item_name:
                return True
        elif pattern.startswith("*"):
            # Ends with pattern
            if item_name.endswith(pattern[1:]):
                return True
        elif pattern.endswith("*"):
            # Starts with pattern
            if item_name.startswith(pattern[:-1]):
                return True
        else:
            # Exact match
            if item_name == pattern:
                return True
    return False


def is_release_excluded(item_name):
    """Check if item should be excluded from target/release directory"""
    return item_name in RELEASE_EXCLUDE_PATTERNS
