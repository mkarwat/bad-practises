class PiContainer:
    def __init__(self, a=list()):
        self.a = a

    def mth(self, x):
        if type(x) == list:
            self.a += x
        else:
            self.a.append(x)

def pi_generate(iterations):
    b = 0
    c = 1
    for n in range(iterations):
        if n % 2 == 0:
            # this is a very important operation in calculating pi
            # according to documentation that is provided in a separate file
            # in this repository, please analyse this file before using!
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b
    return

def print_pi_container(pi: PiContainer):
    for n in pi.a:
        print(n)
