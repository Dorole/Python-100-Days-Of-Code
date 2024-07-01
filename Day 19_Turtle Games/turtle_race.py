import turtle
import random


class TurtleRace:
    def __init__(self):
        self.colors = ["red", "blue", "green", "orange", "purple", "pink"]
        self.screen = self.create_screen(width=500, height=744)
        self.X_COORD = -230
        self.turtles = self.create_turtles(6)
        self.winner = ""

    def create_turtles(self, num):
        y_coord = -325
        all_turtles = []
        for _ in range(num):
            turtle_racer = turtle.Turtle(shape="turtle")
            turtle_racer.shapesize(1.5, 1.5, 1.0)
            this_color = self.colors[random.randint(0, len(self.colors)-1)]
            turtle_racer.color(this_color)
            self.colors.remove(this_color)
            turtle_racer.penup()
            turtle_racer.goto(self.X_COORD, y_coord)

            all_turtles.append(turtle_racer)
            y_coord += 130
        return all_turtles

    def create_screen(self, width, height):
        screen = turtle.Screen()
        screen.bgpic("racetrack.png")
        screen.setup(width, height)
        return screen

    def move_turtles(self, max_distance):
        has_won = False
        while not has_won:
            random.shuffle(self.turtles)
            for t in self.turtles:
                t.forward(random.randint(0, max_distance))
                if t.xcor() > -self.X_COORD:
                    has_won = True
                    self.winner = t.pencolor()
                    break

    def run_race(self):
        user_bet = self.screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? "
                                                                        "Enter a color: ").lower()
        self.move_turtles(max_distance=10)

        print(f"{self.winner.capitalize()} is the winner!")
        if self.winner == user_bet:
            print("You won the bet!")
        else:
            print("You lost the bet!")

        self.screen.exitonclick()
