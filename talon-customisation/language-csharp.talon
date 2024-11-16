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

# "kind" used instead of "type"
# for example:
#   "kind integer" -> "int"
#   "kind integer s" -> "int "
#   "kind string l p" -> "string lp"
kind <user.code_datatype_ex>: 
    insert("{code_datatype_ex}")

kind <user.code_concrete_generic>: 
    insert("{code_concrete_generic}")
