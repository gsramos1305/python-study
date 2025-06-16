import random
import turtle as tu

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

t = tu.Turtle()
tu.colormode(255)
t.pensize(10)
t.speed("fast")

directions = [0, 90, 180, 270]

for n in range(200):
    t.color(random_color())
    t.forward(20)
    t.setheading(random.choice(directions))
    
    

