class PiContainer:
    def __init__(self, my_pies: list | None = None) -> None:
        if my_pies is None:
            self.my_pies = list()
        else:
            self.my_pies = my_pies

    def add_pi(self, next_pi: float | list[float]) -> None:
        if isinstance(next_pi, list):
            self.my_pies += next_pi  # concatenate list
        elif isinstance(next_pi, float):
            self.my_pies.append(next_pi)
        else:
            raise TypeError('incorrect type')

    @property
    def best(self):
        return self.my_pies[-1]

    def enumarate_pi(self):
        for my_pi in self.my_pies:
            print(my_pi)

def calc_pi(approx):
    b = 0
    c = 1
    for idx in range(approx):
        if idx % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b


if __name__ == "__main__":
    print('All functions are defined')
