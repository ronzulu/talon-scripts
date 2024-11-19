from talon import Module, scope
from talon.scripting.core import mode

mod = Module()

@mod.action_class
class ZHello:
    def rz_toggle_command_dictation_mode():
        "Set the format used by following calls to rz_add"
        modes = scope.get("mode")
        if "dictation" in modes:
            mode.disable("dictation")
            mode.enable("command")
        else:
            mode.disable("command")
            mode.enable("dictation")

    def rz_get_current_mode()->str:
        "Set the format used by following calls to rz_add"
        modes = scope.get("mode")
        if "dictation" in modes:
            result = "dictation"
        else:
            result = "command"
        return result
        
    def rz_get_opposite_mode()->str:
        "Set the format used by following calls to rz_add"
        modes = scope.get("mode")
        if "dictation" in modes:
            result = "command"
        else:
            result = "dictation"
        return result
        