from io import TextIOWrapper
import os
from typing import Tuple
from talon import Context, Module, actions, app, fs, imgui, ui

mod = Module()

class tag_hierarchy_calculator:

    @staticmethod
    def get_descendant_tag_list(tag: str, tag_to_child_tag_dict: dict[str, list[str]]) -> list[str]:
        """Print out a sheet of talon commands"""

        result = []
        if tag in tag_to_child_tag_dict:
            child_tag_list = tag_to_child_tag_dict[tag]
            result.extend(child_tag_list)
            for child_tag in child_tag_list:
                result.extend(tag_hierarchy_calculator.get_descendant_tag_list(child_tag, tag_to_child_tag_dict))

        return result

    @staticmethod
    def analyze_all_talon_community() -> tuple[dict[str, list[str]], dict[str, list[str]]]:
        """Print out a sheet of talon commands"""

        app_to_child_tag_dict = dict()
        tag_to_child_tag_dict = dict()

        file_list = tag_hierarchy_calculator.generate_talon_file_list()
        for filename in file_list:
            app_list, extra_match_list, tag_list, child_tag_list = tag_hierarchy_calculator.analyze_file(filename)
            for app in app_list:
                app_str = app
                if app_str and len(extra_match_list) > 0:
                    app_str += f" ({';'.join(extra_match_list)})"
                app_to_child_tag_dict[app_str] = child_tag_list
            for tag in tag_list:
                tag_to_child_tag_dict[tag] = child_tag_list

        return [app_to_child_tag_dict, tag_to_child_tag_dict]

    @staticmethod
    def determine_command_group_list(app_to_child_tag_dict, tag_to_child_tag_dict) -> list[str]:
        """Print out a sheet of talon commands"""

        print(f"determine_command_group_list: {app_to_child_tag_dict}, {tag_to_child_tag_dict}")
        s = set()
        for command_group_list in app_to_child_tag_dict.items():
            print(f"name1A: {type(command_group_list)} {command_group_list}")
            for name in command_group_list:
                print(f"name1B: {type(name)} {name}")
                s.update(name)
        for command_group_list in tag_to_child_tag_dict.items():
            print(f"name2A: {type(command_group_list)} {command_group_list}")
            for name in command_group_list:
                print(f"name2B: {type(name)} {name}")
                s.update(name)

        print(f"s: {s}")
        result = list(s).sort()
        print(f"result: {result}")
        return result

    @staticmethod
    def analyze_file(filename: str) -> Tuple[list[str], list[str], list[str], list[str]]:
        """This function is a test."""
        app_list = []
        extra_match_list = []
        tag_list = []
        child_tag_list = []
        in_frontmatter = True

        file = open(filename, "r") 
        while True:
            line = file.readline()
            if not line:
                break
            if in_frontmatter:
                if line.startswith("-"):
                    in_frontmatter = False
                else:
                    bits = line.split()
                    if len(bits) == 2 and bits[0].endswith(":") and len(bits[0]) > 1:
                        name = bits[0][:-1]
                        v = bits[1]
                        if name == "app":
                            app_list.append(v)
                        elif name == "tag":
                            if len(app_list) > 0:
                                raise Exception(f'app_list[0]: {app_list[0]}, line: {line}')
                            tag_list.append(v)
                        elif not line.startswith("#"):
                            extra_match_list.append(line.strip())

            else:
                bits = line.split()
                if len(bits) == 2 and bits[0] == "tag():" and len(bits[1]) > 1:
                    child_tag_list.append(bits[1])

        file.close()
        return [app_list, extra_match_list, tag_list, child_tag_list]
            
    @staticmethod
    def generate_talon_file_list():
        """This function is a test."""
        result = []
        w = os.walk(r'C:\Users\ronny\AppData\Roaming\talon\user\talon-community')
        for (dirpath, dirnames, filenames) in w:
            for filename in filenames:
                f, file_extension = os.path.splitext(filename)
                if file_extension == '.talon':
                    result.append(f"{dirpath}\\{filename}")
        
        return result

@mod.action_class
class user_actions:
    def tag_hierarchy_lister():
        """Print out a sheet of talon commands"""
        #open file
        app_to_child_tag_dict, tag_to_child_tag_dict = tag_hierarchy_calculator.analyze_all_talon_community()

        this_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(this_dir, 'tag-hierarchy-list.md')
        file = open(file_path,"w") 

        file.write(f"# Command group list\n\n")
        file.write("| Command Groups |")
        file.write("| -------------- |")
        command_group_list = tag_hierarchy_calculator.determine_command_group_list(app_to_child_tag_dict, tag_to_child_tag_dict)
        for command_group_name in command_group_list:
            file.write(f"| {command_group_name} |\n")


        file.write(f"# Application to command group list\n\n")
        file.write("| Application               | Command Groups |")
        file.write("| ------------------------- | -------------- |")

        for app, child_tag_list in app_to_child_tag_dict.items():
            list = child_tag_list
            for tag in child_tag_list:
                list.extend(tag_hierarchy_calculator.get_descendant_tag_list(tag, tag_to_child_tag_dict))
            
            file.write(f"| {app} | {user_actions.format_child_tag_list(list)} |\n")

        file.close()

    @staticmethod
    def format_child_tag_list(list: list[str]) -> str:
        """Print out a sheet of talon commands"""
        formatted_list = []
        for str in list:
            command_group = str.replace("'", "").replace("user.", "")
            formatted = f"[{command_group}](./Command%20Groups/{command_group}.md)"
            formatted_list.append(formatted)
        return ", ".join(formatted_list)
