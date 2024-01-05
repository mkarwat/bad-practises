from pi_ops import PiContainer, calc_pi, display_pi_value
from pathlib import Path


def enumerate_pi(pi):
    for piValue in pi.piValue:
        print(f'Next element: {piValue}')


def main():
    pi_value_1 = PiContainer()
    pi_value_2 = PiContainer()
    pi_value_3 = PiContainer()

    try:
        pi_gen = calc_pi(approxLvl=5)
        for pi in pi_gen:
            pi_value_1.add_pi(pi)
    except(StopIteration) as e:
        print('Error: ')
        raise e

    pi_gen = calc_pi(approxLvl=194)

    required_approx_level = 23
    for _ in range(required_approx_level):
        pi_value_2.add_pi(next(pi_gen))

    pi_gen = calc_pi(approxLvl=6)
    pi_value_3.add_pi(list(pi_gen))

    print('my first pi')
    display_pi_value(pi_value_1)

    print('my second pi')
    display_pi_value(pi_value_2)

    path = Path(r'')
    with open(path / 'best_pi.txt', 'w') as f:
        f.write(f'my best pi: {pi_value_2.best_approx}')


if __name__ == '__main__':
    main()
