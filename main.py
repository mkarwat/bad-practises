# in Python, you cant override functions with the same name

# it is better to clearly write what you want to import
from pi_container import PiContainer, pi_generator, enumerate_pi


#  script should be modular
def first_pi():
    my_pi = PiContainer()  # object definition before try/except
    lim = 5  # better to store important numbers in variables
    iterations = 10
    try:
        pi_gen = pi_generator(lim)
        for _ in range(iterations):
            my_pi.set_values(pi_gen.__next__())
    except StopIteration as err:  # try/except should not be used with no errors after except
        print("Raised StopIteration error. ")  # proper message printing
    return my_pi


def second_pi():
    my_pi_2 = PiContainer()  # initialisation of new object in proper place
    lim = 194
    iterations = 23
    pi_gen_2 = pi_generator(lim)
    for _ in range(iterations):  # not used loop variable should be named as '_'
        my_pi_2.set_values(next(pi_gen_2))
    return my_pi_2


def third_pi():
    my_pi_3 = PiContainer()
    lim = 6
    pi_gen_3 = pi_generator(lim)  # proper name according to connection in this script
    my_pi_3.set_values([i for i in list(pi_gen_3)])
    return my_pi_3


def init():
    my_pi = first_pi()
    my_pi_2 = second_pi()
    my_pi_3 = third_pi()

    if my_pi:
        print('My first pi: ')  # proper english
        enumerate_pi(my_pi)

    if my_pi_2:
        print('My second pi: ')
        enumerate_pi(my_pi_2)

    if my_pi_3:
        # it is better to use with, then it will automatically close the stream
        with open('best_pi.txt', 'w') as f:
            f.write(f'my best pi: {my_pi_3.values[-1]}')  # proper naming


if __name__ == '__main__':
    init()
