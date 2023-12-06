from utils import *

my_pi = PiContainer()
my_pi_2 = PiContainer()
my_pi_3 = PiContainer()

try:
    pi_gen = pi_approximation(5)
    my_pi.mth([i for i in list(pi_gen)])
    print('my first pi')
    my_pi.pi_enumerate()
except Exception as e:
    print('An Error has occurred during pi approximation:', e)

pi_gen_2 = pi_approximation(23)
my_pi_2.mth([i for i in list(pi_gen_2)])
print('my second pi')
my_pi_2.pi_enumerate()

pi_gen_3 = pi_approximation(196)
my_pi_3.mth([i for i in list(pi_gen_3)])

with open('best pi.txt', 'w') as file:
    file.write(f'my best pi: {my_pi_3.pi_list[-1]}')

