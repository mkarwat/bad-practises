class PiContainer:
    def __init__(self, piValue : list[float] | None = None):
        if piValue is None:
            self.piValue = []
        else:
            self.piValue = piValue

    def add_pi(self, pi):
        if isinstance(pi, list):
            self.piValue += pi
        else:
            self.piValue.append(pi)

    def enumerate_pi(self):
        for pi in self.piValue:
            print(f"Next element: {pi}")

    @property
    def best_approx(self):
        return self.piValue[-1]


def calculate_pi(aproxLevel):
    b = 0
    c = 1
    for hello in range(aproxLevel):
        if hello % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b


if __name__ == '__main__':
    print('All functions are defined')