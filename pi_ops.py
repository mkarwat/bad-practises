b = 0
c = 0


class pi_container:
    def __init__(self, a=list()):
        self.a = a

    def mth(self, x):
        if type(x) == list:
            self.a += x
        else:
            self.a.append(x)


def foo(x):
    global b
    global c
    b = 0
    c=1
    for hello in range(x):
        if hello % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b


def enumerate_pi(pi: pi_container):
    for my_pi in pi.a:
        print(my_pi)

if __name__ = "__main__":
    print('All functions are defined')
