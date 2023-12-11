from pi_calculator import pi_container, calc_pi

try:
    my_pi = pi_container()
    my_pi2 = pi_container()
    oper = 5
    pi_gen = calc_pi(num_of_operations=oper)
    for i in range(oper):
        my_pi.add_calc(pi_gen.__next__())
    oper = 3
    pi_gen = calc_pi(num_of_operations=3)
    for i in range(oper):
        my_pi2.add_calc(pi_gen.__next__())
except Exception as e:
    print("Error: " + str(e))

calc_pi(num_of_operations=23)

my_pi3 = pi_container()
pi_gen = calc_pi(num_of_operations=oper)
for i in range(oper):
        my_pi3.add_calc(pi_gen.__next__())
if len(my_pi) > 0:
    print('my first pi')
    print(my_pi)
    if len(my_pi2) > 1:
        print('my second pi')
        print(my_pi2)

result_file = open('results.txt', 'w')
result_file.write('my best pi: ' + str(my_pi3.pi_list[-1]))
result_file.close()
