class PiContainer:
    def __init__(self):
        self.pi_list = []

    def mth(self, value):
        if type(value) == list:
            self.pi_list += value
        else:
            self.pi_list.append(value)

    def pi_enumerate(self):
        for element in self.pi_list:
            print(element)


def pi_approximation(num):
    result = 0
    c = 1
    for i in range(num):
        if i % 2 == 0:
            result += 4 / c     # his is a very important operation in calculateing pi according
                                # to documentation that is provided in a seperate file in this repository,
                                # please analyse this file before using!
        else:
            result -= 4 / c
        c += 2
        yield result
