class PiContainer:
    def __init__(self):
        self.vector_pi = list()

    def add_element(self, x) -> None:
        if isinstance(x, list):
            self.vector_pi += x
        else:
            self.vector_pi.append(x)

    def print_results(self) -> None:
        for i in self.vector_pi:
            print(i)

    def approximation(self, iterations):
        denominator = 1
        sum = 0
        for i in range(iterations):
            # even index elements are positive
            if i % 2 == 0:
                sum += 4 / denominator
            else:
                # odd index elements are negative
                sum -= 4 / denominator

            # denominator is odd
            denominator += 2
        self.vector_pi.append(sum)


def main():
    my_pi = PiContainer()
    my_pi.approximation(10000)
    my_pi.print_results()
    with open("pi.txt", "w") as file:
        file.write(f"Best approximation: {my_pi.approximation(10000)}")
        file.close()


if __name__ == "__main__":
    main()
