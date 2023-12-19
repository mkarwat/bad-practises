class PiContainer:
    def __init__(self, a = None):
        self.a = a if a is not None else []

    def mth(self, x):
        if isinstance(x, list):
            self.a += x
        else:
            self.a.append(x)

# Calculate pi value
def calculatePi(x):

    '''
    Wzór:
    b: Opis zmiennej b
    c: Opis zmiennej c

    miejsce na wzór 
    
    dodatkowe informacje
    '''
    
    b = 0
    c = 1
    for hello in range(x):
        if hello % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b

# Printing element with preamble
def printElements(pi):
    for x in pi.a:
        print(f"Next element: {x}")

# Printing only values
def enumarate(pi):
    for x in pi.a:
        print(x)
