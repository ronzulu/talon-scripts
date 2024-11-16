language: en
-
pass are: "parser"
hello talon: "hello world90210!!"
hello friend: "rnd"
test it sometime: user.rz_insert_key_sequence("{{left-brace}}{{enter}}{{enter}}{{up}}{{end}}{{tab}}")

(c name space | c namespace | ten name space): "namespace "
state new: "new "

(hullo | hallo) : "hello"

# new block: mimic("c new block")

echo: "e"

dock you sore us: "docusaurus"
# <user.word>$: user.rz_add(word)

# something reasonably: "<something reasonably>"
# something reasonably interesting: "<something reasonably interesting>"
# interesting: "<interesting>"

{user.dictionary}: user.rz_insert_key_sequence("{dictionary}")
# proud {user.dictionary}: "p2:{dictionary}"
prouder {user.dictionary}: user.rz_insert_key_sequence(str("p3:") + "{dictionary}")

(Zulaikha | zoo like her): "Zulaikha"


middle drag | drag middle:
    # close zoom if open
    user.zoom_close()
    user.mouse_drag(2)
    # close the mouse grid
    user.grid_close()

^next {user.clickless_mouse_action}$: 
    user.clickless_mouse_next_standstill_action(clickless_mouse_action)
