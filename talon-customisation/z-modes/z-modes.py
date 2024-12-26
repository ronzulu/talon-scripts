import re
from typing import Dict
from talon import Module, actions

mod = Module()

global_next_pre_phrase = ""
global_next_format = ""
global_subsequent_pre_phrase = ""
global_subsequent_format = ""

@mod.action_class
class ZModeActions:
    def rz_set_format(name: str):
        "Set the format used by following calls to rz_add"
        match name:
            case "Z1":
                actions.user.rz_set_next_format("", "PUBLIC_CAMEL_CASE")
            case "Z1L":
                actions.user.rz_set_next_format("", "PRIVATE_CAMEL_CASE")
                actions.user.rz_set_subsequent_format("", "PUBLIC_CAMEL_CASE")
            case "Z1LS":
                actions.user.rz_set_next_format(" ", "PRIVATE_CAMEL_CASE")
                actions.user.rz_set_subsequent_format("", "PUBLIC_CAMEL_CASE")
            case "Z2":
                actions.user.rz_set_next_format("", "NOOP")
                actions.user.rz_set_subsequent_format(" ", "NOOP")
            case "Z2C":
                actions.user.rz_set_next_format("", "CAPITALIZE_FIRST_WORD")
                actions.user.rz_set_subsequent_format(" ", "NOOP")
            case "Z2S":
                actions.user.rz_set_next_format(" ", "NOOP")
                actions.user.rz_set_subsequent_format(" ", "NOOP")
            case "Z2SC":
                actions.user.rz_set_next_format(" ", "CAPITALIZE_FIRST_WORD")
                actions.user.rz_set_subsequent_format(" ", "NOOP")
            case "Z3":
                actions.user.rz_set_next_format("", "CAPITALIZE_ALL_WORDS")
                actions.user.rz_set_subsequent_format(" ", "CAPITALIZE_ALL_WORDS")
            case "Z3S":
                actions.user.rz_set_next_format(" ", "CAPITALIZE_ALL_WORDS")
                actions.user.rz_set_subsequent_format(" ", "CAPITALIZE_ALL_WORDS")
            case "Z4":
                actions.user.rz_set_next_format("", "ALL_CAPS")
                actions.user.rz_set_subsequent_format(" ", "ALL_CAPS")
            case "Z4S":
                actions.user.rz_set_next_format(" ", "ALL_CAPS")
                actions.user.rz_set_subsequent_format(" ", "ALL_CAPS")


    def rz_set_next_format(pre_phrase: str, format: str):
        "Set the format used by following calls to rz_add"
        global global_next_pre_phrase, global_next_format
        global global_subsequent_pre_phrase, global_subsequent_format

        global_next_pre_phrase = pre_phrase
        global_next_format = format
        global_subsequent_pre_phrase = pre_phrase
        global_subsequent_format = format

    def rz_set_subsequent_format(pre_phrase: str, format: str):
        "Set the format used by following calls to rz_add"
        global global_subsequent_pre_phrase, global_subsequent_format

        global_subsequent_pre_phrase = pre_phrase
        global_subsequent_format = format

    def rz_add(text: str):
        "Inserts the supplied text, formatted as per last call to rz_set_format"
        global global_next_pre_phrase, global_next_format
        global global_subsequent_pre_phrase, global_subsequent_format
        
        if global_next_pre_phrase:
            actions.insert(global_next_pre_phrase)

        str = actions.user.convert_words_to_symbols(text)
        actions.user.insert_formatted(str, global_next_format)
        global_next_format = global_subsequent_format
        global_next_pre_phrase = global_subsequent_pre_phrase

    @staticmethod
    def convert_words_to_symbols(text: str):
        "Hello"
        words = text.split(" ")
        for i, word in enumerate(words):
            if word.lower() == "dot":
                words[i] = "."

        return " ".join(words)
    
    def rz_insert_key_sequence(text: str):
        "Inserts the supplied text, formatted as per last call to rz_set_format"
        # print(f"rz_insert_key_sequence: {text}")
        words = actions.user.extract_substrings(text)
        for w in words:
            word = str(w)
            # print(f"word: {word}")
            if word.startswith("{") and word.endswith("}"):
                s = word[1:-1]
                actions.user.handle_command(s)
            else:
                actions.insert(word)

        # actions.insert("hello:")
        # actions.insert("|".join(str))
        #         actions.user.insert_formatted("count: {str}")
#         actions.user.insert_formatted("|".join(str), global_next_format)
        
    @staticmethod
    def handle_command(s: str):
        "Hello"
        if s.startswith("Z"):
            actions.user.rz_set_format(s)
        elif s.startswith("wait:"):
            actions.sleep("{s[5:]}ms")
        elif s == "l-brace":
            actions.insert('{')
        elif s == "r-brace":
            actions.insert('}')
        else:
            actions.key(s)
       
    @staticmethod
    def extract_substrings(s: str):
        "Hello"
        # Regular expression to match sequences without '{' and sequences within '{...}'
        pattern = re.compile(r'\{?[^{}]+\}?|\{[^}]*\}')
        matches = pattern.findall(s)
        return matches



