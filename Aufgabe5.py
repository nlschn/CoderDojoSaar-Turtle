from turtle import *

def go():
    speed(0)
    schneeflocke(50, 4, 3)
    input()


def schneeflocke(l, n, e):
    for i in range(e):
        koch_rek(l, n)
        right(360 / e)



def koch(l, n):
    koch_rek(l, n)

def koch_einfach(l):
    forward(l)
    left(60)
    forward(l)
    right(120)
    forward(l)
    left(60)
    forward(l)


def koch_rek(l, n):
    if n <= 1:
        koch_einfach(l)
        return

    koch_rek(l / 3, n - 1)
    left(60)
    koch_rek(l / 3, n - 1)
    right(120)
    koch_rek(l / 3, n - 1)
    left(60)
    koch_rek(l / 3, n - 1)
