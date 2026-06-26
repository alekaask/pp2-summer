# This script moves and copies files between directories.
from pathlib import Path
import shutil

source_dir = Path(__file__).resolve().parent
source_file = source_dir / "create_list_dirs.py"

# Create a destination folder.
destination_dir = source_dir / "backup_folder"
destination_dir.mkdir(exist_ok=True)

# Copy the file to the destination.
shutil.copy(source_file, destination_dir / "create_list_dirs.py")
print("File copied to backup folder.")

# Move another file into the destination.
move_target = destination_dir / "move_files.py"
Path(__file__).resolve().rename(move_target)
print("File moved to backup folder.")

# Expected output:
# File copied to backup folder.
# File moved to backup folder.
