import datetime
from talon import Context, Module
mod = Module()
mod.list("month", desc="the names of the months")
mod.list("date_format", desc="date format")


@mod.action_class
class DateFormatter:
    def date_formatter_format_date(day_of_month: int, month: str, year: int, date_format: str):
        "Set the format used by following calls to rz_add"
        date_str = f"{day_of_month} {month} {year}"
        date_value = datetime.datetime.strptime(date_str, "%d %B %Y").date()
        return date_value.strftime(date_format)

ctx = Context()

ctx.lists["self.date_format"] = {
    "long": "%d %B %Y",
    "us": "%m/%d/%Y"
}
