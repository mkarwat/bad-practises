
class PiContainer:
    def __init__(self, piVal : list[float] | None = None):
        if piVal is None:
            self.piVal = []
        else:
            self.piVal = piVal

    def add_pi(self, pi):
        if isinstance(pi, list):
            self.piVal += pi
        else:
            self.piVal.append(pi)

    def enumerate_pi(self):
        for pi in self.piVal:
            print(f"Next elem: {pi}")

    @property
    def best_approx(self):
        return self.piVal[-1]


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
