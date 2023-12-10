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
            my_pi.add_pies(next_pi)
    except ValueError as e:
        print('something went horribly wrong :(')
        raise e
    except (FileNotFoundError, EOFError):
        raise

    pi_gen = calc_pi(approx_level=194)
    my_pi_2 = PiContainer()
    needed_aprox = 23
    for _ in range(needed_aprox):
        my_pi_2.add_pies(next(pi_gen))
    my_pi_3 = PiContainer()
    pi_gen = calc_pi(approx_level=6)
    my_pi_3.add_pies(list(pi_gen))

    print('my first pi')
    enumerate_pi(my_pi)
    print('my second pi')

    enumerate_pi(my_pi_2)

    base_path = Path('dawdw/dawd/fw')
    file_name = 'pi-file.txt'


    with open('some-file.txt', 'w') as f:
        new_file.write(f'my best pi: {my_pi_3.best')
    new_file.close()
