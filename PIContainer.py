class PiContainer:
    def __init__(self, my_pies:list|None = None) -> None:
        if my_pies is None:
            self.my_pies = []
        else:
            self.my_pies = my_pies 

    def addPi(self, new_pi:float|list[float]) -> None:
        if isinstance(new_pi, list):
            self.my_pies += new_pi
        else:
            self.my_pies.append(new_pi)

    @property
    def best_pi(self):
        return self.my_pies[-1]

def calcPi(approx_level:int) -> float:
    b:float = 0
    c:float = 1
    for i in range(approx_level):
        if i % 2 == 0:
            b += 4 / c
        else:
            b -= 4 / c
        c += 2
        yield b

def printPies(pi: PiContainer):
    for my_pi in pi.my_pies:
        print(my_pi)

if __name__ == "__main__":
    print('All functions are defined')
