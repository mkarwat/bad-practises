from function import PiContainer, calculate_pi, print_pi

def main():
    my_pi = PiContainer()
    my_pi_2 = PiContainer()
    try:
        num_approx = 5
        pi_gen = calculate_pi(num_approx)
        for pi in pi_gen:
            my_pi.add_pi(pi)
    except ValueError:
        print('ERROR Value error')
        raise
    except (RuntimeError, TypeError) as e:
        print(e)
        print('')
        raise

    approx_level = 194
    pi_gen = calculate_pi(approx_level)
    needed_approx = 23
    for _ in range(needed_approx):
        my_pi_2.add_pi(next(pi_gen))

    my_pi_3 = PiContainer()
    pi_gen = calculate_pi(approximation_level=6)
    my_pi_3.add_pi(list(pi_gen))

    print('my first pi')
    print_pi(my_pi)
    print('my second pi')
    print_pi(my_pi_2)

    with open('file.txt','w') as new_file:
        new_file.write(f'my best pi: {my_pi_2.my_pi[-1]}')

if __name__ == '__main__':
    main()
