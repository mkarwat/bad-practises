# Changes

### file87.py

- renamed filename **file87.py** into **pi_toolkit.py**
- removed global variables form file
- renamed class `pi_container` into `PiContainer` *(camelCase)*
- list `my_pies` list is no longer created in arguments
- changed `type(x) == list` into `isinstance(new_pi, list)` (allows using of subclasses)
- added property `best`, that returns the most accurate calculated pi approximation
- added function docstring
- removed unnecessary comment
- removed `yield 'finished'` (unnecessary, mixes return float with string)
- moved print into main idiom

### file157.py

- renamed filename **file157.py** into **main.py**
- moved imports into the top of file, instead of importing everything,
- import specific classes and functions, import `print_pi` as different name
- move `PiContainer` creation outside try
- added `num_approx` and loop that calculates based of that number
- added error type cases
- removed unused variable from loop and changed it into `_` (line 30)
- simplify `[i for i in list(pi_gen)]` into `list(pi_gen)`
- added **Path** variable `file_path`
- changed file handling (automatic closing the file)
- moved everything into main function and added main idiom

### overall changes

- improved code readability and styling
- added static typing
- renamed some variables and functions into more meaningful names
- renamed `enumerate` into `print_pi` (shadows build in function)