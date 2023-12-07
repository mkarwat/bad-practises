class PiContainer:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = elements

    def add(self, item):
        if isinstance(item, list):
            self.elements += item
        else:
            self.elements.append(item)


def approximate_pi(iterations):
    pi_approximation = 0
    denominator = 1
    for step in range(iterations):
        if step % 2 == 0:
            pi_approximation += 4 / denominator
        else:
            pi_approximation -= 4 / denominator
        denominator += 2
        yield pi_approximation
    yield 'finished'

def display_values(container: PiContainer):
    for value in container.elements:
        print(value)


print('All functions are defined')

# Example usage:
# container = PiContainer()
# for approximation in approximate_pi(1000):
#     container.add(approximation)
# display_values(container)
