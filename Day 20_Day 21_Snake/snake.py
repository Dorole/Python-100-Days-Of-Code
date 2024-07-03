from turtle import Turtle

SNAKE_COLOR = "white"
OFFSET = 20
MOVE_DISTANCE = 20
START_SPEED = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        # lock_movement prevents moving in the opposite direction in case of two keys at the same time
        self.lock_movement = False

    def create_snake(self):
        for i in range(3):
            x_offset = -OFFSET * len(self.snake)
            position = (x_offset, 0)
            self.add_snake_part(position)

    def extend_snake(self):
        position = self.snake[-1].pos()
        self.add_snake_part(position)

    def add_snake_part(self, position):
        snake_part = Turtle(shape="square")
        snake_part.color(SNAKE_COLOR)
        snake_part.speed(START_SPEED)
        snake_part.penup()
        snake_part.goto(position)
        self.snake.append(snake_part)

    def collision_self(self):
        for segment in self.snake[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def move(self):
        target_pos = self.head.pos()
        self.head.forward(MOVE_DISTANCE)
        if self.lock_movement:
            self.lock_movement = False

        for i in range(1, len(self.snake)):
            new_x, new_y = target_pos
            target_pos = self.snake[i].pos()
            self.snake[i].goto(new_x, new_y)

    def up(self):
        if self.head.heading() != DOWN and not self.lock_movement:
            self.head.seth(UP)
            self.lock_movement = True

    def down(self):
        if self.head.heading() != UP and not self.lock_movement:
            self.head.seth(DOWN)
            self.lock_movement = True

    def left(self):
        if self.head.heading() != RIGHT and not self.lock_movement:
            self.head.seth(LEFT)
            self.lock_movement = True

    def right(self):
        if self.head.heading() != LEFT and not self.lock_movement:
            self.head.seth(RIGHT)
            self.lock_movement = True

    def increase_speed(self):
        if self.head.speed() == 10:
            pass
        else:
            current_speed = self.head.speed()
            for segment in self.snake:
                segment.speed(current_speed + 1)
