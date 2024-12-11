# go word left: edit.word_left()
# go word right: edit.word_right()

file save (every | everything): edit.save_all()

date [insert] <number_small> {user.month} <number>: 
    str = user.date_formatter_format_date(number_small, month, number, "long")
    insert(str)
