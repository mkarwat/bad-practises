from file87 import *

def print_pi_container(pi):
    for hello in pi.a:
        print(f'Next element: {hello}')

pi_gen = pi_generate(15)
my_pi = PiContainer()
my_pi.mth([pi_approx for pi_approx in pi_gen])

pi_gen_2 = pi_generate(194)
my_pi_2 = PiContainer()

my_pi_2.mth([pi_approx for pi_approx in pi_gen_2])

pi_gen_3 = pi_generate(6)    
my_pi_3 = PiContainer()
my_pi_3.mth([pi_approx for pi_approx in pi_gen_3])

print('my first pi')
print_pi_container(my_pi)
print('my second pi')
print_pi_container(my_pi_2)
print('my third pi')
print_pi_container(my_pi_3)

with open('best-pi.txt', 'w') as best_pi:
    best_pi.write(f'my best pi: {my_pi_3.a[-1]}')
