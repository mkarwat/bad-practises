class PiCalculator:
    def __init__(self):
        self.vector_pi = []

    def pi_leibniz(self, iteration: int) -> float:
        pi = 0.0

        for i in range(iteration):
            pi += 4 / (2 * i + 1) if i % 2 == 0 else -4 / (2 * i + 1)
            self.vector_pi.append(pi)

        return pi


pi_calculator = PiCalculator()
iteration = 1000000
approx_pi = pi_calculator.pi_leibniz(iteration)
print(f"Przybliżona wartość liczby π dla {iteration} iteracji: {approx_pi}")
