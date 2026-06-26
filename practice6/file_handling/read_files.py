# This script reads and prints the contents of a text file.
from pathlib import Path

file_path = Path(__file__).with_name("sample_data.txt")

with file_path.open("r", encoding="utf-8") as file:
    content = file.read()

print(content)

# Expected output:
# Hello from Practice 6
# This is sample data.
