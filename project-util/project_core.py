import os
import re
import yaml
from datetime import datetime
from talon import Module

mod = Module()

class ProjectCore:
    def __init__(self):
        self.obsidian_folder = r"C:\Obsidian\Obsidian"
        self.base_folder = os.path.join(self.obsidian_folder, "Projects")
        self.template_folder = os.path.join(self.obsidian_folder, "My Stuff\Obsidian\Templates")
        self.project_class_map = {
            "TECH": "Technical",
            "FIN": "Finance",
            "ENV": "Environment",
            "SEGGY": "Segway"
        }

    def find_project_folder(self, project_id):
        group_name = project_id.split("-")[0]
        group_folder_path = os.path.join(self.base_folder, group_name)
        if not os.path.isdir(group_folder_path):
            raise FileNotFoundError(f"Group folder '{group_name}' not found.")

        for folder in os.listdir(group_folder_path):
            if folder.startswith(project_id):
                return os.path.join(group_folder_path, folder)

        raise FileNotFoundError(f"No folder found starting with '{project_id}' in '{group_folder_path}'.")

    def find_existing_project_ids(self, group_name):
        pattern = re.compile(rf"^{re.escape(group_name)}-(\d+)")
        project_ids = []

        for root, dirs, _ in os.walk(self.base_folder):
            for folder in dirs:
                match = pattern.match(folder)
                if match:
                    project_ids.append(int(match.group(1)))

        return project_ids

    def generate_new_project_id(self, group_name):
        existing_ids = self.find_existing_project_ids(group_name)
        next_id = max(existing_ids, default=0) + 1
        formatted_id = f"{next_id:03d}"
        return f"{group_name}-{formatted_id}"

    def verify_group_folder_exists(self, group_name):
        group_folder_path = os.path.join(self.base_folder, group_name)
        if not os.path.isdir(group_folder_path):
            raise FileNotFoundError(f"Group folder '{group_name}' not found under base folder.")
        return group_folder_path

    def create_project_folder(self, group_folder_path, project_id, description):
        folder_name = f"{project_id} {description}"
        project_path = os.path.join(group_folder_path, folder_name)
        os.makedirs(project_path, exist_ok=True)
        files_path = os.path.join(project_path, "files")
        os.makedirs(files_path, exist_ok=True)

        return project_path
