from turtle import Screen


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
BG_COLOR = "black"
WINDOW_TITLE = "Ye Olde Snake Game"


class Window:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.screen.bgcolor(BG_COLOR)
        self.screen.title(WINDOW_TITLE)
        self.screen.tracer(0)
        self.x_border = self.screen.window_width() // 2
        self.y_border = self.screen.window_height() // 2

    def get_screen(self):
        return self.screen
