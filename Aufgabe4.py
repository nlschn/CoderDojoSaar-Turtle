

def go():
   print(pot(2, 10))

def pot(a, b):
    if b > 0:
        return a * pot(a, b - 1)
    else :
        return 1

    