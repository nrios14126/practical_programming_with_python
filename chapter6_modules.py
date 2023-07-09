
#### Chapter 6: A Modular Approach to Program Organization ########################################

# A module is a collection of variables and functions that are grouped together in a single file. 
# The variables and functions in a module are usually related to one another in some way.

### Importing Modules ############################################################################

# To gain access to the variables and functions from a module, you have to import it; to tell 
# Python that you want to use functions from math:
import math

# Importing a module creates a new variable with that name. That variable refers to an object whose 
# type is module:
print(type(math))

# To use the functions within 'math', we must use the dot notation. The dot is an operator; its 
# meaning is "look up the object that the variable to the left of the dot refers to and, in that 
# object, find the name that occurs to the right of the dot":
math.sqrt(81)

# Python also lets you specify exactly what you want to import from a module:
from math import sqrt, pi

# Doing this doesn't introduce a variable called 'math'. Instead, it creates function sqrt() and 
# variable pi in the current namespace:
sqrt(9)

pi ** 2

### Defining Your Own Modules #####################################################################

# Python executes modules as it imports them. However, Python loads modules only the first time 
# they're imported. Internally, Python keeps track of the modules it has already seen; when it's 
# asked to load one that's already in that list, it just skips over it. 

# If a module is to be imported by another module, then the files containing the two modules should 
# be saved in the same directory:
import temperature
celsius = temperature.convert_to_celsius(17)

# Sometimes we want to write code that should only be run when the module is run directly and not 
# when the module is imported. Python defines a special string variable called __name__ in every 
# module to help us figure this out. 

# When you run a module directly __name__ is set to "__main__".

# When you import a module __name__ is set to the name of the module itself.

# With this setup you could use the following:
if __name__ == '__main__':
    print('I am the main program')
else:
    print('Another module is importing me')







