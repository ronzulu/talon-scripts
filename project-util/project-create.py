import os
import re
from talon import Module

mod = Module()

class ProjectCreator:
    def __init__(self):
        self.filename = r"C:\temp\obsidian project create.txt"
        self.base_folder = r"C:\Obsidian\Obsidian\Projects"

    def extract_project_info(self):
        """Reads the input file and extracts group name and description."""
        with open(self.filename, "r", encoding="utf-8") as f:
            line = f.readline().strip()
            if "\t" not in line:
                raise ValueError("Input line must contain a tab separator.")
            group_name, description = line.split("\t", 1)
            return group_name.strip(), description.strip()

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
        """Determines the next available project ID for the group, formatted with leading zeros."""
        existing_ids = self.find_existing_project_ids(group_name)
        next_id = max(existing_ids, default=0) + 1
        formatted_id = f"{next_id:03d}"
        return f"{group_name}-{formatted_id}"

    def verify_group_folder_exists(self, group_name):
        """Checks that the group folder exists under the base folder."""
        group_folder_path = os.path.join(self.base_folder, group_name)
        if not os.path.isdir(group_folder_path):
            raise FileNotFoundError(f"Group folder '{group_name}' not found under base folder.")
        return group_folder_path

    def create_project_folder(self, group_folder_path, project_id, description):
        """Creates the project folder under the group folder."""
        folder_name = f"{project_id} {description}"
        project_path = os.path.join(group_folder_path, folder_name)
        os.makedirs(project_path, exist_ok=True)
        return project_path

    def create_markdown_file(self, project_path, description):
        """Creates a markdown file named after the project description."""
        safe_filename = re.sub(r'[\\/*?:"<>|]', "_", description)  # sanitize filename
        md_path = os.path.join(project_path, f"{safe_filename}.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# {description}\n\n")
            f.write("Project initialized.\n")
        return md_path

    def create_project(self):
        """Main method to extract info, validate, and generate project structure."""
        group_name, description = self.extract_project_info()
        project_id = self.generate_new_project_id(group_name)
        group_folder_path = self.verify_group_folder_exists(group_name)
        project_path = self.create_project_folder(group_folder_path, project_id, description)
        md_file_path = self.create_markdown_file(project_path, description)

        print(f"✅ Project ID: {project_id}")
        print(f"📁 Folder Created: {project_path}")
        print(f"📝 Markdown File: {md_file_path}")
        return project_id, description, project_path, md_file_path


@mod.action_class
class user_actions:
    def rz_update_talon_list():
        """Trigger project creation from Talon voice command."""
        creator = ProjectCreator()
        creator.create_project()

