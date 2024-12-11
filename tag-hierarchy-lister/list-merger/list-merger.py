import os
from talon import Module

mod = Module()

class list_merger:
    START_MARKER = "##### GLOBAL_VOCAB_MARKER"
    GLOBAL_VOCAB_FILENAME = r"C:\Users\ronny\AppData\Roaming\talon\user\talon-scripts\talon-customisation\global-vocabulary.txt"
    DICTATION_TALON_LIST = r"C:\Users\ronny\AppData\Roaming\talon\user\talon-scripts\talon-customisation\dictation-list.talon-list"
    VOCABULARY_TALON_LIST = r"C:\Users\ronny\AppData\Roaming\talon\user\talon-scripts\talon-customisation\vocabulary.talon-list"

    def perform_merging(self):
        """Print out a sheet of talon commands"""
        self.merge_file(list_merger.GLOBAL_VOCAB_FILENAME, list_merger.VOCABULARY_TALON_LIST)
        self.merge_file(list_merger.GLOBAL_VOCAB_FILENAME, list_merger.DICTATION_TALON_LIST)

    def merge_file(self, global_filename: str, target_filename: str):
        """Print out a sheet of talon commands"""

        print("global_filename:", global_filename)
        print("target_filename:", target_filename)
        self.remove_global_section(target_filename)
        with (
            open(target_filename, 'a+') as target_file, 
            open(global_filename, 'r') as source_file
        ):
            target_file.writelines([list_merger.START_MARKER + '\n'])
            target_file.write(source_file.read())

    def remove_global_section(self, filename: str):
        """Print out a sheet of talon commands"""
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        line_index = None
        for i in range(len(lines)):
            if lines[i].startswith(list_merger.START_MARKER):
                line_index = i
                break
        
        print("line_index:", line_index)
        if line_index:
            with open(filename, 'w') as file:
                file.writelines(lines[:line_index])

@mod.action_class
class user_actions:

    def rz_update_talon_list():
        """Print out a sheet of talon commands"""
        merger = list_merger()
        merger.perform_merging()
