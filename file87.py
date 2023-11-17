class PiContainer:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = elements

    def add(self, item):
        if isinstance(item, list):
            self.elements.extend(item)
        else:
            self.elements.append(item)


def calculate_pi(iterations):
    pi_approximation = 0
    denominator = 1
    for i in range(iterations):
        if i % 2 == 0:
            pi_approximation += 4 / denominator
        else:
            pi_approximation -= 4 / denominator
        denominator += 2
        yield pi_approximation


def print_elements(container):
    for element in container.elements:
        print(element)


if __name__ == "__main__":
    print('All functions are defined')

    # Example usage
    pi_calculator = calculate_pi(10)
    pi_container = PiContainer()
    for approximation in pi_calculator:
        pi_container.add(approximation)

    print_elements(pi_container)
