from turtle import Turtle, Screen

tu = Turtle()
tu.width(3)
# tu.speed('fastest')
tu.up()
tu.right(135)
tu.forward(300)
tu.setheading(0)
tu.down()

def bola():
    tu.circle(100)
    tu.up()
    tu.forward(200)
    tu.down()
    tu.circle(100)

def corpo():
    tu.setheading(90)
    tu.forward(300)
#terminar corpo

bola()
tu.up()
tu.backward(200)
tu.left(90)
tu.fd(100)
tu.right(20)
tu.fd(100)
tu.down()
corpo()


screen = Screen()
screen.exitonclick()