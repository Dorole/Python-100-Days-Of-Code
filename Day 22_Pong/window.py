from turtle import Screen, Turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = "deepskyblue2"
TITLE = "PONG"
PADDLE_OFFSET = 50
LINE_COLOR = "lightgoldenrodyellow"


class Window:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor(SCREEN_COLOR)
        self.screen.title(TITLE)
        self.screen.tracer(0)
        self.draw_line()
        self.screen.listen()

    def get_borders(self):
        screen_size = self.screen.screensize()
        horizontal_border = screen_size[0]
        vertical_border = screen_size[1]
        borders = {
            "top": vertical_border,
            "bottom": -vertical_border,
            "right": horizontal_border,
            "left": -horizontal_border
        }
        return borders

    def draw_line(self):
        line = Turtle()
        line.pensize(1)
        line.pencolor(LINE_COLOR)
        line.hideturtle()
        line.goto(0, SCREEN_HEIGHT/2)
        line.speed(0)
        line.goto(0, -SCREEN_HEIGHT/2)
