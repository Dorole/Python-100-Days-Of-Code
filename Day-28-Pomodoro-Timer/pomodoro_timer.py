from sound_manager import SoundManager
import config


class PomodoroTimer:
    def __init__(self, root, event_manager):
        super().__init__()
        self.root = root
        self.sound_manager = SoundManager()
        self.event_manager = event_manager
        self.event = config.EventType
        self.timer = None
        self.reps = 0
        self.paused = False
        self.remaining_time = 0
        self.cycle = config.CYCLE
        self.work_sec = config.WORK_MIN * 60
        self.short_break_sec = config.SHORT_BREAK_MIN * 60
        self.long_break_sec = config.LONG_BREAK_MIN * 60
        self.work_ui = ("WORK", config.GREEN)
        self.cycle_end_ui = ("Pomodoro", config.PINK)
        self.short_break_ui = ("BREAK", config.PINK)
        self.long_break_ui = ("BREAK", config.RED)

    def reset_cycle(self):
        self.reps = 0
        if self.paused:
            self.pause_timer()
        self.event_manager.raise_event(event_type=self.event.RESET_EVENT)

    def count_down(self, counter):
        if self.paused:
            return

        minutes, seconds = divmod(counter, 60)
        self.event_manager.raise_event(event_type=self.event.TIMER_EVENT, state=f"{minutes:02}:{seconds:02}")
        if counter > 0:
            self.remaining_time = counter - 1
            self.timer = self.root.after(1000, self.count_down, self.remaining_time)

            if counter <= 3:
                self.sound_manager.play_tick_sound()
        else:
            self.start_timer()

    def start_timer(self):
        self.reps += 1
        self.event_manager.raise_event(event_type=self.event.BUTTON_STATE_EVENT, state=self.reps > self.cycle)

        if self.reps > self.cycle:
            self.reset_cycle()
            self.sound_manager.play_cycle_end_sound()
            self.event_manager.raise_event(event_type=self.event.STATUS_CHANGE_EVENT, state=self.cycle_end_ui)
            return
        elif self.reps == self.cycle:
            self.count_down(self.long_break_sec)
            self.event_manager.raise_event(event_type=self.event.STATUS_CHANGE_EVENT, state=self.long_break_ui)
        elif self.reps % 2 == 1:
            self.count_down(self.work_sec)
            self.event_manager.raise_event(event_type=self.event.STATUS_CHANGE_EVENT, state=self.work_ui)
        else:
            self.count_down(self.short_break_sec)
            self.event_manager.raise_event(event_type=self.event.STATUS_CHANGE_EVENT, state=self.short_break_ui)

        if self.reps % 2 == 0:
            self.event_manager.raise_event(event_type=self.event.CYCLE_END_EVENT)

        self.sound_manager.play_session_start_sound()

    def pause_timer(self):
        if self.paused:
            self.paused = False
            self.count_down(self.remaining_time)
        else:
            self.paused = True
            self.root.after_cancel(self.timer)

        self.event_manager.raise_event(self.event.BUTTON_LABEL_EVENT, state=self.paused)
