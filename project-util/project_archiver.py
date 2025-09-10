import os
import shutil
import yaml
from datetime import datetime
from .project_scanner import ProjectScanner
from .project_core import ProjectCore

class ProjectArchiver:
    def __init__(self):
        self.core = ProjectCore()
        self.archive_folder = r"C:\Obsidian\Obsidian\Projects\_Archive"
        self.log_path = os.path.join(self.core.obsidian_temp_folder, "obsidian_archive_log.txt")

    def archive_project(self, group_name, project_id):
        # Locate project folder
        group_path = os.path.join(self.core.base_folder, group_name)
        if not os.path.isdir(group_path):
            raise FileNotFoundError(f"Group folder '{group_name}' not found.")

        project_folder = None
        for folder in os.listdir(group_path):
            if folder.startswith(project_id):
                project_folder = os.path.join(group_path, folder)
                break

        if not project_folder or not os.path.isdir(project_folder):
            raise FileNotFoundError(f"Project folder for ID '{project_id}' not found.")

        # Locate markdown file
        md_file = None
        for file in os.listdir(project_folder):
            if file.endswith(".md"):
                md_file = os.path.join(project_folder, file)
                break

        if not md_file:
            raise FileNotFoundError("Markdown file not found in project folder.")

        # Update front matter
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        match = yaml_front_matter(content)
        if not match:
            raise ValueError("Markdown file does not contain valid front matter.")

        front_matter_raw, body = match
        front_matter = yaml.safe_load(front_matter_raw) or {}
        front_matter["project-status"] = "Archived"
        front_matter["project-date-archived"] = datetime.today().strftime("%Y-%m-%d")

        updated_front_matter = yaml.dump(front_matter, sort_keys=False).strip()
        updated_md = f"---\n{updated_front_matter}\n---\n{body}"

        with open(md_file, "w", encoding="utf-8") as f:
            f.write(updated_md)

        # Move folder to archive
        os.makedirs(self.archive_folder, exist_ok=True)
        archived_path = os.path.join(self.archive_folder, os.path.basename(project_folder))
        shutil.move(project_folder, archived_path)

        # Log action
        with open(self.log_path, "a", encoding="utf-8") as log:
            log.write(f"[{datetime.now()}] Archived {project_id} → {archived_path}\n")

        print(f"📦 Archived: {project_id}")
        print(f"📝 Updated Markdown: {md_file}")
        print(f"📁 Moved to: {archived_path}")

def yaml_front_matter(content):
    import re
    match = re.match(r"(?s)^---\n(.*?)\n---\n(.*)", content)
    return match.groups() if match else None


# Example usage
scanner = ProjectScanner()
closed = scanner.scan_closed_projects()

print("📋 Closed Projects:")
for group, pid in closed:
    print(f"🔹 {group} → {pid}")    