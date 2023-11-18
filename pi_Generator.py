class PiContainer:
    def __init__(self, pi_values: list[float] = None):
        self.pi_values = pi_values if pi_values is not None else []

    def add_pi_values(self, new_values):
        if isinstance(new_values, list):
            self.pi_values.extend(new_values)
        else:
            self.pi_values.append(new_values)

    @property
    def latest_pi(self):
        return self.pi_values[-1] if self.pi_values else None

def calculate_pi(approximation_level: int):
    numerator = 4
    denominator = 1
    pi_approximation = 0
    for i in range(approximation_level):
        pi_approximation += numerator / denominator if i % 2 == 0 else -numerator / denominator
        denominator += 2
        yield pi_approximation

def display_pi_values(container: PiContainer):
    for value in container.pi_values:
        print(value)

if __name__ == '__main__':
    print('All functions are defined')
