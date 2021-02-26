
import turtle

def reset():
    turtle.reset()
    turtle.shape("turtle")
    #turtle.speed(1)

def go():
    pass


def a():
    '''
    Zeichne die Buchstaben "MK" in bunt.
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

    # Leerzeichen    
    turtle.penup()
    turtle.right(270)
    turtle.forward(20)
    turtle.pendown()

    # K
    turtle.color("green")
    turtle.left(90)
    turtle.forward(100)    
    turtle.left(180)
    turtle.forward(50)
    turtle.left(45)
    turtle.forward(72)
    turtle.right(180)
    turtle.forward(72)
    turtle.right(90)
    turtle.forward(72)
    
def b():
    pass