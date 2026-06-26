# This script creates a text file and writes sample data into it.
from pathlib import Path

file_path = Path(__file__).with_name("sample_data.txt")

with file_path.open("w", encoding="utf-8") as file:
    file.write("Hello from Practice 6\n")
    file.write("This is sample data.\n")

print("File created and written successfully.")

# Expected output:
# File created and written successfully.
