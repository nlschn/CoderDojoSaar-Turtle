from turtle import *

def koch_einfach(l : int) -> None:
    '''
    Löse hier Aufgabe 5 (a).
    Zeichne hier eine einfache Kochkurve nach dem Bild in der 
    Aufgabenstellung.
    '''
    pass

def koch_rek(l : int, n : int) -> None:
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

def schneeflocke(l : int, n : int, e : int)  -> None:
    for i in range(e):
        koch_rek(l, n)
        right(360 / e)