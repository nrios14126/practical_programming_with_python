
#### Chapter 7: Using Methods #####################################################################

# A method is another kind of function that is attached to a particular type (objects).

### Modules, Classes, and Methods #################################################################

# There is another kind of object that is similar to a module: a class, which is how Python 
# represents a type:
help(str)

# The above describes the class str. We can use str() as a function to create a string. We can also 
# use str to call a method in class str, much like we call a function in module math. The main 
# difference is that every method in class str requires a string as its first argument:
str.capitalize('browning')

# This is how methods are different from functions: the first argument to every string method must 
# be a string, and the parameter is not described in the documentation for the method. More 
# generally, all methods in a class require an object of that class as the first argument. 

### Calling Methods the Object-Oriented Way #######################################################

# Python provides a shorthand form for calling a method where the object appears first and then the 
# method call:
print('browning'.capitalize())

# When Python encounters one of these method calls, it translates it to the more long-winded form.

# The general form of a method call is as follows:
# <<expression>>.<<method_name>>(<<arguments>>)

# Any expression can be used as long as it evaluates to the correct type:
('TTA' + 'G' * 3).count('T')

## Exploring String Methods ***********************************************************************

# Method calls look almost like function calls, except we need an object of the type associated
# with the method.

# String method startswith() takes a string argument and returns a bool indicating whether the 
# called string begins with the given string argument
print('species'.startswith('a'))
print('species'.startswith('spe'))
str.startswith('species', 'spe')

# There's also an endswith() method:
print('species'.endswith('a'))
print('species'.endswith('es'))

# Sometimes strings have extra whitespace at the ends. There are methods that can remove the 
# extra whitespace characters:
compound = '    \n Methyl \n butanol   \n'
compound.lstrip()    # left side
compound.rstrip()    # right side
compound.strip()     # both sides

# Here's a method that swaps lower case to upper case and vice-versa:
print('cOMPUTER sCIENCE'.swapcase())

# Here's how we can substitute a series of strings into a format string:
print('"{0}" is derived from "{1}"'.format('none', 'no one'))
print('"{0}" is derived from the {1} "{2}"'.format('Etymology', 'Greek', 'ethos'))
print('"{0}" is derived from the {2} "{1}"'.format('December', 'decem', 'Latin'))

# We can also specify the number of decimal places to round a float type:
my_pi = 3.14159
print('Pi rounded to {0} decimal places is {1:.2f}'.format(2, my_pi))

# It's possible to remove the position numbers, in which case arguments are placed in order:
print('Pi rounded to {} decimal places is {:.3f}'.format(3, my_pi))

# You can also chain methods as long as the previous ends with an expression:
print('Computer_Science'.swapcase().endswith('ENCE'))

# Note that most modern programming languages are structured in such a way that the things in the
# program are objects, and most code in the program consists of methods that use the data stored
# in those objects.

## Underscores ************************************************************************************

# Any method (or other name) beginning and ending with two underscores is considered special by
# Python. These methods are typically connected with some particular syntax in Python; use of that 
# syntax will trigger a method call that describes what is done:
print('TTA' + 'GGG')         # particular syntax
print('TTA'.__add__('GGG'))  # associated special method

# Note that programmers almost never call these special methods directly:
abs(-3)
(-3).__abs__()
3 > 5
3 .__gt__(5)     # Note that the whitespace is required for int and float

# Function objects contain double-underscore variables:
import math
math.sqrt.__doc__

# If you call the print function on the variable, it will print the help documentation:
print(math.sqrt.__doc__)
