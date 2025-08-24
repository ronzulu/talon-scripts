import os
import re
from talon import Module

mod = Module()

class ProjectCreator:
    def __init__(self):
        self.filename = r"C:\temp\obsidian project create.txt"  # Hardcoded input file
        self.base_folder = r"C:\Obsidian\Obsidian\Projects"  # Hardcoded base search directory

    def extract_project_info(self):
        """Reads the input file and extracts group name and description."""
        with open(self.filename, "r", encoding="utf-8") as f:
            line = f.readline().strip()
            if "\t" not in line:
                raise ValueError("Input line must contain a tab separator.")
            group_name, description = line.split("\t", 1)
            return group_name, description

    def find_existing_project_ids(self, group_name):
        """Recursively searches for folders starting with group_name- and extracts numeric suffixes."""
        pattern = re.compile(rf"^{re.escape(group_name)}-(\d+)")
        project_ids = []

        for root, dirs, _ in os.walk(self.base_folder):
            for folder in dirs:
                match = pattern.match(folder)
                if match:
                    project_ids.append(int(match.group(1)))

        return project_ids

    def generate_new_project_id(self, group_name):
        """Determines the next available project ID for the group."""
        existing_ids = self.find_existing_project_ids(group_name)
        next_id = max(existing_ids, default=0) + 1
        return f"{group_name}-{next_id}"

    def create_project(self):
        """Main method to extract info and generate new project ID."""
        group_name, description = self.extract_project_info()
        new_project_id = self.generate_new_project_id(group_name)
        print(f"New Project ID: {new_project_id}")
        print(f"Description: {description}")
        return new_project_id, description


@mod.action_class
class user_actions:

    def rz_update_talon_list():
        """Print out a sheet of talon commands"""
        project_creator = ProjectCreator()
        project_creator.create_project()
        