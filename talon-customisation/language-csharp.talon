# code.language: csharp
# -


# state very hello <user.code_access_modifier>: insert("hellox")
# state very hello [user.code_access_modifier]: "hellox: "
# state goodbye <user.code_access_modifiers>: insert("hello: " + code_access_modifiers)
state hello: "hello everyone"

# for example: "state 
<user.code_statement_prefix> <user.code_modifiers>: 
    insert("{code_modifiers} ")

<user.code_statement_prefix> <user.code_modifiers> <user.code_datatype>: 
    insert("{code_modifiers} {code_datatype} ")

kind <user.code_datatype>: 
    insert("{code_datatype}")

kind <user.code_datatype> <user.variable_prefix> : 
    insert("{code_datatype} {variable_prefix}")

kind <user.code_datatype> s: 
    insert("{code_datatype} ")
