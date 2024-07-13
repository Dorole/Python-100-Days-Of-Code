from turtle import Turtle, Screen

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = "gray70"
LINE_COLOR = "white"


class Display:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor(SCREEN_BG_COLOR)
        self.screen.tracer(0)
        self.screen.listen()
        self.draw_lines()
        self.borders = self.get_screen_borders()

    # TODO: Dashed lines?
    def draw_lines(self):
        line_painter = Turtle()
        line_painter.pensize(1)
        line_painter.speed(0)
        line_painter.pencolor(LINE_COLOR)
        line_painter.hideturtle()

        for i in range(SCREEN_HEIGHT // 2, -SCREEN_HEIGHT // 2, -50):
            line_painter.penup()
            line_painter.setposition(SCREEN_WIDTH // 2, i)
            line_painter.pendown()
            line_painter.goto(-SCREEN_WIDTH // 2, i)

    @staticmethod
    def get_screen_borders():
        top = SCREEN_HEIGHT//2
        bottom = -top
        right = SCREEN_WIDTH//2
        left = -right
        screen_borders = {
            "top": top,
            "bottom": bottom,
            "right": right,
            "left": left
        }
        return screen_borders

