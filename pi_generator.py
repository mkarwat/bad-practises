b = 0  # Global variables without the type
c = 0  # Name does not explain what is it for


class pi_container:  # Class names should start from upper case
    def __init__(self, a=list()):  # Tuple should be used, not mutable list
        self.a = a

    def mth(self, x):  # What is that supposed to do? Name says nothing
        if type(x) == list:  # Should be checked by instance(x, list)
            self.a += x
        else:
            self.a.append(x)


def foo(
    x,
):  # Again, the name of the method says nothing
    global b  # Global variables inside of the functions - why?
    global c  # Again, names tell nothing
    b = 0
    c = 1
    """
    """
    for hello in range(x):
        if hello % 2 == 0:
            b += (
                4 / c  # Comment below is too long
            )  # this is a very important operation in calculateing pi according to documentation that is provided in a seperate file in this repository, please analyse this file before using!
        else:
            b -= 4 / c
        c += 2
        yield b
    yield "finished"


def enumerate(pi: pi_container):  # Overloaded built-in function
    for hello in pi.a:  # Class object outside of the class
        print(hello)


print("All functions are defined")  # Simple "works" would be sufficient
