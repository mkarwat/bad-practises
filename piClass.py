class PiClass:
    def __init__(self, value : list[float] | None = None):
        if value is None:
            self.value = []
        else:
            self.value = value

    def appendPi(self, valuePi):
        if isinstance(valuePi, list):
            self.value += valuePi
        else:
            self.value.append(valuePi)

    @property
    def best(self):
        return self.value[-1]

    def enumerate(self):
        for pi_es in self.value:
            print(pi_es)

def calculatePi(level):    
    b = 0
    c = 1
    for _ in range(level):
        if _ % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b    


if __name__ == '__main__':
    print('All functions are defined')
