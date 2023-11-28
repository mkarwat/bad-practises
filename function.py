class PiContainer:
    def __init__(self, my_pi=None):
        if my_pi is None:
            my_pi = []
        self.my_pi = my_pi

    def add_pi(self, next_pi):
        if isinstance(next_pi,list):
            self.my_pi += next_pi
        else:
            self.my_pi.append(next_pi)


def calculate_pi(approximation_level):
    pi_approximation = 0
    denominator=1
    for i in range(approximation_level):
        if i % 2 == 0:
            pi_approximation += 4 / denominator
        else:
            pi_approximation -= 4 / denominator
        denominator += 2
        yield pi_approximation

def print_pi(pi: PiContainer):
    for value in pi.my_pi:
        print(value)

if __name__ == "__main__":
    print('All functions are defined')
