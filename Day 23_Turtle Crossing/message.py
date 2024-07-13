from turtle import Turtle

TEXT_COLOR = "black"
SPEED = 0
ALIGN = "center"
FONT = ("Futura", 50, "bold")
CLEARED_TEXT = "CLEARED!"
GAME_OVER_TEXT = "GAME OVER"


class Message(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(TEXT_COLOR)
        self.speed(SPEED)
        self.goto(0, 0)

    def game_end(self):
        self.write(CLEARED_TEXT, align=ALIGN, font=FONT)

    def game_over(self):
        self.write(GAME_OVER_TEXT, align=ALIGN, font=FONT)
