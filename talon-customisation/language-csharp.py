from talon import Context, Module, app

mod = Module()
mod.list("code_modifier", desc="All table keys")
mod.list("code_datatype_simple", desc="All table keys")
mod.list("code_generic_type", desc="All table keys")
mod.list("variable_prefix", desc="All table keys")
mod.list("code_whitespace", desc="All table keys")


@mod.capture(rule="{self.code_modifier}")
def code_modifier(m) -> str:
    "One directional table key"
    return m.code_modifier


@mod.capture(rule="<self.code_modifier>+")
def code_modifiers(m) -> str:
    "One or more table keys separated by a space"
    return str(m)

@mod.capture(rule="{self.code_datatype_simple}")
def code_datatype_simple(m) -> str:
    "One directional table key"
    return m.code_datatype_simple

@mod.capture(rule="{self.variable_prefix}")
def variable_prefix(m) -> str:
    "One directional table key"
    return m.variable_prefix

@mod.capture(rule="{self.code_generic_type}")
def code_generic_type(m) -> str:
    "One directional table key"
    return m.code_generic_type

@mod.capture(rule="{self.code_whitespace}")
def code_whitespace(m) -> str:
    "One directional table key"
    return m.code_whitespace

@mod.capture(rule="{self.code_generic_type} [of] {self.code_datatype_simple}")
def code_concrete_generic(m) -> str:
    "One directional table key"
    return f"{m.code_generic_type}<{m.code_datatype_simple}>"

@mod.capture(rule="{self.code_datatype_simple} [{self.code_whitespace}] [{self.variable_prefix}]")
def code_datatype_ex(m) -> str:
    print("code_datatype_ex: ", type(m), m)
    str = m.code_datatype_simple
    if hasattr(m, "code_whitespace"):
        str += m.code_whitespace
    if hasattr(m, "variable_prefix"):
        if not hasattr(m, "code_whitespace"):
            str += " "
        str += m.variable_prefix
    "One directional table key"
    return str

ctx = Context()

ctx.lists["self.code_modifier"] = {
    "public": "public",
    "private": "private",
    "protected": "protected",
    "internal": "internal",
    "static": "static",
    "class": "class",
    "extern": "extern",
    "external": "extern",
    "virtual": "virtual",
    "abstract": "abstract",
    "override": "override",
    "sealed": "sealed",
    "const": "const",
    "constant": "const",
    "readonly": "readonly",
    "read only": "readonly",
    "volatile": "volatile",
    "acing": "async",
    "async": "async",
    "asynchronous": "async",
    "partial": "partial",
    "event": "event",
#    "": "",

}

ctx.lists["self.code_datatype_simple"] = {
    "boolean": "bool",
    "bullion": "bool",
    "integer": "int",
    "int": "int",
    "i n t p t r": "IntPtr",
    "int pointer": "IntPtr",
    "integer pointer": "IntPtr",
    "string": "string",
    "double": "double",
    "void": "void",
#    "": "",
}

ctx.lists["self.variable_prefix"] = {
    "l p": "lp",
#    "": "",
}

ctx.lists["self.code_generic_type"] = {
    "list": "List",
    "dictionary": "Dictionary",
#    "": "",
}

ctx.lists["self.code_whitespace"] = {
    "s": " ",
#    "": "",
}
