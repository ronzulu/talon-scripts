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

        actions.user.insert_formatted(text, global_next_format)
        global_next_format = global_subsequent_format
        global_next_pre_phrase = global_subsequent_pre_phrase
