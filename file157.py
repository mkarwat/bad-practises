from file87 import pi_container, estimate

def enumerate(pi):
    for i in pi.a:
        print(f'Next element: {i}')

try:
    my_pi = pi_container()
    pi_gen_1 = estimate(5)
    for i in range(6):
        my_pi.mth(pi_gen_1.__next__())

    my_pi_2 = pi_container()
    pi_gen_2 = estimate(194)
    for i in range(23):
        my_pi_2.mth(next(pi_gen_2))

    my_pi_3 = pi_container()
    pi_gen_3 = estimate(6)
    my_pi_3.mth([i for i in list(pi_gen_3)])

    print('my first pi')
    enumerate(my_pi)
    
    print('my second pi')
    enumerate(my_pi_2)
    new_file = open('pi_aproximation_3.txt', 'w')
    new_file.write(f'my third pi: {my_pi_3.a[:]}')
    new_file.close()

except:
    print('something went wrong')