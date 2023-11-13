from pi_container import PI_Container, pi_generator, PI_enumerate


if __name__ == "__main__":
    my_pi = PI_Container()
    my_pi_2 = PI_Container()
    my_pi_3 = PI_Container()
        
    for gen in pi_generator(8):
        my_pi.add(gen)

    for gen in pi_generator(194) :
        my_pi_2.add(gen)

    my_pi_3.add(list(pi_generator(6)))

    print('My first pi')
    PI_enumerate(my_pi)
    print("#"*30)

    print('My second pi')
    PI_enumerate(my_pi_2)
    print("#"*30)


    with open("result.txt", "w") as file:
        file.write(f'my best pi: {my_pi_3.values[-1]}')
