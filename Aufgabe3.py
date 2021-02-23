from turtle import *

def reset():
    shape("turtle")
    speed(100)

farben = ["red", "green", "blue", "yellow", "brown", "purple"]


def go():
    reset()
    pensize(2)
    bgcolor("black")

    for r in range(2, 150, 5):
        hex(r)
        right(10)




def hex(r):
    penup()
    left(60)
    forward(r)
    right(120)
    pendown()

    for c in range(6):
        color(farben[c])
        forward(r)
        right(60)

    penup()
    right(60)
    forward(r)
    left(120)
    pendown()