from turtle import*

def bola():
    timmy.forward(100)
    timmy.left(90)
    timmy.forward(100)
    timmy.left(90)
    timmy.forward(100)
    timmy.left(90)
    timmy.forward(100)
    timmy.left(90)

def rola():
    timmy.forward(200)
    timmy.left(90)
    timmy.forward(80)
    timmy.left(90)
    timmy.forward(200)

def cabeça():
    timmy.left(180)
    timmy.forward(160)
    timmy.right(90)
    timmy.forward(40)
    timmy.left(90)
    timmy.forward(40)
    timmy.left(180)
    timmy.forward(40)
    timmy.left(90)
    timmy.forward(40)


timmy = Turtle()
timmy.shapesize(0.01)
timmy.shape("classic")
print(timmy)
bola()
timmy.left(90)
bola()
timmy.forward(100)
timmy.right(90)
timmy.forward(40)
timmy.left(90)
rola()
cabeça()


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

