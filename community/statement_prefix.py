from talon import Context, Module, app

mod = Module()
mod.list("code_statement_prefix", desc="All table keys")


@mod.capture(rule="{self.code_statement_prefix}")
def code_statement_prefix(m) -> str:
    "One directional table key"
    return m.code_statement_prefix


ctx = Context()

ctx.lists["self.code_statement_prefix"] = {
    "state": "state",
    "tat": "state",
}
