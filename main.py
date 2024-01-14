from pi_container import PiContainer, pi_generator, pi_enumerate

my_pi = PiContainer()
my_pi_2 = PiContainer()
my_pi_3 = PiContainer()

pi_gen = pi_generator(5)
for i in range(8):
    my_pi.add(pi_gen.__next__())    
    

pi_gen_2 = pi_generator(194)    
for i in range(23):
    my_pi_2.add(next(pi_gen_2))
    
my_pi_3.add(list(pi_gen))

print('my first pi')
pi_enumerate(my_pi)

print('my second pi')
pi_enumerate(my_pi_2)

with open('pi_approx_result.txt', 'w') as file:
    file.write(f'my best pi: {my_pi_3.a[-1]}')

