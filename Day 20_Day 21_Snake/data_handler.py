HIGHSCORE_FILE = "data.txt"


def get_highscore():
    with open(HIGHSCORE_FILE) as file:
        try:
            high_score = int(file.read())
        except ValueError:
            high_score = 0
    return high_score


def write_highscore(new_highscore):
    with open(HIGHSCORE_FILE, mode="w") as file:
        file.write(f"{new_highscore}")

