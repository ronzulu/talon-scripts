mode: command
mode: dictation
-

^(toggle mode | toed | tod | toad)$:
    current = user.rz_get_current_mode()
    opposite = user.rz_get_opposite_mode()
    mode.disable(current)
    mode.enable(opposite)
