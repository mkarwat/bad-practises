# Fixed Issues

## file157.py -> main.py
* changed 'enumerate' function to 'enumerate_pi' (enumerate is already builtin function)
* iterator 'hello' -> 'i'
* placing import keyword on the top of file
* instead of 'import *' import only class and methods
* foramtting issues deleting adding blank lines where needed
* get next generator value using for loop


## file87.py -> pi_container.py
* changed global variables to local (it is better to avoid global variables)
* deleted 'a' variable from constructor (it was always set to empty)
* class name changed to Pascal Case
* changed function foo() to pi_generator()
* changed iterator 'hello' to 'i'
* added description about pi approximation method and explain variables b, c purpose
* added if __name__ == "__main__" line to don't run this file while importing 
