# code.language: csharp
# -


# state very hello <user.code_access_modifier>: insert("hellox")
# state very hello [user.code_access_modifier]: "hellox: "
# state goodbye <user.code_access_modifiers>: insert("hello: " + code_access_modifiers)

<user.code_statement_prefix> new: "new "


# for example: "state public abstract" -> "public abstract"
<user.code_statement_prefix> <user.code_modifiers>: 
    insert("{code_modifiers} ")

# for example: "state public static boolean" -> "public static bool "
<user.code_statement_prefix> <user.code_modifiers> <user.code_datatype>: 
    insert("{code_modifiers} {code_datatype} ")

# for example: "kind integer" -> "int"
# "kind" used instead of "type"
kind <user.code_datatype> [<user.code_whitespace>]: 
    insert("{code_datatype}{code_whitespace or ''}")

kind <user.code_concrete_generic>: 
    insert("{code_concrete_generic}")

# for example: "kind string l p" -> "string lp"
kind <user.code_datatype> <user.variable_prefix> : 
    insert("{code_datatype} {variable_prefix}")
