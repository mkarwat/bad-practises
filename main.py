from PIContainer import PiContainer, calcPi
from pathlib import Path

def printPi(pi:PiContainer):
    for my_pi in pi.my_pies:
        print(f'Next element: {my_pi}')

def main():
    my_pi = PiContainer()
    my_pi_2 = PiContainer()
    my_pi_3 = PiContainer()
    try:
        num_approx = 5
        pi_gen = calcPi(num_approx)
        for pi in pi_gen:
            my_pi.addPi(pi)
    except ValueError:
        print('something went horribly wrong :(')
        raise
    except (RuntimeError, TypeError) as err:
        print(err)
        raise

    num_approx = 194
    pi_gen_2 = calcPi(num_approx)
    for _ in range(num_approx):
        my_pi_2.addPi(next(pi_gen_2))


    pi_gen_3 = calcPi(approx_level=6)
    my_pi_3.addPi(list(pi_gen_3))

    print('my first pi')
    printPi(my_pi)
    print('my second pi')
    printPi(my_pi_2)

    file_path = Path('bestPi.txt')
    with file_path.open('w+') as new_file:
        new_file.write(f'my best pi: {my_pi_3.best_pi}')

if __name__ == "__main__":
    main()