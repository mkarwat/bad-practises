from pi_ops import PiContainer, calc_pi
from pathlib import Path


def enumerate_pi(pi):
    for my_pi in pi.my_pies:
        print(f'Next element: {my_pi}')


def main():
    my_pi = PiContainer()
    pi_gen = calc_pi(approx_level=5)

    try:
        for next_pi in pi_gen:
            my_pi.more_pies(next_pi)

    except ValueError as e:
        print(e)
        raise e

    pi_gen = calc_pi(approx_level=194)
    my_pi_2 = PiContainer()

    required_level = 23
    for _ in range(required_level):
        my_pi_2.more_pies(next(pi_gen))

    my_pi_3 = PiContainer()
    pi_gen = calc_pi(approx_level=60)
    my_pi_3.more_pies(list(pi_gen))

    print('my first pi')
    enumerate_pi(my_pi)
    print('my second pi')
    my_pi_2.enumerate_me()

    base_path = Path(r'./')
    file_name = 'pi-file.txt'
    file_path = base_path / file_name

    with open(file_path, 'w') as f:
        f.write(f'my best pi: {my_pi_3.best}')


if __name__ == '__main__':
    main()
