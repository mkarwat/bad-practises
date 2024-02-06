# global variables should be used only if necessary


class PiContainer:  # classes should be named in Pascal case
    def __init__(self, values=None):  # default value for argument should not be mutable
        if values is None:  # correct default value initialisation if list
            values = []
        self.values = values   # better naming convention (variables names should point what they are)

    def set_values(self, value):  # proper arg and method naming
        if type(value) == list:
            self.values += value
        else:
            self.values.append(value)


# proper name with pointed functionality
def pi_generator(lim: int):  # proper name for args with written type
    pi = 0  # proper naming
    divider = 1
    for i in range(lim):  # iterator variable should have proper name eg. i, item
        if i % 2 == 0:
            pi += 4 / divider  # should contain directory where this docs can be found
        else:
            pi -= 4 / divider
        divider += 2
        yield pi
#  yield should be used with the same type


# don't use names same as built-in functionalities and name should point what function does
def enumerate_pi(pi: PiContainer):
    for item in pi.values:  # iterator variable should have proper name eg. i, item
        print(f'Next element: {item}')


print('All functions are defined')
