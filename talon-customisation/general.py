from talon import Module
import time

mod = Module()

@mod.action_class
class Actions:
    def my_custom_date_function():
        """My custom date function"""
        return time.strftime("%Y-%m-%d")