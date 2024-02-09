import random
from turtle import *
import turtle as t
tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

# Make square shape
# x = 0
# while x < 4:
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(100)
#     x += 1

# Make dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.color("white")
#     tim.forward(10)
#     tim.color("black")

# Make sharp for 4 - 8
# for i in range(4,9):
#     for _ in range(i):
#         angle = 360 / i
#         tim.forward(100)
#         tim.right(angle)

# Make sharp and change color
# colors  = ["red","green","blue","orange","purple","pink","yellow"] # Make a list of colors to picvk from
# def draw_sharpe(num_sides):
#     angle = 360 / num_sides
#     color = random.choice(colors)
#     tim.color(color)
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     draw_sharpe(shape_side_n)

# Random Walking
# degrees = [90, 180, 0, 270]
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
#            "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# for _ in range(200):
#     directions = [tim.right, tim.left]
#     set_direction = (random.choice(directions))
#     set_direction(random.choice(degrees))
#     tim.color(random.choice(colours))
#     tim.pensize(5)
#     tim.speed(10)
#     tim.forward(30)

screen = Screen()
screen.exitonclick()
