import time
from window import Window
from snake import Snake
from food import Food
from scoreboard import Scoreboard

window = Window()
screen = window.get_screen()
snake = Snake()
food = Food(screen)
scoreboard = Scoreboard(screen)

binding_dictionary = {
    "Up": snake.up,
    "Down": snake.down,
    "Left": snake.left,
    "Right": snake.right
}

screen.listen()
for key in binding_dictionary:
    screen.onkeypress(binding_dictionary[key], key)

OFFSET = 10
x_collision = window.x_border - OFFSET
y_collision = window.y_border - OFFSET


def wall_collision():
    if (snake.head.xcor() > x_collision or snake.head.xcor() < -x_collision or snake.head.ycor()
            > y_collision or snake.head.ycor() < -y_collision):
        return True
    else:
        return False


def check_food_collection():
    if snake.head.distance(food) < 25:
        snake.extend_snake()
        food.spawn()
        scoreboard.increase_score()
        check_speed_increase()


def check_speed_increase():
    if scoreboard.score > 0 and scoreboard.score % 10 == 0:
        snake.increase_speed()


def check_game_over():
    if wall_collision() or snake.collision_self():
        scoreboard.game_over()
        return True
    else:
        return False


# ************* GAME LOOP *************
play = True
while play:
    screen.update()
    time.sleep(0.1)
    snake.move()
    check_food_collection()
    if check_game_over():
        play = False


screen.exitonclick()
