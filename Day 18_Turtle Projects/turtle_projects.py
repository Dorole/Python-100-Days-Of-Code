import turtle
import random
from random_color_generator import random_color

my_turtle = turtle.Turtle()
my_turtle.hideturtle()
my_turtle.speed("fast")
turtle.colormode(255)


def draw_square():
    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.left(90)


def draw_dashed():
    for _ in range(20):
        my_turtle.forward(10)
        my_turtle.penup()
        my_turtle.forward(10)
        my_turtle.pendown()


def calculate_angle(sides):
    return 360/sides


def shapes():
    nr_sides = 3
    angle = calculate_angle(nr_sides)
    while nr_sides < 11:
        my_turtle.color(random.random(), random.random(), random.random())
        for _ in range(nr_sides):
            my_turtle.forward(100)
            my_turtle.right(angle)
        nr_sides += 1
        angle = calculate_angle(nr_sides)


def shapes_short():
    for i in range(3, 11):
        my_turtle.color(random_color())
        angle = 360/i
        for _ in range(i):
            my_turtle.forward(100)
            my_turtle.right(angle)


def random_walk():
    my_turtle.pensize(10)
    directions = [0, 90, 180, 270]
    for _ in range(0, 200):
        my_turtle.color(random_color())
        my_turtle.setheading(random.choice(directions))
        my_turtle.forward(30)


def draw_spirograph(angle):
    for _ in range(360//angle):
        my_turtle.color(random_color())
        my_turtle.circle(150)
        my_turtle.left(angle)
        # OR:
        # my_turtle.setheading(my_turtle.heading() + angle)


screen = turtle.Screen()
screen.exitonclick()
