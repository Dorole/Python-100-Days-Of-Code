import math
import random
from turtle import Turtle

BALL_COLOR = "gold"
START_SPEED = 0.1
MOVE_INCREMENT = 20
SCREEN_SAFE_ZONE = 20


class Ball(Turtle):
    def __init__(self, start_x, start_y, window):
        super().__init__(shape="circle")
        move_borders = window.get_borders()
        self.vertical_border = move_borders["top"]
        self.horizontal_border = move_borders["right"]
        self.penup()
        self.color(BALL_COLOR)
        self.setheading(random.randrange(-180, 180))
        self.goto(start_x, start_y)
        self.move_speed = START_SPEED
        self.move_increment = MOVE_INCREMENT

    def move(self):
        angle_in_radians = math.radians(self.heading())
        new_x = self.xcor() + self.move_increment * math.cos(angle_in_radians)
        new_y = self.ycor() + self.move_increment * math.sin(angle_in_radians)
        self.setposition(new_x, new_y)

    def check_wall_collision(self):
        if abs(self.ycor()) > self.vertical_border - SCREEN_SAFE_ZONE:
            new_heading = 360 - self.heading()
            self.setheading(new_heading)
            return True
        return False

    def check_paddle_collision(self, paddle):
        if self.distance(paddle) < 40:
            # add 180 to account for small values; %360 to ensure the value is in the 0-360 range
            new_heading = (360 - (self.heading() + 180)) % 360
            self.move_speed *= 0.9
            self.setheading(new_heading)
            return True
        return False

    def is_ball_screen_right(self):
        """Returns true if ball x-coordinate is greater than 0 (RIGHT half of the screen),
        false if it is below 0 (LEFT half of the screen)"""
        return self.xcor() > 0

    def get_ball_x_cor(self):
        return self.xcor()

    def is_off_screen(self):
        return abs(self.xcor()) > self.horizontal_border

    def reset_ball(self):
        base_heading = self.heading() + 180
        angle_offset = random.uniform(-30, 30)
        new_heading = (base_heading + angle_offset) % 360
        self.home()
        self.move_speed = START_SPEED
        self.setheading(new_heading)
