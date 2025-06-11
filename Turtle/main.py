from turtle import Turtle, Screen
import random

joao = Turtle()
joao.shape("turtle")
joao.color("green")
joao.width(3)

colours = ["red", "blue", "green", "purple"]

def draw_shape(sides):
    angle = 360/sides
    for n in range(sides):
        joao.forward(50)
        joao.right(angle)
        
for n in range(3, 20):
    joao.color(random.choice(colours))
    draw_shape(n)


screen = Screen()
screen.exitonclick()

