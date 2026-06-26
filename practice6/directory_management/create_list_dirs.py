# This script creates nested directories, lists their contents, and finds files by extension.
from pathlib import Path

base_dir = Path(__file__).resolve().parent / "nested_project"
sub_dir = base_dir / "src" / "utils"
sub_dir.mkdir(parents=True, exist_ok=True)

print("Nested directories created.")

# List files and folders inside the created directories.
print("Contents of base directory:")
for item in base_dir.rglob("*"):
    print(item.name)

# Find files by extension.
py_files = [path.name for path in base_dir.rglob("*.py")]
print("Python files:", py_files)

# Expected output:
# Nested directories created.
# Contents of base directory:
# nested_project
# src
# utils
# Python files: []
