import colorgram
import turtle as t
import random

tu = t.Turtle()
tu.speed('fastest')
tu.width(1)
t.colormode(255)




def next_line(radius, height):
    tu.home()
    tu.left(90)
    # tu.forward(radius)
    tu.forward(((radius * 2) * 1.50) * (height))
    tu.right(90)

def paint(radius, circles_per_line, height):
    for n in range(1, height + 1):
        for _ in range(circles_per_line):
            tu.setheading(0)
            tu.down()
            tu.dot(radius, random.choice(rgb_colors))
            tu.up()
            tu.forward((radius * 2) * 1.50)
        next_line(radius, n)
        



rgb_colors = []
colors = colorgram.extract('hirst-painting/test.jpg', 25)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

color = random.choice(rgb_colors)
print(color)

paint(15, 5, 5)

screen = t.Screen()
screen.exitonclick()