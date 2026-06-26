# This script appends content, copies the file to a backup, and safely deletes it.
import shutil
from pathlib import Path

file_path = Path(__file__).with_name("sample_data.txt")
backup_path = Path(__file__).with_name("sample_data_backup.txt")

# Append new lines and verify the updated content.
with file_path.open("a", encoding="utf-8") as file:
    file.write("Appended line 1\n")
    file.write("Appended line 2\n")

print("Appended lines successfully.")

# Copy the file to a backup location using shutil.
shutil.copyfile(file_path, backup_path)
print("Backup created.")

# Delete the backup safely.
if backup_path.exists():
    backup_path.unlink()
    print("Backup deleted.")

# Expected output:
# Appended lines successfully.
# Backup created.
# Backup deleted.
