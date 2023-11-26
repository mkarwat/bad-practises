from pathlib import Path
from pi_ops import calc_pi,PiContainer

def enumerate_pi(pi_container):
    for pi in pi_container.my_pies:
        print(f'Next element: {pi}')

     
def main():
    my_pi = PiContainer()
    my_pi_2 = PiContainer()
    pi_gen = calc_pi(approx=5)

    try:
        for next_pi in pi_gen:
            my_pi.add_pi(next_pi)

    except ValueError as e:
        print(e)
        raise e
    
    pi_gen = calc_pi(approx=194)
    my_pi_2 = PiContainer() 


    req_approx_level = 23
    for _ in range(req_approx_level):
        my_pi_2.add_pi(next(pi_gen)) 


    my_pi_3 = PiContainer()
    pi_gen = calc_pi(approx=60)
    my_pi_3.add_pi(list(pi_gen))


    print('my first pi')
    enumerate_pi(my_pi)
    print('my second pi')
    my_pi_2.enumarate_pi()


    with open('pi.txt', 'w') as f:
        f.write(f'my best pi: {my_pi_3.best}')

if __name__ == '__main__':
    main()