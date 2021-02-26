

def go():
    print(summe_for(100))
    print(summe_rek(100))

def summe_for(n):
    summe = 0
    for i in range(1, n + 1):
        summe += i
    return summe

def summe_rek(n):
    if n > 0:
        return n + summe_rek(n-1)
    else:
        return 0

