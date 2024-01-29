from my_pi import PiContainer, calc_pi

def enumerate_pi(pi):
    for next_pi in pi.my_pies:
        print(f'Next element: {next_pi}')

my_pi = PiContainer()
limit = 5
try:

    pi_gen = calc_pi(limit)

    for next_pi in pi_gen:
        my_pi.add_pi(next_pi)

except ValueError:
    print(f'unsupported value {limit}')

my_pi_2 = PiContainer()
pi_gen_3 = calc_pi(approx_level=194)

needed_limit = 23
for _ in range(needed_limit):
    my_pi_2.add_pi(next(pi_gen_3))

my_pi_3 = PiContainer()
pi_gen = calc_pi(approx_level=6)
my_pi_3.add_pi(list(pi_gen))

print('my first pi')
enumerate_pi(my_pi)
print('my second pi')
enumerate_pi(my_pi_2)

with open('some-file.txt', 'w') as new_file:
    new_file.write(f'my best pi: {my_pi_3.best}')
