from talon import Context, Module, app

mod = Module()
mod.list("code_modifier", desc="All table keys")
mod.list("code_datatype", desc="All table keys")
mod.list("code_collections", desc="All table keys")
mod.list("variable_prefix", desc="All table keys")


@mod.capture(rule="{self.code_modifier}")
def code_modifier(m) -> str:
    "One directional table key"
    return m.code_modifier


@mod.capture(rule="<self.code_modifier>+")
def code_modifiers(m) -> str:
    "One or more table keys separated by a space"
    return str(m)

@mod.capture(rule="{self.code_datatype}")
def code_datatype(m) -> str:
    "One directional table key"
    return m.code_datatype

@mod.capture(rule="{self.variable_prefix}")
def variable_prefix(m) -> str:
    "One directional table key"
    return m.variable_prefix

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

ctx.lists["self.code_datatype"] = {
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

ctx.lists["self.code_collections"] = {
    "list": "List",
    "dictionary": "Dictionary",
#    "": "",
}
