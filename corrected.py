class PiContainer:
    def __init__(self):
        self.vector_pi = list()

    def add_element(self, x) -> None:
        if isinstance(x, list):
            self.vector_pi += x
        else:
            self.vector_pi.append(x)

    def print_pi(self) -> None:
        for i in self.vector_pi:
            print(i)

    def pi_leibniz_approximation(self, iteration: int) -> float:
        pi = 0
        for i in range(iteration):  # pi += 4 / (2 * i + 1) if i % 2 == 0 else -4 / (2 * i + 1)
            if i % 2 == 0:
                pi += 4 / (2 * i + 1)
            else:
                pi -= 4 / (2 * i + 1)
            self.vector_pi.append(pi)
        return pi


def main():
    my_pi = PiContainer()
    my_pi.pi_leibniz_approximation(100)
    my_pi.print_pi()
    with open('pi_approximation.txt', 'w') as f:
        f.write(f'Best approximation: {my_pi.pi_leibniz_approximation(100)}')
        f.close()
        
        
if __name__ == "__main__":
    main()
