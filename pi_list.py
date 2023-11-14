def enumerate(  # Yet again original enumerate says adios
    pi,
):
    for hello in pi.a:  # Again reference to class object outside of the class
        print(f"Next element: {hello}")


from main import *  # Import should've been at the very start

try:
    my_pi = (
        pi_container()  # Constructor without arguments is not defined for this function
    )
    pi_gen = foo(5)
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
    my_pi_2 = (
        pi_container()  # Again constructor without arguments is not defined for this function
    )
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
except:  # Most to least specific, this kind of usage of exceptions is a heresy
    print("something went horribly wrong :(")
pIgEn3 = foo(194)  # ThE nAmE oF tHe VaRiAbLe Is DeFiNiTeLy WrItTeN iN a WrOnG fOrM
for the_variable_that_contains_next_approximations_of_pi_from_generator in range(
    23
):  # Too long variable name
    my_pi_2.mth(next(pIgEn3))  # Name of the variable says nothing
my_pi_3 = (
    pi_container()
)  # Again name of the variable says nothing and the problem with constructor
pi_gen = foo(6)
my_pi_3.mth([i for i in list(pi_gen)])  # Overkill, list(pi_gen) is enough
print("my first pi")  # Lack of the word "approximation"
enumerate(my_pi)
print("my second pi")
enumerate(my_pi_2)
new_file = open("some-file.txt", "w")  # Name of the file says nothing
new_file.write(f"my best pi: {my_pi_3.a[-1]}")
new_file.close()
