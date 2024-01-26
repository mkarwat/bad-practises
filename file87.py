class PiContainer:
    def __init__(self):
        self.elements = []

    def add_approximation(self, approximation):
        self.elements.append(approximation)

    def add_approximations(self, approximations_list):
        self.elements.extend(approximations_list)

def generate_pi_series(terms):
    pi_base = 4.0
    denominator = 1.0
    pi_approximation = 0.0

    for term_index in range(terms):
        pi_term = pi_base / denominator
        pi_approximation += pi_term if term_index % 2 == 0 else -pi_term
        denominator += 2
        yield pi_approximation
    yield 'series_end'
