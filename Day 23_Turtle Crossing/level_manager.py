from turtle import Turtle
from display import Display

TEXT_COLOR = "black"
SPEED = 0
ALIGN = "center"
FONT = ("Futura", 15, "normal")
TEXT_Y_OFFSET = 20
TEXT_X_OFFSET = 50
FINAL_LEVEL = 3


class LevelManager(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color(TEXT_COLOR)
        self.speed(SPEED)
        text_y_pos = Display.get_screen_borders()["bottom"] + TEXT_Y_OFFSET
        text_x_pos = Display.get_screen_borders()["left"] + TEXT_X_OFFSET
        self.goto(text_x_pos, text_y_pos)
        self.display_level()

    def level_up(self):
        self.level += 1
        self.clear()
        self.display_level()

    def display_level(self):
        self.write(f"LEVEL: {self.level}", align=ALIGN, font=FONT)

    def check_game_end(self):
        return self.level == FINAL_LEVEL
