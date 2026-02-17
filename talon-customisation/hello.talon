language: en
-
(c name space | c namespace | ten name space): "namespace "
state new: "new "

(hullo | hallo) : "hello"

# new block: mimic("c new block")

echo: "e"

# <user.word>$: user.rz_add(word)

# something reasonably: "<something reasonably>"
# something reasonably interesting: "<something reasonably interesting>"
# interesting: "<interesting>"

{user.dictionary}: user.rz_insert_key_sequence("{dictionary}")
# proud {user.dictionary}: "p2:{dictionary}"
prouder {user.dictionary}: user.rz_insert_key_sequence("{dictionary}")

(Zulaikha | zoo like her): "Zulaikha"


middle drag | drag middle:
    # close zoom if open
    user.zoom_close()
    user.mouse_drag(2)
    # close the mouse grid
    user.grid_close()

^next {user.clickless_mouse_action}$: 
    user.clickless_mouse_next_standstill_action(clickless_mouse_action)

cap p <number_small>: "P{number_small}"
cap p <number_small> dash <number_small>: "P{number_small_1}-{number_small_2}"

replace all from clipboard:
    edit.select_all()
    edit.paste()
