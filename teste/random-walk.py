import random
from turtle import Turtle, Screen

t = Turtle()

directions = [0, 90, 180, 270]

for n in range(200):
    t.setheading(random.choice(directions))
    t.forward(10)
    





my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

