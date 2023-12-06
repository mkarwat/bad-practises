from utils import *

try:
    my_pi = PiContainer()
    pi_gen = foo(5)
    my_pi.mth([i for i in list(pi_gen)])
    print('my first pi')
    my_enumerate(my_pi)
except:
    print('something went horribly wrong :(')

my_pi_2 = PiContainer()
pi_gen_2 = foo(2)
my_pi_2.mth([i for i in list(pi_gen_2)])
print('my second pi')
my_enumerate(my_pi_2)

my_pi_3 = PiContainer()
pi_gen_3 = foo(196)
my_pi_3.mth([i for i in list(pi_gen_3)])

new_file = open('some-file.txt', 'w')
new_file.write(f'my best pi: {my_pi_3.a[-1]}')
new_file.close()


