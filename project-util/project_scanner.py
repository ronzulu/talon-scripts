import os
import re
import yaml
from datetime import datetime

class ProjectScanner:
    def __init__(self):
        self.base_folder = r"C:\Obsidian\Obsidian\Projects"
        self.archive_folder = r"C:\Obsidian\Obsidian\Projects\_Archive"
        self.project_id_pattern = re.compile(r"^([A-Z]+)-(\d{3})")

    def scan_closed_projects(self):
        return self.scan_projects_with_status("Closed")

    def scan_projects_with_status(self, target_statuses):
        if isinstance(target_statuses, str):
            target_statuses = [target_statuses]
        elif target_statuses is None:
            raise ValueError("target_statuses must be specified.")


        result = []

        for group_name in os.listdir(self.base_folder):
            group_path = os.path.join(self.base_folder, group_name)
            if not os.path.isdir(group_path) or group_name.startswith("_"):
                continue  # Skip non-folders and archive/system folders

            for folder in os.listdir(group_path):
                folder_path = os.path.join(group_path, folder)
                if not os.path.isdir(folder_path):
                    continue

                match = self.project_id_pattern.match(folder)
                if not match:
                    continue

                project_id = match.group(0)
                md_file = self._find_markdown_file(folder_path)
                if not md_file:
                    continue

                status = self._extract_project_status(md_file)
                if status in target_statuses:
                    result.append((group_name, project_id))

        return result

    def _find_markdown_file(self, folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(".md"):
                return os.path.join(folder_path, file)
        return None

    def _extract_project_status(self, md_path):
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        match = re.match(r"(?s)^---\n(.*?)\n---\n", content)
        if not match:
            return None

        front_matter = yaml.safe_load(match.group(1)) or {}
        return front_matter.get("project-status")
