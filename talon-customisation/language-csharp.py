from talon import Context, Module, app

mod = Module()
mod.list("code_modifier", desc="All table keys")
mod.list("code_datatype_simple", desc="All table keys")
mod.list("code_generic_type", desc="All table keys")
mod.list("variable_prefix", desc="All table keys")
mod.list("code_whitespace", desc="All table keys")

# "code_modifier" is a list, "code_modifiers" (plural) is a capture
@mod.capture(rule="{self.code_modifier}+")
def code_modifiers(m) -> str:
    "One or more table keys separated by a space"
    return str(m)

@mod.capture(rule="{self.variable_prefix}")
def variable_prefix(m) -> str:
    "One directional table key"

@mod.capture(rule="[{self.code_generic_type} [of]] [{self.code_generic_type} [of]] {self.code_datatype_simple}")
def code_datatype_complex(m) -> str:
    "One directional table key"
    if hasattr(m, "code_generic_type_2"):
        part2 = f"{m.code_generic_type_2}<{m.code_datatype_simple}>"
    else:
        part2 = m.code_datatype_simple

    if hasattr(m, "code_generic_type_1"):
        str = f"{m.code_generic_type_1}<{part2}>"
    else:
        str = part2
    return str

@mod.capture(rule="<self.code_datatype_complex> [{self.variable_prefix}]")
def code_datatype_ex(m) -> str:
    print("code_datatype_ex: ", type(m), m)
    str = m.code_datatype_complex
    str += " "
    if hasattr(m, "variable_prefix"):
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
