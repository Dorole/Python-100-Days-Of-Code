import window
import time
import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

window_o = window.Window()
screen = window_o.screen
root = screen.getcanvas().winfo_toplevel()

paddle_start_x = (window.SCREEN_WIDTH/2) - window.PADDLE_OFFSET
right_paddle = Paddle(start_x=paddle_start_x, window=window_o)
left_paddle = Paddle(start_x=-paddle_start_x, window=window_o)

ball = Ball(start_x=0, start_y=0, window=window_o)

screen.onkeypress(fun=right_paddle.move_up, key="Up")
screen.onkeypress(fun=right_paddle.move_down, key="Down")
screen.onkeypress(fun=left_paddle.move_up, key="w")
screen.onkeypress(fun=left_paddle.move_down, key="s")

scoreboard = Scoreboard()


def on_close():
    global play
    play = False


screen.onkeypress(fun=on_close, key="Escape")
root.protocol("WM_DELETE_WINDOW", on_close)

play = True
while play:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()
    if ball.check_wall_collision():
        continue

    if ball.is_ball_screen_right():
        if ball.check_paddle_collision(right_paddle):
            continue
    else:
        if ball.check_paddle_collision(left_paddle):
            continue

    if ball.is_off_screen():
        if ball.is_ball_screen_right():
            scoreboard.update_l_score()
        else:
            scoreboard.update_r_score()
        ball.reset_ball()
        screen.update()
        time.sleep(1)

    if scoreboard.check_game_end():
        scoreboard.display_game_end()
        screen.update()
        play = False

    if not play:
        break

turtle.bye()
