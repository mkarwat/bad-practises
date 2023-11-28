from file87 import *

if __name__ == "__main__":
    try:
        my_pi = PiContainer()
        pi_gen = calculate_pi(5)
        for _ in range(5):
            my_pi.add_values(next(pi_gen))

        my_pi_2 = PiContainer()
        pi_gen_2 = calculate_pi(194)
        for _ in range(23):
            my_pi_2.add_values(next(pi_gen_2))

        my_pi_3 = PiContainer()
        pi_gen_3 = calculate_pi(6)
        my_pi_3.add_values(list(pi_gen_3))

        print('my first pi')
        print_values(my_pi)
        print('my second pi')
        print_values(my_pi_2)

        with open('some-file.txt', 'w') as new_file:
            new_file.write(f'My best pi: {my_pi_3.a[5]}')

    except Exception as e:
        print(f'Something went wrong: {e}')
