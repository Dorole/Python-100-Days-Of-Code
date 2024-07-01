import turtle
import random

my_turtle = turtle.Turtle()
turtle.colormode(255)
my_turtle.speed("fastest")

colors = [(237, 251, 245), (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188),
          (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (244, 39, 149),
          (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16),
          (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

START_COORD = -250
END_COORD = 250


def get_random_color():
    return colors[random.randint(0, len(colors)-1)]


def generate_painting(dot_radius, dot_distance):
    my_turtle.hideturtle()
    for y in range(START_COORD, END_COORD, dot_distance):
        for x in range(START_COORD, END_COORD, dot_distance):
            my_turtle.teleport(x, y)
            my_turtle.dot(dot_radius, get_random_color())


generate_painting(dot_radius=20, dot_distance=50)

screen = turtle.Screen()
screen.exitonclick()
