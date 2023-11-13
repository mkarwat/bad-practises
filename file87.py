class PiContainer:
    def __init__(self, a=None):
        self.a = a if a is not None else []

    def mth(self, x):
        if isinstance(x, list):
            self.a += x
        else:
            self.a.append(x)


def calculate_pi(x):
    b = 0
    c = 1
    for hello in range(x):
        if hello % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b
    yield 'finished'


def print_pi_values(pi):
    for hello in pi.a:
        print(hello)


print('All functions are defined')
