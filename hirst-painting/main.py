import colorgram
import turtle as t
import random

tu = t.Turtle()
tu.speed('fastest')
tu.width(1)
t.colormode(255)



def center_grid(radius, circles_per_line, height):
    spacing = radius * 2 * 1.5
    total_width = circles_per_line * spacing
    total_height = height * spacing

    start_x = -total_width / 2
    start_y = total_height / 2

    tu.penup()
    tu.goto(start_x, start_y)

def next_line(radius, height):
    tu.home()
    tu.left(90)
    # tu.forward(radius)
    tu.forward(((radius * 2) * 1.50) * (height))
    tu.right(90)

def paint(radius, circles_per_line, height):
    spacing = radius * 2 * 1.5
    total_width = circles_per_line * spacing
    total_height = height * spacing

    start_x = -total_width / 2
    start_y = total_height / 2

    tu.penup()
    tu.goto(start_x, start_y)

    for row in range(height):
        for col in range(circles_per_line):
            tu.dot(radius, random.choice(rgb_colors))
            tu.forward(spacing)
        # Move to next row
        tu.backward(spacing * circles_per_line)
        tu.right(90)
        tu.forward(spacing)
        tu.left(90)


# def paint(radius, circles_per_line, height):
#     for n in range(1, height + 1):
#         for _ in range(circles_per_line):
#             tu.setheading(0)
#             tu.down()
#             tu.dot(radius, random.choice(rgb_colors))
#             tu.up()
#             tu.forward((radius * 2) * 1.50)
#         next_line(radius, n)
        



rgb_colors = []
colors = colorgram.extract('hirst-painting/test.jpg', 25)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

radius = int(input("Radius: "))
dots_per_line = int(input("Dots per line: "))
height = int(input("Height: "))

center_grid(radius, dots_per_line, height)
paint(radius, dots_per_line, height)

screen = t.Screen()
screen.exitonclick()