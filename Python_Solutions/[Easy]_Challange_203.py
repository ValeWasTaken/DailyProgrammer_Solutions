import turtle

def drawSquare():
    turtle.color("pink")
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
drawSquare()
