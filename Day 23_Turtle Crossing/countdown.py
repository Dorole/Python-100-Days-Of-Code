from turtle import Turtle

TEXT_COLOR = "black"
SPEED = 0
ALIGN = "center"
FONT = ("Futura", 100, "bold")
TIME_TO_START = 6
DURATION = 1


class Countdown(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(TEXT_COLOR)
        self.speed(SPEED)
        self.previous_time = None
        self.countdown = TIME_TO_START
        self.finished = False
        self.goto(0, 0)

    def update_time(self, current_time):
        current_rounded = round(current_time)
        if self.previous_time is None:
            self.previous_time = current_rounded
        if current_rounded - self.previous_time >= DURATION:
            self.previous_time = current_rounded
            return True
        return False

    def display_countdown(self, current_time):
        if self.update_time(current_time):
            self.countdown -= 1
            if self.countdown > 0:
                self.clear()
                self.write(self.countdown, align=ALIGN, font=FONT)
            elif self.countdown == 0:
                self.clear()
                self.write("GO!", align=ALIGN, font=FONT)
            else:
                self.finished = True
                self.clear()

    def reset_countdown(self):
        self.countdown = TIME_TO_START
        self.finished = False
