from PI_CalculationBlock import PiContainer, generate_pi_approximations

NUM_GENERATOR_CALLS = 194
NUM_ITERATIONS = 23

def my_enumerate(pi):
    for actualPI in pi.a:
        print(f'Next element: {actualPI}')

if __name__ == '__main__':
    try:
        my_pi = PiContainer()
        pi_gen = generate_pi_approximations(5)
        for _ in range(5):
            my_pi.mth(next(pi_gen))
        my_pi_2 = PiContainer()
        for _ in range(3):
            my_pi_2.mth(next(pi_gen))
    except StopIteration:
        print('Generator has completed.')

    pi_gen3 = generate_pi_approximations(NUM_GENERATOR_CALLS)
    for _ in range(NUM_ITERATIONS):
        try:
            my_pi_2.mth(next(pi_gen3))
        except StopIteration:
            print('Generator has completed.')

    my_pi_3 = PiContainer()
    pi_gen = generate_pi_approximations(6)
    my_pi_3.mth(list(pi_gen))
    print('my first pi')
    my_enumerate(my_pi)
    print('my second pi')
    my_enumerate(my_pi_2)

    with open('result_Pi_Calculation.txt', 'w') as new_file:
        new_file.write(f'my best pi: {my_pi_3.a[-1]}')