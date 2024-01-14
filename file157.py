from file87 import piContainer, calculate


def enumerate(pi):
    for i in pi.a:
        print(f'Next element: {i}')


try:
    my_pi = piContainer()
    pi_gen_1 = calculate(5)

    for i in range(6):
        my_pi.mth(pi_gen_1.__next__())

    my_pi_2 = piContainer()

    pi_gen_2 = calculate(194)
    for i in range(23):
        my_pi_2.mth(next(pi_gen_2))

    my_pi_3 = piContainer()
    pi_gen_3 = calculate(6)
    my_pi_3.mth([i for i in list(pi_gen_3)])

    print('my first pi')
    enumerate(my_pi)

    print('my second pi')
    enumerate(my_pi_2)

    new_file = open('pi_approximation.txt', 'w')
    new_file.write(f'my best pi: {my_pi_3.a[:]}')
    new_file.close()

except:
    print('something went wrong')
