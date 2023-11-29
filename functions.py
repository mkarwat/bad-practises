class PiContainer:
    def __init__(self, values=None):
        if values is None:
            values = []
        self.values = values

    def addnewpositions(self, valuetoadd):
        if type(valuetoadd) == list:
            self.values += valuetoadd
        else:
            self.values.append(valuetoadd)


def piexpander(numofexp):
    b = 0
    c = 1
    for x in range(numofexp): #read attached documentation before use
        if x % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b
    #yield 'finished'


def enumerate(pi):
    for element in pi.values:
        print(f'Next element: {element}')



