
class PiContainer:
    def __init__(self) -> None:
        self.a = []

    def add_pi(self, x):
        if isinstance(x, list):
            self.a += x
        else:
            self.a.append(x)


def calculate_pi(x):
    b = 0
    c = 1
    for i in range(x):
        if i % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b


def enum_pi(pi: PiContainer):
    for i in pi.a:
        print(i)


if __name__ == "__main__":
    print('All functions are defined')
