import tkinter as tk
from event_manager import EventManager
from pomodoro_timer import PomodoroTimer
from pomodoro_ui import PomodoroUI

root = tk.Tk()
event_manager = EventManager()
timer = PomodoroTimer(root, event_manager)
ui = PomodoroUI(root, event_manager, timer)

root.mainloop()
