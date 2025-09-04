import os
import logging

# Configure logging for auditability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Hardcoded base directory
BASE_DIR = r"C:\Obsidian\Obsidian\Projects\SEGGY"

def rename_seg_folders(base_dir: str):
    """
    Renames folders starting with 'SEG-0' to 'SEGGY-0' within the given base directory.
    """
    if not os.path.isdir(base_dir):
        logging.error(f"Provided base directory does not exist: {base_dir}")
        return

    for entry in os.listdir(base_dir):
        full_path = os.path.join(base_dir, entry)

        if os.path.isdir(full_path) and entry.startswith("SEG-0"):
            new_name = entry.replace("SEG-0", "SEGGY-0", 1)
            new_path = os.path.join(base_dir, new_name)

            try:
                os.rename(full_path, new_path)
                logging.info(f"Renamed: {entry} → {new_name}")
            except OSError as e:
                logging.error(f"Failed to rename {entry}: {e}")

if __name__ == "__main__":
    rename_seg_folders(BASE_DIR)