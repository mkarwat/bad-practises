from pi_generator import PiContainer, calc_pi
#from pi_generator import enumerate_pi as ep
from pathlib import Path

def enumerate_pi(pi):
    for my_pi in pi.my_pi:
        print(f'Next element: {my_pi}')

def main():
    my_pi = PiContainer()
    approx_level = 5
    pi_gen = calc_pi(approx_level)
    try:
        for next_pi in pi_gen:
            my_pi.add_pies(next_pi)

    except ValueError as e:
        print('ValueError was raised')
        raise e

    my_pi = calc_pi(approx_level=194)
    my_pi_2 = PiContainer()
    rounded_approx = 23
    for _ in range(rounded_approx):
        my_pi_2.add_pies(next(pi_gen))
    my_pi_3 = PiContainer()
    pi_gen = calc_pi(approx_level=6)
    my_pi_3.add_pies(list(pi_gen))

    print('my first pi')
    enumerate(my_pi)
    print('my second pi')
    enumerate(my_pi_2)

    base_path = Path('test/filepath')
    filename = 'pi-file.txt'
    my_file = base_path / filename

    with my_file.open('w') as f:
        f.write(f'my best pi: {my_pi_3.best}')

if __name__ == '__main__':
    main()