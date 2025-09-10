import os
import re
import yaml
from datetime import datetime
from .project_core import ProjectCore
from talon import Module

mod = Module()

class ProjectCreator:
    def __init__(self):
        self.core = ProjectCore()
        self.filename = os.path.join(self.core.obsidian_temp_folder, "obsidian project create.txt")
        self.template_path = os.path.join(self.core.template_folder, "Project.md")

    def extract_project_info(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            line = f.readline().strip()
            if "\t" not in line:
                raise ValueError("Input line must contain a tab separator.")
            group_name, description = line.split("\t", 1)
            return group_name.strip(), description.strip()

    def create_project_folder(self, group_folder_path, project_id, description):
        folder_name = f"{project_id} {description}"
        project_path = os.path.join(group_folder_path, folder_name)
        os.makedirs(project_path, exist_ok=True)
        files_path = os.path.join(project_path, "files")
        os.makedirs(files_path, exist_ok=True)

        return project_path

    def load_template(self):
        with open(self.template_path, "r", encoding="utf-8") as f:
            return f.read()

    def populate_template(self, template, project_id, group_name):
        project_class = self.core.project_class_map.get(group_name, group_name)
        today = datetime.today().strftime("%Y-%m-%d")

        # Extract front matter block
        front_matter_match = re.match(r"(?s)^---\n(.*?)\n---\n(.*)", template)
        if not front_matter_match:
            raise ValueError("Template does not contain valid front matter.")

        front_matter_raw, body = front_matter_match.groups()
        front_matter = yaml.safe_load(front_matter_raw) or {}

        # Update specified attributes
        front_matter["project-id"] = project_id
        front_matter["project-class"] = project_class
        front_matter["project-date-opened"] = today
        front_matter["project-status"] = "Open"

        # Reconstruct front matter block
        updated_front_matter = yaml.dump(front_matter, sort_keys=False).strip()
        updated_template = f"---\n{updated_front_matter}\n---\n{body}"
        
        updated_template = updated_template.replace("PROJECT_MARKER", project_id)

        return updated_template

    def create_markdown_file(self, project_path, description, project_id, group_name):
        safe_filename = re.sub(r'[\\/*?:"<>|]', "_", description)
        md_path = os.path.join(project_path, f"{safe_filename}.md")

        template = self.load_template()
        populated = self.populate_template(template, project_id, group_name)

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(populated)

        return md_path

    def create_project(self):
        group_name, description = self.extract_project_info()
        project_id = self.core.generate_new_project_id(group_name)
        group_folder_path = self.core.verify_group_folder_exists(group_name)
        project_path = self.create_project_folder(group_folder_path, project_id, description)
        md_file_path = self.create_markdown_file(project_path, description, project_id, group_name)

        print(f"✅ Project ID: {project_id}")
        print(f"📁 Folder Created: {project_path}")
        print(f"📝 Markdown File: {md_file_path}")
        return project_id, description, project_path, md_file_path


@mod.action_class
class user_actions:
    def obsidian_project_create():
        """Trigger project creation from Talon voice command."""
        creator = ProjectCreator()
        creator.create_project()
