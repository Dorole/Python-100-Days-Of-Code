from turtle import Turtle

CAR_LEN = 1.5


class Car(Turtle):
    def __init__(self, color):
        super().__init__(shape="square")
        self.shapesize(stretch_len=CAR_LEN)
        self.color(color)
        self.penup()
        self.setheading(180)
        self.car_speed = 0
