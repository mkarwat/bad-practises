from typing import List, Optional


class PiContainer:
    def __init__(self, my_pies: Optional[List[float]] = None):
        if my_pies is None:
            self.my_pies = []
        else:
            self.my_pies = my_pies

    def mth(self, next_pi):
        if isinstance(next_pi, list):
            self.my_pies += next_pi
        else:
            self.my_pies.append(next_pi)

    @property
    def best(self):
        return self.my_pies[-1]


def calc_pi(approx_level):
    """
    result = a + b /c
    :param approx_level
    :return pi
    """
    b = 0
    c = 1
    for index in range(approx_level):
        if index % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b


def enumerate_pi(pi: PiContainer):
    for index in pi.my_pies:
        print(index)


if __name__ == '__main__':
    print('All functions are defined')