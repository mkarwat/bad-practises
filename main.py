from my_ops import PiContainer, calc_pi

def enumerate_pi(pi):
    for index in pi.my_pies:
        print(f'Next element: {index}')

def main():
    try:
        my_pi = PiContainer()
        ctr = 5
        pi_gen = calc_pi(approx_level=ctr)
        for next_pi in pi_gen:
            my_pi.mth(next_pi)

    except ValueError as e:
        print(e)
        raise e
    except (FileNotFoundError, EOFError) as e:
        raise e

    pi_gen = calc_pi(approx_level=194)
    my_pi_2 = PiContainer()
    required_level=23
    for _ in range(required_level):
        my_pi_2.mth(next(pi_gen))

    my_pi_3 = PiContainer()
    pi_gen = calc_pi(approx_level=6)
    my_pi_3.mth(list(pi_gen))

    print('my first pi:')
    enumerate_pi(my_pi)
    print('my second pi:')
    enumerate_pi(my_pi_2)

    with open('some-file.txt', 'w') as f:
        f.write(f'my best pi: {my_pi_3.best}')


if __name__ == "__main__":
    main()