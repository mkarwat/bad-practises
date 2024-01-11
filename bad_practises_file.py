class PiContainer: # pi_container -> PiContainer
    def __init__(self, a=list()):
        self.a = a

    def mth(self, x):
        if type(x) == list:
            self.a += x
        else:
            self.a.append(x)

def foo(x):
    b = 0
    c = 1
    for hello in range(x):
        if hello % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
            c += 2
        yield b
    yield 'finished'

def print_pi(pi)
    for hello in pi.a:
        print(hello)

print('All functions are defined')








# git push --set-upstream origin 01-JB-JR
# git config push.default current