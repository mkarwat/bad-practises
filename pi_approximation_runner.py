from pi_approximator import PiContainer, approximate_pi

def display_values(container: PiContainer):
    for value in container.elements:
        print(f'Next element: {value}')

def main():
    try:
        my_first_pi = PiContainer()
        pi_generator = approximate_pi(5)

        # Adding the first four values from the generator to my_first_pi
        for _ in range(4):
            my_first_pi.add(next(pi_generator))

        my_second_pi = PiContainer()

        # Adding the next three values from the generator to my_first_pi
        for _ in range(3):
            my_first_pi.add(next(pi_generator))

        # Generating more pi approximations and adding to my_second_pi
        more_pi_approximations = approximate_pi(194)
        for _ in range(23):
            my_second_pi.add(next(more_pi_approximations))

        my_third_pi = PiContainer()
        another_pi_generator = approximate_pi(6)
        my_third_pi.add([i for i in list(another_pi_generator)])

        print('my first pi')
        display_values(my_first_pi)

        print('my second pi')
        display_values(my_second_pi)

        # Writing the last value of my_third_pi to a file
        with open('some-file.txt', 'w') as new_file:
            new_file.write(f'my best pi: {my_third_pi.elements[-1]}')

    except Exception as e:
        print(f'something went horribly wrong: {e}')

if __name__ == "__main__":
    main()
