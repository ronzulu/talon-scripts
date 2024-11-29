from io import TextIOWrapper
import os
from typing import Tuple
from talon import Context, Module, actions, app, fs, imgui, ui

mod = Module()

@mod.action_class
class user_actions:
    def tag_hierarchy_lister():
        """Print out a sheet of talon commands"""
        #open file

        this_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(this_dir, 'tag-hierarchy-list.md')
        file = open(file_path,"w") 
        file.write(f"# hello Ronny\n\n")

        app_to_tag_dict = actions.user.analyze_all_talon_community()
        # file_list = actions.user.generate_talon_file_list()
        for app, child_tag_list in app_to_tag_dict.items():
            file.write(f"app: {app}, {child_tag_list}\n")

            # app_list, tag_list, child_tag_list = actions.user.analyze_file(filename)
            # for s in app_list:
            #     file.write(f"app: {s}\n")
            # for s in tag_list:
            #     file.write(f"tag: {s}\n")
            # for s in child_tag_list:
            #     file.write(f"child_tag: {s}\n")

        file.close()

    def analyze_all_talon_community() -> dict[str, list[str]]:
        """Print out a sheet of talon commands"""

        app_to_tag_dict = dict()

        file_list = actions.user.generate_talon_file_list()
        for filename in file_list:
            app_list, tag_list, child_tag_list = actions.user.analyze_file(filename)
            for app in app_list:
                app_to_tag_dict[app] = child_tag_list

        return app_to_tag_dict

    @staticmethod
    def analyze_file(filename: str) -> Tuple[list[str], list[str], list[str]]:
        """This function is a test."""
        app_list = []
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
                            tag_list.append(v)
            else:
                bits = line.split()
                if len(bits) == 2 and bits[0] == "tag():" and len(bits[1]) > 1:
                    child_tag_list.append(bits[1])

        file.close()
        return [app_list, tag_list, child_tag_list]
            
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