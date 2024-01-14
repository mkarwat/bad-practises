from functions import *

if __name__ == '__main__':

    try:
        my_pi = PiContainer()
        pi_gen = piexpander(5)
        for element in pi_gen:
            my_pi.addnewpositions(element)
            if len(my_pi.values) == 4:
                break

        my_pi_2 = PiContainer()
        for element in pi_gen:
            my_pi_2.addnewpositions(element)

        pigen = piexpander(194)
        for piapprximations in range(23):
            my_pi_2.addnewpositions(next(pigen))

        my_pi_3 = PiContainer()
        pi_gen = piexpander(6)
        my_pi_3.addnewpositions([i for i in list(pi_gen)])
        print(f'my first pi')
        enumerate(my_pi)
        print(f'my second pi')
        enumerate(my_pi_2)
        new_file = open('some-file.txt', 'w')
        new_file.write(f'my best pi: {my_pi_3.values[-1]}')
        new_file.close()


    except:
        print('something went horribly wrong :(')

