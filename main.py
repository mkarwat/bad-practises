from pi_toolkit import PiContainer, calc_pi
from pi_toolkit import print_pi as print_pi_1
from pathlib import Path


def print_pi(pi):
    for my_pi in pi.my_pies:
        print(f'Next element: {my_pi}')


def main():
    my_pi = PiContainer()
    my_pi_2 = PiContainer()
    try:
        num_approx = 5
        pi_gen = calc_pi(num_approx)
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
    pi_gen = calc_pi(approx_level)
    needed_approx = 23
    for _ in range(needed_approx):
        my_pi_2.add_pi(next(pi_gen))

    my_pi_3 = PiContainer()
    pi_gen = calc_pi(approx_level=6)
    my_pi_3.add_pi(list(pi_gen))

    print('my first pi')
    print_pi(my_pi)
    print('my second pi')
    print_pi(my_pi_2)

    file_path = Path('pi_file.txt')

    with open(file_path, 'a+') as f:
        f.write(f'my best pi: {my_pi_3.best}\n')


if __name__ == "__main__":
    main()