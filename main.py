from helpers import PiContainer, generator, enumerate_pi

if __name__ == "__main__":
    my_pi = PiContainer()
    my_pi_2 = PiContainer()
    my_pi_3 = PiContainer()
    pi_gen = generator(5)
    pi_gen_2 = generator(6)
    pi_gen_3 = generator(194)
    my_pi.mth([i for i in list(pi_gen)])
    my_pi_2.mth([i for i in list(pi_gen_2)])
    my_pi_3.mth([i for i in list(pi_gen_3)])
    print('my first pi')
    enumerate_pi(my_pi)
    print('my second pi')
    enumerate_pi(my_pi_2)
    with open('some-file.txt', 'w') as file:
        file.write(f'my best pi: {my_pi_3.a[-1]}')
