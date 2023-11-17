class PiContainer:
    def __init__(self, pi_val=None):
        if pi_val is None:
            pi_val = list()
        self.pi_val = pi_val

    def append_container(self, x):
        if isinstance(x, list):
            self.pi_val += x
        else:
            self.pi_val.append(x)

    def enumerate(self):
        for i in self.pi_val:
            print(f'Next element: {i}')


def pi_generator(x):
    b = 0
    c = 1
    for i in range(x):
        if i % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b
