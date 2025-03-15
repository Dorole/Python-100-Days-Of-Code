import tkinter as tk
import config
from sound_manager import SoundManager


class PomodoroUI:
    def __init__(self, root, event_manager, timer):
        self.root = root
        self.event_manager = event_manager
        self.timer = timer
        self.window_setup(root)
        self.sound_manager = SoundManager()
        self.event = config.EventType

        self.canvas = tk.Canvas()
        self.tomato_img = tk.PhotoImage(file=config.TOMATO_PNG)
        self.timer_text = ""
        self.canvas_setup(self.canvas, self.tomato_img)

        self.start_button = tk.Button()
        self.reset_button = tk.Button()
        self.pause_button = tk.Button()
        self.buttons_setup(start_button=self.start_button, reset_button=self.reset_button, pause_button=self.pause_button)

        self.timer_label = tk.Label()
        self.checkmark = tk.Label()
        self.labels_setup(timer_label=self.timer_label, checkmark=self.checkmark)

        self.subscribe_to_events()

    def subscribe_to_events(self):
        self.event_manager.subscribe(self.event.BUTTON_STATE_EVENT, lambda state: self.update_button_state(self.start_button, state))
        self.event_manager.subscribe(self.event.BUTTON_LABEL_EVENT, lambda state: self.update_button_label(self.pause_button, state))
        self.event_manager.subscribe(self.event.RESET_EVENT, self.reset_ui)
        self.event_manager.subscribe(self.event.CYCLE_END_EVENT, self.update_checkmark)
        self.event_manager.subscribe(self.event.STATUS_CHANGE_EVENT, lambda state: self.update_status_ui(status_text=state[0], color=state[1]))
        self.event_manager.subscribe(self.event.TIMER_EVENT, self.update_timer_text)

    def update_button_state(self, button, is_active):
        button["state"] = "active" if is_active else "disabled"

    def update_button_label(self, button, state):
        button["text"] = "CONTINUE" if state else "PAUSE"

    def update_status_ui(self, status_text, color):
        self.timer_label.config(text=status_text, fg=color)

    def reset_ui(self, _):
        self.checkmark.config(text="")

    def update_checkmark(self, _):
        self.checkmark["text"] += config.CHECKMARK_SIGN

    def update_timer_text(self, text):
        self.canvas.itemconfig(self.timer_text, text=text)

    def window_setup(self, root):
        root.title("Pomodoro")
        root.config(padx=100, pady=15, bg=config.YELLOW)

    def canvas_setup(self, canvas, image):
        canvas.config(width=config.CANVAS_WIDTH, height=config.CANVAS_HEIGHT, highlightthickness=0, bg=config.YELLOW)
        canvas.create_image(config.CANVAS_WIDTH / 2, config.CANVAS_HEIGHT / 2, image=image)
        self.timer_text = canvas.create_text(config.CANVAS_WIDTH / 2, (config.CANVAS_HEIGHT / 2) + config.
                                             ELEMENT_OFFSET, text="00:00", font=config.DEFAULT_FONT, fill="white")
        canvas.grid(column=1, row=1, pady=25)

    def buttons_setup(self, start_button=None, reset_button=None, pause_button=None):
        start_button.config(text="START", bg="white", highlightthickness=0, command=lambda: self.on_button_click(self.timer.start_timer))
        start_button.grid(column=0, row=2)

        reset_button.config(text="RESET", bg="white", highlightthickness=0, command=lambda: self.on_button_click(self.timer.reset_cycle))
        reset_button.grid(column=2, row=2)

        pause_button.config(text="PAUSE", bg="white", highlightthickness=0, command=lambda: self.on_button_click(self.timer.pause_timer))
        pause_button.grid(column=1, row=2)

    def labels_setup(self, timer_label=None, checkmark=None):
        timer_label.config(text="Pomodoro", font=config.DEFAULT_FONT, bg=config.YELLOW, fg=config.PINK, width=8)
        timer_label.grid(column=1, row=0)

        checkmark.config(text="", font=config.DEFAULT_FONT, bg=config.YELLOW, fg=config.GREEN)
        checkmark.grid(column=1, row=3, pady=15)

    def on_button_click(self, func):
        func()
        self.sound_manager.play_button_sound()
