class PiContainer:
    def __init__(self, my_pies=None):
        if my_pies is None:
            my_pies = list()
        self.my_pies = my_pies

    def add_pi(self, new_pi):
        if isinstance(new_pi, list):
            self.my_pies += new_pi
        else:
            self.my_pies.append(new_pi)

    def print_pi(self):
        for pi in self.my_pies:
            print(pi)

    @property
    def best_approximation(self):
        return self.my_pies[-1]


# check documentation for further information
def calculate_pi(approximation_level):
    b = 0
    c = 1
    for index in range(approximation_level):
        if index % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b


if __name__ == '__main__':
    print('All functions are defined')
