from Pi_Operations import PiContainer, calculate_pi
from pathlib import Path


def print_pi_elements(pi):
    for value in pi.my_pies:
        print(f'Next element: {value}')


def main():
    my_pi = PiContainer()
    pi_gen = calculate_pi(approx_level=5)

    try:
        for next_pi in pi_gen:
            my_pi.add_pies(next_pi)

    except ValueError as e:
        print(e)
        raise

    pi_gen = calculate_pi(approx_level=194)
    my_pi_2 = PiContainer()

    required_level = 23
    for _ in range(required_level):
        my_pi_2.add_pies(next(pi_gen))

    my_pi_3 = PiContainer()
    pi_gen = calculate_pi(approx_level=6)
    my_pi_3.add_pies(list(pi_gen))

    print('my first pi')
    print_pi_elements(my_pi)
    print('my second pi')
    my_pi_2.enumerate_me()

    base_path = Path(r'./')
    file_name = 'outcome_pi_file.txt'
    file_path = base_path / file_name

    with open(file_path, 'w') as f:
        f.write(f'my best pi: {my_pi_3.best}')


if __name__ == '__main__':
    main()
