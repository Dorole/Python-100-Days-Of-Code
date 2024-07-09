from turtle import Turtle

TEXT_COLOR = "aquamarine"
SPEED = 0
X_COR = 100
Y_COR = 210
ALIGN = "center"
FONT = ("Futura", 60, "bold")
MAX_POINTS = 10


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(TEXT_COLOR)
        self.speed(SPEED)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def update_r_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-X_COR, Y_COR)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(X_COR, Y_COR)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def check_game_end(self):
        return self.l_score == MAX_POINTS or self.r_score == MAX_POINTS

    def display_game_end(self):
        winner = ""
        if self.l_score == MAX_POINTS:
            winner = "LEFT"
        else:
            winner = "RIGHT"
        self.home()
        self.write(f"{winner} PLAYER WINS!", align=ALIGN, font=("Futura", 40, "bold"))
