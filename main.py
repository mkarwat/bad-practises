from pi_Generator import PiContainer, calc_pi
from pathlib import Path

def display_pi_values(container: PiContainer):
    for pi_value in container.pi_values:
        print(f'Next element: {pi_value}')

def main():
    approx_level = 5
    pi_generator = calc_pi(approx_level)

    # First container
    my_pi = PiContainer()
    try:
        for next_pi in pi_generator:
            my_pi.add_pi_values(next_pi)
    except ValueError as e:
        print('ValueError was raised:', e)
        raise

    # Second container
    my_pi_2 = PiContainer()
    rounded_approx = 23
    pi_generator = calc_pi(approx_level=194)
    for _ in range(rounded_approx):
        my_pi_2.add_pi_values(next(pi_generator))

    # Third container
    my_pi_3 = PiContainer()
    pi_generator = calc_pi(approx_level=6)
    my_pi_3.add_pi_values(list(pi_generator))

    # Displaying values
    print('My first pi:')
    display_pi_values(my_pi)
    print('My second pi:')
    display_pi_values(my_pi_2)

    # Writing to a file
    base_path = Path('test/filepath')
    filename = 'pi-file.txt'
    my_file = base_path / filename

    with my_file.open('w') as f:
        f.write(f'my best pi: {my_pi_3.latest_pi}')

if __name__ == '__main__':
    main()
