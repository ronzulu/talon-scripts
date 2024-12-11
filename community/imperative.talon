tag: user.code_imperative
language: en
-
block: user.code_block()
<user.code_statement_prefix> if: user.code_state_if()
<user.code_statement_prefix> else if: user.code_state_else_if()
<user.code_statement_prefix> else: user.code_state_else()
<user.code_statement_prefix> while: user.code_state_while()
<user.code_statement_prefix> loop: user.code_state_infinite_loop()
<user.code_statement_prefix> for: user.code_state_for()
<user.code_statement_prefix> for in: user.code_state_for_each()
<user.code_statement_prefix> (switch | match): user.code_state_switch()
<user.code_statement_prefix> case: user.code_state_case()
<user.code_statement_prefix> do: user.code_state_do()
<user.code_statement_prefix> goto: user.code_state_go_to()
<user.code_statement_prefix> return: user.code_state_return()
<user.code_statement_prefix> break: user.code_break()
<user.code_statement_prefix> (continue | next): user.code_next()
