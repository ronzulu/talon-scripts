import os
import re
import yaml
from datetime import datetime

class ProjectCore:
    def __init__(self):
        self.obsidian_folder = r"C:\Obsidian\Obsidian"
        self.base_folder = os.path.join(self.obsidian_folder, "Projects")
        self.project_completed_folder = os.path.join(self.base_folder, "{Complete}")
        self.template_folder = os.path.join(self.obsidian_folder, "My Stuff\Obsidian\Templates")
        self.obsidian_temp_folder = r"C:\temp\Obsidian"
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

    def find_group_project_folder(self, group_name, project_id):
        # Locate project folder
        group_path = os.path.join(self.base_folder, group_name)
        if not os.path.isdir(group_path):
            raise FileNotFoundError(f"Group folder '{group_name}' not found.")

        project_folder = None
        for folder in os.listdir(group_path):
            if folder.startswith(project_id):
                project_folder = os.path.join(group_path, folder)
                break

        if not project_folder or not os.path.isdir(project_folder):
            raise FileNotFoundError(f"Project folder for ID '{project_id}' not found.")

        return project_folder

    def find_markdown_file(self, project_folder):
        # Locate markdown file
        md_file = None
        for file in os.listdir(project_folder):
            if file.endswith(".md"):
                md_file = os.path.join(project_folder, file)
                break

        if not md_file:
            raise FileNotFoundError("Markdown file not found in project folder.")

        return md_file

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
