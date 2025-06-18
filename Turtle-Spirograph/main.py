import random

import turtle as tu

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

    
    
t = tu.Turtle()
t.speed("fastest")
tu.colormode(255)

def draw_spirograph(gap):
    for i in range (int(360 / gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + gap)
    
draw_spirograph(10)

screen = tu.Screen()
screen.exitonclick()




