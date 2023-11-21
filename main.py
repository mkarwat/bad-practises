from pi_ops import PiContainer, calculate_pi


def enumerate_pi(pi_container):
    for pi in pi_container.my_pies:
        print(f'Next element: {pi}')


def main():
    my_pi = PiContainer()
    my_pi_2 = PiContainer()
    pi_gen = calculate_pi(approximation_level=5)

    try:
        for next_pi in pi_gen:
            my_pi.add_pi(next_pi)

    except ValueError as e:
        print(e)
        raise e

    pi_gen = calculate_pi(approximation_level=194)
    required_approximation = 23

    for _ in range(required_approximation):
        my_pi_2.add_pi(next(pi_gen))

    my_pi_3 = PiContainer()
    pi_gen = calculate_pi(approximation_level=6)
    my_pi_3.add_pi(list(pi_gen))

    print('my first pi')
    enumerate_pi(my_pi)
    print('my second pi')
    enumerate_pi(my_pi_2)

    with open('some-file.txt', 'w') as f:
        f.write(f'my best pi: {my_pi_3.best_approximation}')


if __name__ == '__main__':
    main()
