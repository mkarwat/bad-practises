from headers.pi_appr_utils import PiContainer, generate_pi_series

def display_pi_elements(pi_instance):
    for element in pi_instance.elements:
        print(f'Next PI approximation: {element}')

try:
    pi_series_1 = PiContainer()
    pi_generator = generate_pi_series(5)

    for _ in range(6):
        pi_series_1.add_approximation(next(pi_generator))

    pi_series_2 = PiContainer()

    for _ in range(23):
        pi_series_2.add_approximation(next(pi_generator))

    pi_series_3 = PiContainer()
    pi_generator = generate_pi_series(6)
    pi_series_3.add_approximations(list(pi_generator))

    print('Approximations from first series:')
    display_pi_elements(pi_series_1)

    print('Approximations from second series:')
    display_pi_elements(pi_series_2)

    with open('pi_approximations_summary.txt', 'w') as summary_file:
        summary_file.write(f'Latest PI approximation: {pi_series_3.elements[-1]}')

except Exception as error:
    print(f'Error encountered: {error}')
