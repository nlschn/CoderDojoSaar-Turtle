from turtle import *

farben = ["red", "green", "blue", "orange", "brown", "purple"]


def zeichnen() -> None:
    '''
    Zeichnet das Fibonacci-Bild mit den Quadraten und der Fibonacci-Kurve.
    '''
    # Erhöhe die Geschwindigkeit der Turtle.
    speed(0.01)

    # Zeichne zuerst die Quadrate.
    quadrate(15, 20)  
    
    # Zurück zur Mitte ohne zu zeichnen.
    penup()
    goto(0, 0)
    pendown()
    
    # Zeichne dann die Kurve.
    kurve(15, 20)


def naechste_farbe(i : int) -> None:
    '''
    Setzt die Farbe der Turtle auf die i-te Farbe aus der Liste 'farben'.
    '''
    color(farben[i % len(farben)])

def fib_rek(n : int) -> int:
    '''
    Löse hier Aufgabe 6 (a).
    Berechne die n-te Fibonacci-zahl rekursiv.
    '''
    if n <= 1:
        return 1
    else:
        return fib_rek(n - 1) + fib_rek(n - 2)


def quadrat(l : int) -> None:  
    '''
    Löse hier Aufgabe 6 (b).
    Zeichne ein Quadrat der Seitenlänge l beginnend mit der aktuellen
    Blickrichtung.
    '''
    pass

def quadrate(n : int, l : int) -> None:
    '''
    Löse hier Aufgabe 6 (c).
    Zeichne die Fibonacci-Quadrate.
    '''
    pass


def kurve(n : int, l : int) -> None:
    '''
    Löse hier Aufgabe 6 (d).
    Zeichne die Fibonacci-Kurve.
    '''
    pass