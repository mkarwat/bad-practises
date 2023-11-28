from piOpts import PiContainer, calculate_pi
from pathlib import Path


def main():
    my_pi = PiContainer()
    my_pi_2 = PiContainer()
    my_pi_3 = PiContainer()
    try:
        pi_gen = calculate_pi(aproxLevel=5)
        for pi in pi_gen:
            my_pi.add_pi(pi)
    except(StopIteration) as e:
        print(e)


    pi_gen = calculate_pi(aproxLevel=194)

    myApproxLevel = 23

    for _ in range(myApproxLevel):
        my_pi_2.add_pi(next(pi_gen))

    pi_gen = calculate_pi(aproxLevel=6)
    my_pi_3.add_pi(list(pi_gen))

    print('my first pi')
    my_pi.enumerate_pi(my_pi)

    print('my second pi')
    my_pi.enumerate_pi(my_pi_2)

    path = Path(r'')
    with open(path / 'best_pi.txt', 'w') as f:
        f.write(f'my best pi: {my_pi_3.best_approx}')

if __name__ == '__main__':
    main()