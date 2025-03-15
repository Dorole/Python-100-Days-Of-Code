from enum import Enum, auto

TOMATO_PNG = "./assets/tomato.png"
BUTTON_SOUND = "./assets/plop.wav"
TICK_SOUND = "./assets/tick.wav"
SESSION_START_SOUND = "./assets/session-end.wav"
CYCLE_END_SOUND = "./assets/cycle-end.mp3"

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
DEFAULT_FONT = (FONT_NAME, 35, "bold")
CHECKMARK_SIGN = "🗹"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
CYCLE = 8

CANVAS_WIDTH = 200
CANVAS_HEIGHT = 224
ELEMENT_OFFSET = 20


class EventType(Enum):
    BUTTON_LABEL_EVENT = auto()
    BUTTON_STATE_EVENT = auto()
    RESET_EVENT = auto()
    CYCLE_END_EVENT = auto()
    STATUS_CHANGE_EVENT = auto()
    TIMER_EVENT = auto()
