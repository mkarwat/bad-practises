class PiContainer:
    def __init__(self, pi_val=list()):
        self.pi_val = pi_val

    def append_container(self, x):
        if type(x) == list:
            self.pi_val += x
        else:
            self.pi_val.append(x)

    def enumerate(self):
        for i in self.pi_val:
            print(f'Next element: {i}')

    @property
    def best_approx(self):
        return self.pi_val[-1]

# For further information refer to 'PiDocummentation' located in repository directory
def leibniz_pi_generator(approximation_level):
    b = 0
    c = 1
    for i in range(approximation_level):
        if i % 2 == 0:
            # According to 'PiDocummentation' 5.1
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b

