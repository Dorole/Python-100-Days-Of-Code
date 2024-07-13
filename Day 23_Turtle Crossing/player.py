from turtle import Turtle

PLAYER_COLOR ="green4"
MOVE_STEP = 25


class Player(Turtle):
    def __init__(self, start_y):
        super().__init__(shape="turtle")
        self.color(PLAYER_COLOR)
        self.penup()
        self.setheading(90)
        self.start_y = start_y
        self.set_init_pos(self.start_y)
        self.should_move = False
        self.hideturtle()

    def move_player(self):
        if self.should_move:
            self.forward(MOVE_STEP)

    def set_init_pos(self, start_y):
        self.setpos(0, start_y)

    def get_y_cor(self):
        return self.ycor()

    def show_self(self):
        self.showturtle()

    def reset_player(self):
        self.hideturtle()
        self.set_init_pos(self.start_y)
        self.should_move = False

