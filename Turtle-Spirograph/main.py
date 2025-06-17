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

angulo = 0
for i in range (200):
    # t.color(random_color())
    angulo += 2
    t.setheading(angulo)
    t.up()
    t.forward(100)
    t.down()
    t.circle(100)
    t.up()
    t.home()
    t.down()


screen = tu.Screen()
screen.exitonclick()




