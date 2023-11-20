from typing import List


class PiContainer:
    def __init__(self, my_pies: List[float] or None = None):
        if my_pies is None:
            self.my_pies = []
        else:
            self.my_pies = my_pies

    def more_pies(self, next_pi):
        if isinstance(next_pi, list):
            self.my_pies += next_pi
        else:
            self.my_pies.append(next_pi)

    @property
    def best(self):
        return self.my_pies[-1]

    def enumerate_me(self):
        for my_pi in self.my_pies:
            print(my_pi)


def calc_pi(approx_level):
    """
    Calculate an approximation of pi using the Leibniz formula for pi.

    The Leibniz formula for pi is given by the alternating series:
    pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - ...

    Parameters:
    - approx_level (int): The number of iterations to perform for the approximation.

    Returns:
    - generator: A generator that yields successive approximations of pi as the number of iterations increases.

    Variables:
    - b (float): Running total in the series.
    - c (int): Denominator of the fractions in the series.
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


if __name__ == '__main__':
    print('All functions are defined')
