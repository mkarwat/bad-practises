class PiContainer:
    def __init__(self, values=None):
        if values is None:
            values = list()
        self.a = values

    def mth(self, x):
        if x is list:
            self.a += x
        else:
            self.a.append(x)


def generator(length):
    b = 0
    c = 1
    for hello in range(length):
        if hello % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b


def enumerate_pi(pi: PiContainer):
    for hello in pi.a:
        print(hello)
