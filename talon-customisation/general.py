import string
from talon import Module, actions
import time
import yaml
import glob

mod = Module()

@mod.action_class
class Actions:
    def my_custom_date_function():
        """My custom date function"""
        return time.strftime("%Y-%m-%d")

    def update_obsidian_medical_vault():
        """update_obsidian_medical_vault"""
        print(f"update_obsidian_medical_vault: Starting")
        updates = 0
        for file in glob.glob('C:/Obsidian/Medical/**/*.md', recursive=True):
            if actions.user.copy_frontmatter(file):
                updates += 1
                if updates > 10:
                    return

    def copy_frontmatter(path: str):
        """copy_frontmatter"""
        # print(f"File: {path}")
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        if not text.startswith("---"):
            return False
    
        _, fm_text, body = text.split("---", 2)
        fm = yaml.safe_load(fm_text)

        update_made = actions.user.rationalize_status_properties(path, fm)
        if update_made:
            new_text = "---\n" + yaml.dump(fm) + "---" + body
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_text)
            
        return update_made

    def rationalize_date_properties(path: str, fm: dict):
        """rationalize_date_properties"""

        apt_date = fm.get("apt-date")
        procedure_date = fm.get("procedure-date")
        test_date = fm.get("test-date")
        date = fm.get("date")
        count = 0

        if apt_date: count += 1
        if procedure_date: count += 1
        if test_date: count += 1

        if apt_date == None and procedure_date == None and test_date == None:
            return False
        if date:
            print(f"❌ File: {path}, date already has a value")
            return False
        if count > 1:
            print(f"❌ File: {path}, count of date values: {count}")
            return False
        print(f"File: {path}, date: {date}, apt-date: {apt_date}, procedure-date: {procedure_date}, test-date: {test_date}")

        if apt_date:
            fm["date"] = str(fm["apt-date"])
            fm["item-type"] = "appointment"
            del fm["apt-date"]

        if procedure_date:
            fm["date"] = str(fm["procedure-date"])
            fm["item-type"] = "procedure"
            del fm["procedure-date"]

        if test_date:
            fm["date"] = str(fm["test-date"])
            fm["item-type"] = "test"
            del fm["test-date"]
            
        return True

    def rationalize_associated_item_properties(path: str, fm: dict):
        """rationalize_associated_item_properties"""
        # print(f"rationalize_associated_item_properties: {path}")

        test_ordered_for = fm.get("test-ordered-for")
        illness = fm.get("illness")
        procedure_for = fm.get("procedure-for")
        item_for = fm.get("item-for")
        count = 0

        if test_ordered_for: count += 1
        if illness: count += 1
        if procedure_for: count += 1

        if test_ordered_for == None and illness == None and procedure_for == None:
            return False
        if item_for:
            print(f"❌ File: {path}, item_for already has a value")
            return False
        if count > 1:
            print(f"❌ File: {path}, count of item_for values: {count}")
            return False
        print(f"File: {path}, test-ordered-for: {test_ordered_for}, illness: {illness}, procedure-for: {procedure_for}, item-for: {item_for}")

        if test_ordered_for:
            fm["item-for"] = str(test_ordered_for)
            del fm["test-ordered-for"]

        if illness:
            fm["item-for"] = str(illness)
            del fm["illness"]

        if procedure_for:
            fm["item-for"] = str(procedure_for)
            del fm["procedure-for"]
            
        return True

    def rationalize_status_properties(path: str, fm: dict):
        """rationalize_status_properties"""
        # print(f"rationalize_associated_item_properties: {path}")

        apt_status = fm.get("apt-status")
        procedure_status = fm.get("procedure-status")
        item_status = fm.get("item-status")
        count = 0

        if apt_status: count += 1
        if procedure_status: count += 1
        if item_status: count += 1

        if apt_status == None and procedure_status == None:
            return False
        if item_status:
            print(f"❌ File: {path}, item_status already has a value")
            return False
        if count > 1:
            print(f"❌ File: {path}, count of item_status values: {count}")
            return False
        print(f"File: {path}, apt-status: {apt_status}, procedure-status: {procedure_status}, item-status: {item_status}")

        if apt_status:
            fm["item-status"] = str(apt_status)
            del fm["apt-status"]

        if procedure_status:
            fm["item-status"] = str(procedure_status)
            del fm["procedure-status"]
            
        return True
