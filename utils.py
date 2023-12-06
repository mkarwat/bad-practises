class PiContainer:
    def __init__(self):
        self.a = []

    def mth(self, x):
        if type(x) == list:
            self.a += x
        else:
            self.a.append(x)


def foo(x):
    b = 0
    c = 1
    for i in range(x):
        if i % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b


def my_enumerate(pi: PiContainer):
    for element in pi.a:
        print(element)


#print('All functions are defined')

