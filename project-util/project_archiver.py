import os
import shutil
import yaml
from datetime import datetime
from .project_scanner import ProjectScanner
from .project_core import ProjectCore
from talon import Module

mod = Module()

class ProjectArchiver:
    def __init__(self):
        self.core = ProjectCore()
        self.log_path = os.path.join(self.core.obsidian_temp_folder, "obsidian_archive_log.txt")

    def archive_project(self, group_name, project_id):
        # Locate project folder
        project_folder = self.core.find_group_project_folder(group_name, project_id)

        # Locate markdown file
        md_file = self.core.find_markdown_file(project_folder)

        # Update front matter
        self.update_front_matter(md_file)

        # Move folder to archive
        group_folder = os.path.join(self.core.project_completed_folder, group_name)
        os.makedirs(group_folder, exist_ok=True)
        archived_path = os.path.join(group_folder, os.path.basename(project_folder))
        shutil.move(project_folder, archived_path)

        # Log action
        with open(self.log_path, "a", encoding="utf-8") as log:
            log.write(f"[{datetime.now()}] Archived {project_id} → {archived_path}\n")

        print(f"📦 Archived: {project_id}")

    def update_front_matter(self, md_file):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        match = yaml_front_matter(content)
        if not match:
            raise ValueError("Markdown file does not contain valid front matter.")

        front_matter_raw, body = match
        front_matter = yaml.safe_load(front_matter_raw) or {}
        front_matter["project-date-archived"] = datetime.today().strftime("%Y-%m-%d")

        updated_front_matter = yaml.dump(front_matter, sort_keys=False).strip()
        updated_md = f"---\n{updated_front_matter}\n---\n{body}"

        with open(md_file, "w", encoding="utf-8") as f:
            f.write(updated_md)

def yaml_front_matter(content):
    import re
    match = re.match(r"(?s)^---\n(.*?)\n---\n(.*)", content)
    return match.groups() if match else None


""" # Example usage
scanner = ProjectScanner()
closed = scanner.scan_closed_projects()
archiver = ProjectArchiver()

print("📋 Closed Projects:")
for group, project_id in closed:
    print(f"🔹 {group} → {project_id}")
    archiver.archive_project(group, project_id) """


@mod.action_class
class user_actions:
    def obsidian_archive_closed_projects():
        """Trigger project creation from Talon voice command."""
        scanner = ProjectScanner()
        closed = scanner.scan_closed_projects()
        archiver = ProjectArchiver()
        for group, project_id in closed:
            # print(f"🔹 {group} → {project_id}")
            archiver.archive_project(group, project_id)
