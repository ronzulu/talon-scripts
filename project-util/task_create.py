import os
import re
import yaml
from datetime import datetime
from talon import Module
from .project_core import ProjectCore

mod = Module()

class TaskCreator:
    def __init__(self):
        self.core = ProjectCore()
        self.filename = os.path.join(self.core.obsidian_temp_folder, "obsidian task create.txt")
        self.template_path = os.path.join(self.core.template_folder, "Task.md")

    def extract_task_info(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            line = f.readline().strip()
            if "\t" not in line:
                raise ValueError("Input line must contain a tab separator.")
            project_id, task_description = line.split("\t", 1)
            return project_id.strip(), task_description.strip()

    def find_existing_task_ids(self, project_folder):
        task_ids = []
        for root, _, files in os.walk(project_folder):
            for file in files:
                if file.endswith(".md"):
                    path = os.path.join(root, file)
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                        match = re.match(r"(?s)^---\n(.*?)\n---", content)
                        if match:
                            front_matter = yaml.safe_load(match.group(1))
                            if isinstance(front_matter, dict) and "task-id" in front_matter:
                                try:
                                    task_ids.append(int(front_matter["task-id"]))
                                except ValueError:
                                    continue
        return task_ids

    def load_template(self):
        with open(self.template_path, "r", encoding="utf-8") as f:
            return f.read()

    def populate_template(self, template, project_id, task_id):
        today = datetime.today().strftime("%Y-%m-%d")

        front_matter_match = re.match(r"(?s)^---\n(.*?)\n---\n(.*)", template)
        if not front_matter_match:
            raise ValueError("Template does not contain valid front matter.")

        front_matter_raw, body = front_matter_match.groups()
        front_matter = yaml.safe_load(front_matter_raw) or {}

        front_matter["project-id"] = project_id
        front_matter["task-id"] = task_id
        front_matter["task-status"] = "Open"
        front_matter["task-open-date"] = today

        updated_front_matter = yaml.dump(front_matter, sort_keys=False).strip()
        return f"---\n{updated_front_matter}\n---\n{body}"

    def create_task_file(self, project_folder, task_description, project_id, task_id):
        task_folder = os.path.join(project_folder, "Tasks")
        os.makedirs(task_folder, exist_ok=True)

        safe_filename = re.sub(r'[\\/*?:"<>|]', "_", task_description)
        md_path = os.path.join(task_folder, f"{safe_filename}.md")

        template = self.load_template()
        populated = self.populate_template(template, project_id, task_id)

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(populated)

        return md_path

    def create_task(self):
        project_id, task_description = self.extract_task_info()
        project_folder = self.core.find_project_folder(project_id)
        existing_ids = self.find_existing_task_ids(project_folder)
        next_task_id = max(existing_ids, default=0) + 1
        md_file_path = self.create_task_file(project_folder, task_description, project_id, next_task_id)

        print(f"🆕 Task Created: {md_file_path}")
        print(f"🔢 Task ID: {next_task_id}")
        return project_id, task_description, md_file_path, next_task_id


@mod.action_class
class user_actions:
    def obsidian_task_create():
        """Trigger task creation from Talon voice command."""
        creator = TaskCreator()
        creator.create_task()