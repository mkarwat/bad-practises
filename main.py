from function import PiContainer, calc_pi


def enumerate_pi(pi: PiContainer):
    for my_pi in pi.my_pies:
        print(f'Next element: {my_pi}')


def main():
    my_pi = PiContainer()
    pi_gen = calc_pi(approx_level=5)
    try:
        for next_pi in pi_gen:
            my_pi.add_pi(next_pi)
    except Exception as e:
        print('Error:', e)
        raise e
    pi_gen = calc_pi(approx_level=194)
    my_pi_2 = PiContainer()
    needed_approx = 23
    for _ in range(needed_approx):
        my_pi_2.add_pi(next(pi_gen))
    my_pi_3 = PiContainer()
    pi_gen = calc_pi(approx_level=6)
    my_pi_3.add_pi(list(pi_gen))
    print('my first pi')
    enumerate_pi(my_pi)
    print('my second pi')
    enumerate_pi(my_pi_2)

    with open('pi-file.txt', 'w') as file:
        file.write(f'my best pi: {my_pi_3.best}')


if __name__ == '__main__':
    main()
