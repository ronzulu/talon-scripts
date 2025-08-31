# Character sequences
back tab tab: user.rz_insert_key_sequence("{{shift-tab}}{{shift-tab}}")
control shift india: user.rz_insert_key_sequence("{{ctrl-shift-i}}")
back tab copy: user.rz_insert_key_sequence("{{shift-tab}}{{ctrl-c}}")
back tab: user.rz_insert_key_sequence("{{shift-tab}}")
control shift five: user.rz_insert_key_sequence("{{ctrl-shift-5}}")
control shift enter: user.rz_insert_key_sequence("{{ctrl-shift-enter}}")
control shift f three: user.rz_insert_key_sequence("{{ctrl-shift-f3}}")
control shift juliet: user.rz_insert_key_sequence("{{ctrl-j}}")
control shift mike: user.rz_insert_key_sequence("{{ctrl-m}}")
control shift november: user.rz_insert_key_sequence("{{ctrl-n}}")
document menu: user.rz_insert_key_sequence("{{alt--}}")
move window: user.rz_insert_key_sequence("{{alt-space}}m")
new line: user.rz_insert_key_sequence("{{enter}}")
next document: user.rz_insert_key_sequence("{{ctrl-f6}}")
tab key enter: user.rz_insert_key_sequence("{{tab}}{{enter}}")
up enter: user.rz_insert_key_sequence("{{up}}{{enter}}")
(back | bat) quote: "`"
single quote: "'"
(open | close) quote: '"'
left p: "("
right p: ")"
clothes: "close"
apostrophe s: "'s"
pad arrow: " -> "

# Text deletion
(backspace | bat space | brack space): user.rz_insert_key_sequence("{{backspace}}")
# control delete: user.rz_insert_key_sequence("{{ctrl-del}}")
delete back: user.rz_insert_key_sequence("{{del}}{{backspace}}")
delete bottom of document: user.rz_insert_key_sequence("{{ctrl-shift-end}}{{del}}")
delete end key left: user.rz_insert_key_sequence("{{shift-end}}{{shift-left}}{{del}}")
delete end key: user.rz_insert_key_sequence("{{shift-end}}{{del}}")
delete enter: user.rz_insert_key_sequence("{{del}}{{enter}}")
delete house key: user.rz_insert_key_sequence("{{shift-home}}{{del}}")
# delete key (two | to): user.rz_insert_key_sequence("{{del}}{{del}}")
delete space: user.rz_insert_key_sequence("{{del}}{{space}}")
delete top of document: user.rz_insert_key_sequence("{{ctrl-shift-home}}{{del}}")

# Navigation
beginning of line: user.rz_insert_key_sequence("{{home}}")
bottom of document: user.rz_insert_key_sequence("{{ctrl-end}}")
# removed the ~twenty move commands (and others) and retraining to use the standard talon go commands
# control left two: user.rz_insert_key_sequence("{{ctrl-left}}{{ctrl-left}}")
#   down arrow: user.rz_insert_key_sequence("{{down}}")
end key: user.rz_insert_key_sequence("{{end}}")
end of line: user.rz_insert_key_sequence("{{end}}")
home key: user.rz_insert_key_sequence("{{home}}")
#   move down one: user.rz_insert_key_sequence("{{down}}")
#   page d two: user.rz_insert_key_sequence("{{pagedown}}{{pagedown}}")
#   tab key two: user.rz_insert_key_sequence("{{tab}}{{tab}}")

