from file87 import *


def count(pi):
    for hello in pi.a:
        print(f'Next element: {hello}')


try:
    pi_container = PiContainer()
    pi_approximated = pi_approx(5)
    pi_container.mth(pi_approximated.__next__())
    pi_container.mth(pi_approximated.__next__())
    pi_container.mth(pi_approximated.__next__())
    pi_container.mth(pi_approximated.__next__())
    pi_container_2 = PiContainer()
    pi_container.mth(pi_approximated.__next__())
    pi_container.mth(pi_approximated.__next__())
    pi_container.mth(pi_approximated.__next__())
except:
    print('unknown exception')
pi_approximated2 = pi_approx(194)
for i in range(23):
    pi_container_2.mth(next(pi_approximated2))
my_pi_3 = PiContainer()
pi_gen = pi_approx(6)
my_pi_3.mth([i for i in list(pi_gen)])
print('first pi approximation')
count(pi_container)
print('second pi approximation')
count(pi_container_2)
new_file = open('pi_approx.txt', 'w')
new_file.write(f'my best pi: {my_pi_3.a[-1]}')
new_file.close()
