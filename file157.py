from file87 import PiContainer, calculate_pi, print_elements

# Initialize the PiContainer objects outside the try block
my_pi = PiContainer()
my_pi_2 = PiContainer()
my_pi_3 = PiContainer()

try:
    # Generate pi approximations for my_pi
    pi_gen = calculate_pi(5)
    for _ in range(4):
        my_pi.add(next(pi_gen))

    # Continue using the same generator to maintain the state for my_pi
    for _ in range(3):
        my_pi.add(next(pi_gen))

    # Generate pi approximations for my_pi_2
    pi_gen_3 = calculate_pi(194)
    for _ in range(23):
        my_pi_2.add(next(pi_gen_3))

    # Generate pi approximations for my_pi_3
    pi_gen = calculate_pi(6)
    my_pi_3.add([i for i in pi_gen])

except Exception as e:
    print(f'Something went wrong: {e}')

# Print the elements of the first and second PiContainers
print('My first Pi approximations:')
print_elements(my_pi)
print('My second Pi approximations:')
print_elements(my_pi_2)

# Write the last approximation from the third PiContainer to a file
with open('some-file.txt', 'w') as new_file:
    new_file.write(f'My best pi: {my_pi_3.elements[-1]}')
