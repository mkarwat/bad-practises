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
            b += 4 / c 
        else:
            b -= 4 / c
        c += 2
        yield b
