from pi_calculator import pi_container, calc_pi

my_pi = []

try:
    my_pi.append(pi_container())
    pi_gen = calc_pi(num_of_operations=5, container=my_pi[-1])
    my_pi.append(pi_container())
    pi_gen = calc_pi(num_of_operations=3, container=my_pi[-1])
except Exception as e:
    print("Error: " + str(e))

calc_pi(num_of_operations=23, container=my_pi[-1])

my_pi.append(pi_container())
pi_gen = calc_pi(num_of_operations=6, container=my_pi[-1])
if len(my_pi) > 0:
    print('my first pi')
    print(my_pi[0])
    if len(my_pi) > 1:
        print('my second pi')
        print(my_pi[1])

result_file = open('results.txt', 'w')
result_file.write('my best pi: ' + str(my_pi[-1].pi_list[-1]))
result_file.close()
