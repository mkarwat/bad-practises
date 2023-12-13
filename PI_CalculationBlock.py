class PiContainer:
    def __init__(self, a=None):
        self.a = a if a is not None else []

    def mth(self, x):
        if isinstance(x, list):
            self.a += x
        else:
            self.a.append(x)


def generate_pi_approximations(iterations):
    total = 0
    divisor = 1

    for iteration_number in range(iterations):
        try:
            if iteration_number % 2 == 0:
                total += 4 / divisor
            else:
                total -= 4 / divisor
        except ZeroDivisionError as e:
            yield f'Error: {e}'
        else:
            divisor += 2
            yield total
    yield 'finished'

def enumerate_pi(pi: PiContainer):
    for approximation in pi.a:
        print(f'Next approximation: {approximation}')

if __name__ == '__main__':
    print('All functions are defined')