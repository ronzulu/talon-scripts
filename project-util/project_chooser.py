from datetime import datetime
from .project_scanner import ProjectScanner
from talon import Module, app
import random

mod = Module()

@mod.action_class
class user_actions:
    def obsidian_choose_random_open_project():
        """Trigger project creation from Talon voice command."""
        scanner = ProjectScanner()
        open_project_list = scanner.scan_projects_with_status("Open")
        random_choice = random.choice(open_project_list)
        print(f"✅ Open project list: {open_project_list}")
        print(f"✅ Random project: {random_choice}")
        app.notify(title="Your next mission", body=random_choice[1])

