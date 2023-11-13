class PiContainer:
    def __init__(self, a=None):
        self.a = a if a is not None else []

    def mth(self, x):
        if isinstance(x, list):
            self.a += x
        else:
            self.a.append(x)


def calculate_pi(x):
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


def print_pi_values(pi):
    for hello in pi.a:
        print(f'Next element: {hello}')


try:
    my_pi = PiContainer()
    pi_gen = calculate_pi(5)
    my_pi.mth(next(pi_gen))
    my_pi.mth(next(pi_gen))
    my_pi.mth(next(pi_gen))
    my_pi.mth(next(pi_gen))
    my_pi_2 = PiContainer()
    my_pi.mth(next(pi_gen))
    my_pi.mth(next(pi_gen))
    my_pi.mth(next(pi_gen))
except Exception as e:
    print(f'Something went horribly wrong: {e}')

pi_gen3 = calculate_pi(194)
for _ in range(23):
    my_pi_2.mth(next(pi_gen3))

my_pi_3 = PiContainer()
pi_gen = calculate_pi(6)
my_pi_3.mth(list(pi_gen))

print('My first pi:')
print_pi_values(my_pi)
print('My second pi:')
print_pi_values(my_pi_2)

with open('some-file.txt', 'w') as new_file:
    new_file.write(f'My best pi: {my_pi_3.a[-1]}')

print('Code executed successfully.')
