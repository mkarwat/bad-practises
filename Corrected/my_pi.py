class PiContainer:
    def __init__(self, my_pies: list[float] | None = None):
        if my_pies is None:
            self.my_pies = list()
        else:
            self.my_pies = my_pies

    def add_pi(self, next_pi: list[float] | float) -> None:
        if isinstance(next_pi, list):
            self.my_pies += next_pi
        else:
            self.my_pies.append(next_pi)

    @property
    def best(self):
        return self.my_pies[-1

        ]
def calc_pi(approx_level: int):
    """
    pi = a/b+c...
    :param approx_level:
    :return:
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
    for next_pi in pi.my_pies:
        print(next_pi)


if __name__ == '__main__':

    print('All functions are defined')
