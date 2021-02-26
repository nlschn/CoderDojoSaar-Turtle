
def summe_for(n : int) -> int:
    '''
    Berechnet die Summe der ersten n Zahlen iterativ, das heißt mit einer 
    for-Schleife.
    '''
    summe = 0
    for i in range(1, n + 1):
        summe += i
    return summe

def summe_rek(n : int) -> int:
    '''
    Löse hier Aufgabe 4 (a).
    Berechnet die Summe der ersten n Zahlen rekursiv, das heißt durch
    Aufrufen von sich selbst.
    '''
    if n > 0:
        return n + summe_rek(n-1)
    else:
        return 0



def pot_rek(a : int, b : int) -> int:
    '''
    Löse hier Aufgabe 4 (b).
    Berechne "a hoch b" rekursiv. Bedenke dabei: "a hoch 0" ist immer 1.
    '''
    pass
    