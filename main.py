def enumerate(pi):
    for hello in pi.a:
        print(f'Next element: {hello}')
from file87 import *
try:
    my_pi = pi_container()
    pi_gen = foo(5)
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
    my_pi_2 = pi_container()
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
except:
    print('something went horribly wrong :(')
pIgEn3 = foo(194)
for the_variable_that_contains_next_approximations_of_pi_from_generator in range(23):
    my_pi_2.mth(next(pIgEn3))
my_pi_3 = pi_container()
pi_gen = foo(6)
my_pi_3.mth([i for i in list(pi_gen)])
print('my first pi')
enumerate(my_pi)
print('my second pi')
enumerate(my_pi_2)
new_file = open('some-file.txt', 'w')
new_file.write(f'my best pi: {my_pi_3.a[-1]}')
new_file.close()
