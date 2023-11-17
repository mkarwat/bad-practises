from pi_ops import leibniz_pi_generator, PiContainer

if __name__ == "__main__":

    try:
        my_pi = PiContainer()
        my_pi_2 = PiContainer()
        my_pi_3 = PiContainer()

        pi_gen = leibniz_pi_generator(5)
        for _ in range(7):
            my_pi.append_container(pi_gen.__next__())

        pi_gen = leibniz_pi_generator(194)
        for _ in range(23):
            my_pi_2.append_container(next(pi_gen))

        pi_gen = leibniz_pi_generator(6)
        my_pi_3.append_container([i for i in list(pi_gen)])

    except Exception as e:
        print('An error occured during pi approximation.', e)

    print('my first pi')
    my_pi.enumerate()

    print('my second pi')
    my_pi_2.enumerate()

    with open('some-file.txt', 'w') as f:
        f.write(f'my best pi: {my_pi_3.pi_val[-1]}')
