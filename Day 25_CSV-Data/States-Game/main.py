import turtle
import pandas as pd

SCREEN_WIDTH = 725
SCREEN_HEIGHT = 491
STATES_IMAGE = "blank_states_img.gif"
STATES_CSV = "50_states.csv"
TO_LEARN_CSV = "states_to_learn.csv"
TITLE = "U.S. STATES GAME *** Type \"EXIT\" to exit *** Type \"HELP\"  if you get stuck"


class USStatesGame:
    def __init__(self):
        self.screen = self.initialize_screen()
        self.states_dict = self.load_states_data()
        self.remaining_states = set(self.states_dict.keys())
        self.all_states = len(self.remaining_states)
        self.pen = self.initialize_turtle()
        self.correct_guesses = 0
        self.force_exit = False

    def initialize_screen(self):
        screen = turtle.Screen()
        screen.title(TITLE)
        screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        screen.bgpic(STATES_IMAGE)
        return screen

    def load_states_data(self):
        states_data = pd.read_csv("50_states.csv")
        states_data.state = states_data.state.str.lower()
        states_dict = {}
        for index, row in states_data.iterrows():
            states_dict[row.state] = (row.x, row.y)
        return states_dict

    def initialize_turtle(self):
        pen = turtle.Turtle()
        pen.penup()
        pen.hideturtle()
        return pen

    def save_states_to_learn(self):
        caps_states = sorted({state.capitalize() for state in self.remaining_states})
        pd.DataFrame(caps_states).to_csv(TO_LEARN_CSV, index=False)

    def handle_user_input(self):
        title = f"{self.correct_guesses}/{self.all_states} states correct" if self.correct_guesses else "Guess a state!"
        prompt = "Name another state:" if self.correct_guesses else "Name a state:"
        answer = self.screen.textinput(title, prompt)
        return answer.strip().lower() if answer else ""

    def handle_correct_state(self, state):
        self.correct_guesses += 1
        self.remaining_states.remove(state)
        self.pen.goto(self.states_dict[state])
        self.pen.write(state.capitalize())

    def run(self):
        while self.correct_guesses < self.all_states:
            answer = self.handle_user_input()
            if answer == "exit":
                self.force_exit = True
                break
            if answer == "help":
                self.save_states_to_learn()
                self.force_exit = True
                break
            if answer in self.remaining_states:
                self.handle_correct_state(answer)

        turtle.bye() if self.force_exit else self.screen.exitonclick()


if __name__ == "__main__":
    game = USStatesGame()
    game.run()

