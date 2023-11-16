from pi_utils import leibniz_pi_generator, PiContainer
from pathlib import Path

def main():
    my_pi = PiContainer()
    my_pi_2 = PiContainer()
    my_pi_3 = PiContainer()

    try:
        pi_gen = leibniz_pi_generator(approximation_level=5)
        
        for pi in pi_gen:
            my_pi.append_container(pi)
            
    except StopIteration as e:
        print('StopIteration during pi generation', e)

    pi_gen = leibniz_pi_generator(approximation_level=194)

    my_approx_level = 23
    for _ in range(my_approx_level):
        my_pi_2.append_container(next(pi_gen))

    pi_gen = leibniz_pi_generator(approximation_level=6)
    my_pi_3.append_container(list(pi_gen))

    print('my first pi')
    my_pi.enumerate()

    print('my second pi')
    my_pi_2.enumerate()

    dump_path = Path(r'')

    with open(dump_path / 'some-file.txt', 'w') as f:
        f.write(f'my best pi: {my_pi_3.best_approx}')

if __name__ == "__main__":
    main()
