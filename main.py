from piClass import PiClass
from piClass import calculatePi

def enumerate(pi):
    for hello in pi.value:
        print(f'Next element: {hello}')

def main():
    my_pi = PiClass()
    pi_gen = calculatePi(level = 5)
    try:
        for pi in pi_gen:
            my_pi.more_pies(pi)

    except ValueError as e:
        print(e)
        raise e    

    pi_gen = calculatePi(level = 194)

    my_pi_2 = PiClass()
    required_range = 23
    
    for _ in range(required_range):
        my_pi_2.appendPi(next(pi_gen))

    my_pi_3 = PiClass()
    pi_gen2 = calculatePi(6)
    my_pi_3.mth([i for i in list(pi_gen2)])

    print('my first pi')
    enumerate(my_pi)
    print('my second pi')
    enumerate(my_pi_2)

    file_path = 'some-file.txt'

    with open(file_path, 'w') as f:
            f.write(f'my best pi: {my_pi_3.best}')

if __name__ == '__main':
     main()