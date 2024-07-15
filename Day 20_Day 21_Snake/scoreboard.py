from turtle import Turtle
import data_handler

OFFSET = 30
COLOR = "white"
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")
SCORE_INCREASE = 1


class Scoreboard(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.score = 0
        self.high_score = data_handler.get_highscore()
        self.speed(0)
        self.goto(0.0, (screen.window_height()//2)-OFFSET)
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.update_score()

    def increase_score(self):
        self.score += SCORE_INCREASE
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            data_handler.write_highscore(self.high_score)
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
