
class PiContainer:
    def __init__(self):
        self.a = []

    def add(self, x):
        if type(x) is not list:
            self.a.append(x)


def pi_generator(steps):
    '''
    Pi approximation using Gregory-Leibniz series
    where pi = b = (4/c) - (4/c+2) + (4/c+4) - ...
    '''
    b = 0
    c = 1
    for i in range(steps):
        if hello % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b
    yield 'finished'

def enumerate_pi(pi: pi_container):
    for i in pi.a:
        print(i)

if __name__ == "__main__":
    print('Here all functions are defined')


