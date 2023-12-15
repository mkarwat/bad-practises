from my_pi import calc_pi, PiContainer
from pathlib import Path

def enumerate_pi(pi):
    for next_pi in pi.my_pies:
        print(f'Next element: {next_pi}')


def main():
    my_pi = PiContainer()
    limit = 5
    try:
        pi_gen = calc_pi(limit)
        for next_pi in pi_gen:
            my_pi.add_pi(pi_gen.__next__())
    except ValueError:
        print(f'unsupported value {limit}')
        raise
    except (RuntimeError, FileNotFoundError) as e:
        print(e)
        raise

    my_pi_2 = PiContainer()
    approx_level = 194
    pi_gen_3 = calc_pi(approx_level)
    needed_limit = 23
    for _ in range(needed_limit):
        my_pi_2.add_pi(next(pi_gen_3))

    my_pi_3 = PiContainer()
    pi_gen = calc_pi(approx_level=6)
    my_pi_3.add_pi(list(pi_gen))
    print('my first pi')
    enumerate_pi(my_pi)
    print('my second pi')
    enumerate_pi(my_pi_2)

    base_path = Path('')
    file_path = 'pi-file.txt'

    with (base_path / file_path).open('w') as f:
        f.write(f'my best pi: {my_pi_3.my_pies[-1]}')

