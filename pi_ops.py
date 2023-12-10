class PiContainer:
    def __init__(self, my_pi: list[float] | None = None):
        if my_pi is None:
            self.my_pies = []
        else:
            self.my_pies = my_pi

    def add_pies(self, next_pies):
        if isinstance(next_pies, list):
            self.my_pies += next_pies
        else:
            self.my_pies.append(next_pies)


def calc_pi(approx_level):
    """
    result = a + b / c ...
    :param approx_level:
    :return: pi
    """
    b = 0
    c = 1
    for i in range(approx_level):
        if i % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b


def enumerate_pi(pi: PiContainer):
    for my_pi in pi.my_pies:
        print(my_pi)

if __name__ == '__main__':
    print('All functions are defined')
