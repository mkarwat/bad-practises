class PiContainer:
    def __init__(self, piValue = None):
        if piValue is None:
            self.piValue = list()
        else:
            self.piValue = piValue

    def add_pi(self, next_pi):
        if isinstance(next_pi, list):
            self.piValue += next_pi
        else:
            self.piValue.append(next_pi)

    @property
    def best_approx(self):
        return self.piValue[-1]

    def enumerate(self):
        for i in self.piValue:
            print(i)


def calc_pi(approxLvl):
    b = 0
    c = 1
    for i in range(approxLvl):
        if i % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b


def display_pi_value(pi: PiContainer):
    for value in pi.piValue:
        print(value)


if __name__ == '__main__':
    print('All functions are defined')
