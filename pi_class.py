class PiContainer:
    def __init__(self, my_pies=None):
        if my_pies is None:
            my_pies = list()
        else:
            self.my_pies = my_pies

    def add_pi(self, next_pi):
        if isinstance(next_pi, list):
            self.my_pies += next_pi
        else:
            self.my_pies.append(next_pi)

    @property
    def best_approx(self):
        return self.my_pies[-1]
    
    def enumerate(self):
        for i in self.my_pies:
            print(i)

    def pi_generator(approx):
    # Refering to documentation here
        
        b = 0
        c = 1

        for i in range(approx):
            if i % 2 == 0:
                b += 4 / c  #some way shorter comment
                            #or even in new line
            else:
                b -= 4 / c
            c += 2
            yield b

if __name__ == '__main__':
    print('All functions are defined')