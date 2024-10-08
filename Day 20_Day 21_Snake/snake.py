from turtle import Turtle

SNAKE_COLOR = "white"
OFFSET = 20
MOVE_DISTANCE = 20
START_SPEED = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POOL_SIZE = 4


class Snake:
    def __init__(self):
        self.snake_parts = self.create_pool()
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        # lock_movement prevents moving in the opposite direction in case of two keys at the same time
        self.lock_movement = False

    def create_pool(self):
        snake_parts = []
        for i in range(POOL_SIZE):
            snake_part = self.create_snake_part((0, 0))
            snake_parts.append(snake_part)
        return snake_parts

    def get_item_from_pool(self, position):
        snake_part = self.snake_parts[0]
        self.snake_parts.pop(0)
        snake_part.goto(position)
        snake_part.showturtle()
        return snake_part

    def return_to_pool(self, snake_part):
        snake_part.hideturtle()
        snake_part.home()
        self.snake_parts.append(snake_part)

    def create_snake(self):
        for i in range(3):
            x_offset = -OFFSET * len(self.snake)
            position = (x_offset, 0)
            snake_part = self.get_item_from_pool(position)
            self.snake.append(snake_part)

    def extend_snake(self):
        position = self.snake[-1].pos()
        if len(self.snake_parts) == 0:
            self.snake_parts.append(self.create_snake_part((0, 0)))
        snake_part = self.get_item_from_pool(position)
        self.snake.append(snake_part)

    def create_snake_part(self, position):
        snake_part = Turtle(shape="square")
        snake_part.color(SNAKE_COLOR)
        snake_part.speed(START_SPEED)
        snake_part.penup()
        snake_part.goto(position)
        snake_part.hideturtle()
        return snake_part

    def reset_snake(self):
        for part in self.snake:
            self.return_to_pool(part)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

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
