from turtle import Turtle
import random

OFFSET = 20


class Food(Turtle):
    def __init__(self, screen):
        super().__init__(shape="square")
        self.penup()
        self.color("green")
        self.speed(0)

        self.x_edge = screen.window_width()//2
        self.y_edge = screen.window_height()//2

        self.spawn()

    def spawn(self):
        rand_x = random.randrange(-(self.x_edge-OFFSET), self.x_edge-OFFSET, OFFSET)
        rand_y = random.randrange(-(self.y_edge-OFFSET), self.y_edge-OFFSET, OFFSET)
        self.goto(rand_x, rand_y)
