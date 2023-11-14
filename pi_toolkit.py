class PiContainer:
    def __init__(self, my_pies: list | None = None) -> None:
        if my_pies is None:
            self.my_pies = []
        else:
            self.my_pies = my_pies

    def add_pi(self, new_pi: float | list[float]) -> None:
        if isinstance(new_pi, list):
            self.my_pies += new_pi  # concatenate list
        elif isinstance(new_pi, float):
            self.my_pies.append(new_pi)
        else:
            raise TypeError('incorrect type')

    @property
    def best(self):
        return self.my_pies[-1]


def calc_pi(approx_level: int):
    """
    pi = a /b +dfh
    :param approx_level
    : return:
    """
    b: float = 0
    c: float = 1
    for idx in range(approx_level):
        if idx % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b


def print_pi(pi: PiContainer):
    for my_pi in pi.my_pies:
        print(my_pi)


if __name__ == "__main__":
    print('All functions are defined')
