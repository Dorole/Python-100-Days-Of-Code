from turtle import Turtle

PADDLE_COLOR = "lightpink"
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_START_Y = 0
MOVE_INCREMENT = 20


class Paddle(Turtle):
    def __init__(self, start_x, window):
        super().__init__(shape="square")
        self.move_borders = window.get_borders()
        self.penup()
        self.shapesize(stretch_len=5)
        self.left(90)
        self.color(PADDLE_COLOR)
        self.goto(start_x, PADDLE_START_Y)

    def move_up(self):
        if self.distance(self.xcor(), self.move_borders["top"]) > (PADDLE_HEIGHT/2 + MOVE_INCREMENT):
            self.forward(20)

    def move_down(self):
        if self.distance(self.xcor(), self.move_borders["bottom"]) > (PADDLE_HEIGHT/2 + MOVE_INCREMENT):
            self.backward(20)
