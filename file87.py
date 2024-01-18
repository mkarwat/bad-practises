
class pi_container:
    def __init__(self, a=list()):
        self.a = a

    def mth(self, x):
        if type(x) == list:
            self.a += x
        else:
            self.a.append(x)


def foo(x):
    b = 0
    c=1
    for hello in range(x):
        if hello % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b
    yield 'finished'

def enumerate(pi: pi_container):
    for approx in pi.a:
        print(approx)


print('All functions are defined')
