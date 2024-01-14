from pi_def import PiContainer, calc_pi, print_pi
from pathlib import Path


def main():
    my_pi = PiContainer()
    my_pi_2 = PiContainer()

    try:
        pi_gen = calc_pi(approx_level=5)
        for pi in pi_gen:
            my_pi.add_pi(pi)

    except ValueError:
        print('ERROR Value error')
        raise

    except (RuntimeError, TypeError) as err:
        print(err)
        raise

    pi_gen = calc_pi(approx_level=194)
    needed_approx = 23
    for _ in range(needed_approx):
        my_pi_2.add_pi(next(pi_gen))

    my_pi_3 = PiContainer()
    pi_gen = calc_pi(approx_level=6)
    my_pi_3.add_pi(list(pi_gen))

    print('My first pi approximation: ')
    print_pi(my_pi)
    print('My second pi approximation: ')
    print_pi(my_pi_2)

    file_path = Path('pi_approx.txt')

    with open(file_path, 'a+') as f:
        f.write(f'My best pi: {my_pi_3.best}\n')


if __name__ == "__main__":
    main()
