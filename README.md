# The worst way to calculate π in Python

### This project shows what should be avoided when creating Python projects.

### There are many bad practises there, can you find (and correct) them all?

Your task is to clone this repository, create a new branch, fix all the issues and bad practises, add  file with list of all the changes and explanations why they are wrong. Then create a pull request with your branch, add your teacher as reviewer.

(As this project is full of bad practises please do not use it as an example. It's for educational purposes only.)

1. Global variables in file87.py
2. Import in weird places in file157.py
3. Too long and unreadable variable names in the 157.py file, which describe too detailed the operation of the variables
4. Unintuitive files name
5. Variable name like "b = 0, c = 1" can only by if we provide a descriptions.
6. Unnesserly fragment: yield 'finished' 
7. "__init__" in class PiContainer have to by declarate in this way:
        "def __init__(self, a = None):
                self.a = a if a is not None else []"
, because we will by able to create new memory space for the new object.
8. More description, the best to use English language
9. When we imprt something the best way is to define what we use from the library
10. Use 'pathlib' to manipulate paths, as this will reduce the chance of errors when opening our program in another OS
