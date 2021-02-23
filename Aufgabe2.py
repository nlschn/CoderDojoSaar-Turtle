
import turtle

def reset():
    turtle.reset()
    turtle.shape("turtle")
    #turtle.speed(1)

def go():
    a()
    #reset()
    #b()


def a():
    '''
    Zeichne bunt den Namen "Max".
    '''
    # M
    turtle.color("red")

    turtle.left(90)
    turtle.forward(100)

    turtle.right(160)
    turtle.forward(100)

    turtle.left(140)
    turtle.forward(100)

    turtle.right(160)
    turtle.forward(100)

    # A
    turtle.color("green")

    turtle.penup()
    turtle.right(270)
    turtle.forward(20)
    turtle.pendown()

    turtle.left(90)
    turtle.forward(100)

    turtle.right(90)
    turtle.forward(30)

    turtle.right(90)
    turtle.forward(100)

    turtle.penup()
    turtle.right(180)
    turtle.forward(50)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(30)

    turtle.penup()
    turtle.right(180)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(20)
    turtle.pendown()

    # X
    turtle.color("blue")

    turtle.left(45)
    turtle.forward(141)

    turtle.penup()
    turtle.left(135)
    turtle.forward(100)
    turtle.left(135)
    turtle.pendown()

    turtle.forward(141)