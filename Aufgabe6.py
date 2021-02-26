from turtle import *

farben = ["red", "green", "blue", "orange", "brown", "purple"]


def go():
    speed(0)

    # Zuerst die Quadrate.
    quadrate(15, 10)  
    
    # Zurück zur Mitte ohne zu zeichnen.
    penup()
    goto(0, 0)
    pendown()

    # Dann die Kurve.
    kurve(15, 10)


    input()

def naechste_farbe(i):
    color(farben[i % len(farben)])

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def quadrat(l):  
    begin_fill()
    for i in range (4):        
        forward(l)
        left(90)
    end_fill()

def quadrate(n, s):
    for i in range (n):
        naechste_farbe(i)

        f = fib(i)
        quadrat(s * f)
        forward(s * f)
        left(90)
        forward(s * f)


def kurve(n, s):
    color("white") 
    pensize(3)
    left(90)
    for i in range(n):
        f = fib(i)
        circle(s * f, 90)
      
        