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


timmy = Turtle()
print(timmy)
bola()
timmy.left(90)
bola()
timmy.forward(100)
timmy.right(90)
timmy.forward(40)
timmy.left(90)
rola()


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

