
class piContainer:
    def __init__(self, a=list()):
        self.a = a

    def mth(self, x):
        if type(x) == list:
            self.a += x
        else:
            self.a.append(x)
# this is a important operation in calculating pi that is
# provided in a separate file in this repository,
# please analyse this file before using!
def calculate(x):
    b = 0
    c = 1
    for i in range(x):
        if i % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b
    yield 'finished'
