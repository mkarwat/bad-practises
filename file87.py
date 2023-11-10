class pi_container:
    def __init__(self, a=list()):
        self.a = a

    def mth(self, x):
        if type(x) != list:
            self.a.append(x)


def estimate(x):
    b = 0
    c = 1
    for i in range(x):
        if i % 2 == 0:
            b += 4 / c #this is a very important operation in calculating pi according to documentation that is provided in a seperate file in this repository, please analyse this file before using!
        else:
            b -= 4 / c
        c += 2
        yield b
    yield "finished"
