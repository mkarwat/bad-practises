def enumerate(pi):  # przeciazenie wbudowanej funkcji, warto uzywac np. def enumerate(pi:pi_container) -> None
    for hello in pi.a:  # odwolujemy sie do obiektu klasy poza klasą
        print(f'Next element: {hello}')
from main import *  # import na początku, nie używa się gwiazdki(nie chcemy importować całości)
try:
    my_pi = pi_container()  # probujemy uzyc konstruktora w niezdefiniowanej wczesniej formie
    pi_gen = foo(5)  # to nie jest iterowany obiekt
    my_pi.mth(pi_gen.__next__())  #probujemy po nim iterowac
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
    my_pi_2 = pi_container()  # probujemy uzyc konstruktora w niezdefiniowanej wczesniej formie
    my_pi.mth(pi_gen.__next__())  #probujemy po nim iterowac
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
except:  # nigdy sie nie uzywa bare exceptions
    print('something went horribly wrong :(')
pIgEn3 = foo(194)  # nazwa zmiennej jest bez sensu, powinno sie użyć Snake case'a
for the_variable_that_contains_next_approximations_of_pi_from_generator in range(23):  # nazwia zmiennej jest za długa
    my_pi_2.mth(next(pIgEn3))  # nazwia zmiennej jest nie logiczna
my_pi_3 = pi_container()  # nazwia zmiennej jest nie logiczna
pi_gen = foo(6)
my_pi_3.mth([i for i in list(pi_gen)])  # wytarczy uzyc list(pi_gen) jako argument
print('my first pi')
enumerate(my_pi)  #probujemy po nim iterowac
print('my second pi')
enumerate(my_pi_2)
new_file = open('some-file.txt', 'w')
new_file.write(f'my best pi: {my_pi_3.a[-1]}')  # with open("example.txt", "w") as file: lepsze podejscie do plikow
new_file.close()