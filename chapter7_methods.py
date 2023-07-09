
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

# Any expression can be used as long as it evaluates to the correct type.
