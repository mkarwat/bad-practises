class pi_container:
    pi_list = None
    def __init__(self, _list=list()):
        self.pi_list = _list

    def add_calc(self, x):
        self.pi_list.append(x)

    def __str__(self):
        result = ""
        for pi in self.pi_list:
            result += str(pi) + "\n"
        return result


def calc_pi(num_of_operations, container):
    b = 0
    c = 1
    for i in range(num_of_operations):
        if 0 == i % 2:
            b += 4 / c  # an actual comment explaining what is happening here
        else:
            b -= 4 / c
        c += 2
        container.add_calc(b)


