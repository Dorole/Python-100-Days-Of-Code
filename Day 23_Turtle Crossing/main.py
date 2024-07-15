from display import Display
from player import Player
from car_manager import CarManager
from level_manager import LevelManager
from countdown import Countdown
from message import Message
import time
import turtle

POS_OFFSET = 20

display = Display()
screen = display.screen
root = screen.getcanvas().winfo_toplevel()
car_manager = CarManager()
level_manager = LevelManager()
player = Player(display.borders["bottom"] + POS_OFFSET)
countdown = Countdown()
message = Message()

screen.onkeypress(fun=player.move_player, key="Up")
screen.onkeypress(fun=player.move_player, key="w")


def next_level():
    car_manager.on_level_clear()
    player.reset_player()
    countdown.reset_countdown()
    level_manager.level_up()


def game_clear():
    car_manager.on_level_clear()
    player.reset_player()
    message.game_end()


def on_close():
    global play
    play = False


root.protocol("WM_DELETE_WINDOW", on_close)
screen.onkey(fun=on_close, key="Escape")

play = True
screen.update()
while play:
    time.sleep(0.1)
    screen.update()

    if not player.should_move and countdown.finished:
        player.should_move = True
        player.show_self()
    elif not player.should_move and not countdown.finished:
        countdown.display_countdown(time.time())

    car_manager.release_cars(time.time())
    car_manager.move_cars()
    car_manager.try_requeue_car()

    if car_manager.check_collision(player):
        message.game_over()
        screen.update()
        play = False

    if player.get_y_cor() > display.borders["top"]:
        if level_manager.check_game_end():
            game_clear()
            screen.update()
            play = False
        else:
            next_level()

    if not play:
        break

turtle.bye()

