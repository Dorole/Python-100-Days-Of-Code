import turtle


class EtchASketch:
    def __init__(self):
        self.MOVE_UNIT = 20
        self.TURN_UNIT = 10
        self.my_turtle = turtle.Turtle()
        self.screen = turtle.Screen()

        self.function_dictionary = {
            "w": self.move_forwards,
            "s": self.move_backwards,
            "a": self.rotate_left,
            "d": self.rotate_right,
            "c": self.reset_turtle
        }

    def move_forwards(self):
        self.my_turtle.forward(self.MOVE_UNIT)

    def move_backwards(self):
        self.my_turtle.backward(self.MOVE_UNIT)

    def rotate_left(self):
        self.my_turtle.left(self.TURN_UNIT)

    def rotate_right(self):
        self.my_turtle.right(self.TURN_UNIT)

    def reset_turtle(self):
        self.my_turtle.reset()

    def sketch(self):
        for func in self.function_dictionary:
            self.screen.onkey(key=func, fun=self.function_dictionary[func])

        self.screen.listen()
        self.screen.exitonclick()
