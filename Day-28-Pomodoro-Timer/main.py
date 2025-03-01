import tkinter as tk

# TODO: Remove global variables
# TODO: Refactor to separate concerns
# TODO: Add sounds (playsounds?) at start of every sessions and 3 final seconds of every session

# ---------------------------- CONSTANTS ------------------------------- #
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


# ---------------------------- GLOBAL VARIABLES ------------------------------- #
timer = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    reset_cycle()
    start_timer()


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():  # TODO: does too many things (UI) - refactor!
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    update_button(reps > CYCLE)

    if reps > CYCLE:
        update_status_ui("Pomodoro", PINK)
        reset_cycle()
        return
    elif reps == CYCLE:
        count_down(long_break_sec)
        update_status_ui("BREAK", RED)
    elif reps % 2 == 1:
        count_down(work_sec)
        update_status_ui("WORK", GREEN)
    else:
        count_down(short_break_sec)
        update_status_ui("BREAK", PINK)

    if reps % 2 == 0:
        checkmark["text"] += CHECKMARK_SIGN
        window.bell()


def update_status_ui(status_text, color):
    timer_label.config(text=status_text, fg=color)


def update_button(is_active):
    start_button["state"] = "active" if is_active else "disabled"


def reset_cycle():
    global reps
    reps = 0
    checkmark.config(text="")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(counter):
    minutes, seconds = divmod(counter, 60)
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")  # TODO: UI - should not be in here?
    if counter > 0:
        global timer
        timer = window.after(1000, count_down, counter - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, highlightthickness=0, bg=YELLOW)
tomato_img = tk.PhotoImage(file="./tomato.png")
canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=tomato_img)
timer_text = canvas.create_text(CANVAS_WIDTH/2, (CANVAS_HEIGHT/2)+ELEMENT_OFFSET, text="00:00",
                                font=DEFAULT_FONT, fill="white")
canvas.grid(column=1, row=1)

timer_label = tk.Label(text="Pomodoro", font=DEFAULT_FONT, bg=YELLOW, fg=PINK, width=8)
timer_label.grid(column=1, row=0)

start_button = tk.Button(text="START", bg="white", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="RESET", bg="white", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = tk.Label(text="", font=DEFAULT_FONT, bg=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)

window.mainloop()
