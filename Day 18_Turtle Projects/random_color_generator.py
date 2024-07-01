import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # create a tuple
    rand_color = (r, g, b)
    return rand_color