# Text selection and clipboard functions
copy all clipboard: user.rz_insert_key_sequence("{{ctrl-a}}{{ctrl-c}}")
(copy end key | end key copy): user.rz_insert_key_sequence("{{shift-end}}{{ctrl-c}}")
copy (home | house) key: user.rz_insert_key_sequence("{{shift-home}}{{ctrl-c}}")
home key copy: user.rz_insert_key_sequence("{{shift-home}}{{ctrl-c}}")
cut end key: user.rz_insert_key_sequence("{{shift-end}}{{ctrl-x}}")
cut house key: user.rz_insert_key_sequence("{{shift-home}}{{ctrl-x}}")
edit duplicate: user.rz_insert_key_sequence("{{ctrl-c}}{{ctrl-v}}{{ctrl-v}}")
go and paste: user.rz_insert_key_sequence("{{enter}}{{ctrl-v}}")
# k left one: user.rz_insert_key_sequence("{{ctrl-shift-left}}")
paste and go: user.rz_insert_key_sequence("{{ctrl-v}}{{enter}}")
paste end key: user.rz_insert_key_sequence("{{shift-end}}{{ctrl-v}}")
paste house key: user.rz_insert_key_sequence("{{shift-home}}{{ctrl-v}}")
replace all: user.rz_insert_key_sequence("{{ctrl-end}}{{ctrl-shift-home}}{{ctrl-v}}")
shift bottom of document: user.rz_insert_key_sequence("{{shift-ctrl-end}}")
# shift d one: user.rz_insert_key_sequence("{{shift-down}}")
shift end key left: user.rz_insert_key_sequence("{{shift-end}}{{shift-left}}")
shift end key: user.rz_insert_key_sequence("{{shift-end}}")
shift enter [key]: user.rz_insert_key_sequence("{{shift-enter}}")
shift house key: user.rz_insert_key_sequence("{{shift-home}}")
(shift | cell | select) (page | scroll) down: user.rz_insert_key_sequence("{{shift-pagedown}}")
(shift | cell | select) (page | scroll) up: user.rz_insert_key_sequence("{{shift-pageup}}")
shift top of document: user.rz_insert_key_sequence("{{shift-ctrl-home}}")
single quote paste quote: user.rz_insert_key_sequence("'{{ctrl-v}}'")
space and paste: user.rz_insert_key_sequence("{{space}}{{ctrl-v}}")
tab key copy: user.rz_insert_key_sequence("{{tab}}{{ctrl-c}}")
tab key paste: user.rz_insert_key_sequence("{{tab}}{{ctrl-v}}")
tab key: user.rz_insert_key_sequence("{{tab}}")

hunt (all | for) (that | clipboard): 
    edit.copy()
    user.find_everywhere("")
    sleep(25ms)
    edit.paste()
(duke and | key cat | dubclick) hunt [all]: 
    mouse_click()
    mouse_click()
    sleep(25ms)
    mimic("hunt all that")
(duke and | key cat | dubclick) copy: 
    mouse_click()
    mouse_click()
    sleep(25ms)
    edit.copy()
(duke and | key cat | dubclick) paste: 
    mouse_click()
    mouse_click()
    sleep(25ms)
    edit.paste()


sell word left: edit.extend_word_left()
sell word right: edit.extend_word_right()
sell left: edit.extend_left()
sell right: edit.extend_right()
sell down: user.rz_insert_key_sequence("{{shift-down}}")
sell up: user.rz_insert_key_sequence("{{shift-up}}")
delete left: mimic("clear left")
delete right: mimic("clear right")
delete up: mimic("clear up")
delete down: mimic("clear down")
delete word left: mimic("clear word left")
delete word right: mimic("clear word right")

cap air: "A"
cap bat: "B"
cap cute: "C"
cap drum: "D"
cap echo: "E"
cap fine: "F"
cap golf: "G"
cap harp: "H"
cap indie: "I"
cap julie: "J"
cap kilo: "K"
cap lima: "L"
cap mike: "M"
cap near: "N"
cap ox: "O"
cap pit: "P"
cap quench: "Q"
cap red: "R"
cap sun: "S"
cap trap: "T"
cap urge: "U"
cap vest: "V"
cap whale: "W"
cap plex: "X"
cap yank: "Y"
cap zip: "Z"

# Belongs elsewhere?
dot el: user.rz_insert_key_sequence(".{{Z1L}}")
p hot mail: user.rz_insert_key_sequence("bellyB@44HM{{enter}}")
r z five: "rz"

show notifications: key(win-n)

today y m d:
    result = user.my_custom_date_function()
    insert(result)