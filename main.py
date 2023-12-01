from pathlib import Path
from pi_class import pi_generator, PiContainer

def enumerate_pi(pi_container):
    for pi in pi_container.my_pies:
        print(f'Next element: {pi}')


def main():
    my_pi = PiContainer()
    my_pi2 = PiContainer()
    pi_gen = pi_generator(approx=5)

    try:
        for next_pi in pi_gen:
            my_pi.add_pi(next_pi)

    except ValueError as e:
        print(e)
        raise e

    pi_gen = pi_generator(approx=194)
    my_pi2 = PiContainer()

    required_approx_level = 23
    for _ in range(required_approx_level):
        my_pi2.add_pi(next(pi_gen))

    my_pi3 = PiContainer()
    pi_gen = pi_generator(approx_level=60)
    my_pi3.add_pi(list(pi_gen))

    print('my first pi')
    enumerate_pi(my_pi)
    print('my second pi')
    my_pi2.enumerate_my_pi()

    with open('pi.txt', 'w') as f:
        f.write(f'my best pi: {my_pi3.best_approx}')

if __name__ == '__main__':
    main()