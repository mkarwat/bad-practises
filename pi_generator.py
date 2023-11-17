class PiContainer:
    def __init__(self, my_pi:list[float]|None=None):
        if my_pi is None:
            self.my_pi = []
        else:
            self.my_pi = my_pi

    def add_pies(self, next_pies):
        if isinstance(next_pies, list) :
            self.my_pi += next_pies
        else:
            self.my_pi.append(next_pies)

    @property
    def best(self):
        return self.my_pi[-1]

def calc_pi(approx_eval):
    ###
    #result = a + b/c ....
    ###
    b = 0
    c = 1
    for i in range(approx_eval):
        if i % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b


def enumerate_pi(pi: PiContainer):
    for my_pi in pi.a:
        print(my_pi)

if __name__ == '__main_':
    print('All functions are defined')