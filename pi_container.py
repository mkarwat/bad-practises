
class PI_Container:
    def __init__(self) -> None:
        self.values = []

    def add(self, value) -> None:
        if isinstance(value, list): # to być be
            self.values = value
        elif isinstance(value, float):
            self.values.append(value)
        else:
            raise NotImplementedError


def pi_generator(steps: int):
    b = 0
    c = 1

    for i in range(int(steps)):
        if i % 2 == 0:
            b += 4 / c 
        else:
            b -= 4 / c
        c += 2
        yield b



def PI_enumerate(pi: PI_Container):
    for index, value in enumerate(pi.values):
        print(f"{index}. {value}")


if __name__ == "__main__":
    print("Run main file.")
    print("This is only function definer")