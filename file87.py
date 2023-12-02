class PiContainer:
    def __init__(self, a=None):
        self.a = a if a is not None else []

    def add_values(self, x):
        if type(x) == list:
            self.a += x
        else:
            self.a.append(x)


def calculate_pi(x):
    b = 0
    c = 1
    for hello in range(x):
        if hello % 2 == 0:
            b += 4 / c  # this is a very important operation in calculateing pi according to documentation that is
            # provided in a seperate file in this repository, please analyse this file before using!
        else:
            b -= 4 / c
        c += 2
        yield b
    yield 'finished'


def print_values(pi: PiContainer):
    for value in pi.a:
        print(value)


if __name__ == "__main__":
    print('All functions are defined')