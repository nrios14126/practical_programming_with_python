
#### Chapter 3: Designing and Using Functions #####################################################

### Functions that Python Provides ################################################################

# Python comes with many built-in functions that perform common operations.

# To get the absolute value of a number:
abs(-7)

# The general form of a function call is:
# <<function_name>>(<<argument>>)

# An argument is an expression that appears between the parentheses of a function call.

# Here are the rules to executing a function call:
#   1. Evaluate each argument one at a time, working left-to-right
#   2. Pass the resulting values into the function
#   3. Execute the function

# To get a number raised to some power:
pow(base=2, exp=3)

# Some built functions convert one type to another:
int(3.14159)
float(42)

# If you're not sure what a function does, try calling built-in function help which shows 
# documentation for any function (if documentation exists):
help(abs)

# Another built-in function is round() which by default rounds to the nearest integer:
round(3.14159)

# But can round to specified decimal places:
round(3.14159, 2)

# Lastly, there is the pow() function, which computes the power of a value:
pow(2, 4)     # 2 ** 4
pow(2, 4, 3)  # 2 ** 4 % 3

### Memory Addresses ##############################################################################

# You can discover the actual memory address of an object using built-in funciton id():
id(-9)
id(23.1)
shoe_size = 11.0
id(shoe_size)
id(abs)
id(round)

# A cache is a collection of data. Because small integers (up to about 250 or so, depending on the 
# Python version) are so common, Python creates those objects as it starts up and reuses the same 
# objects whenever it can. This speeds up operations involving these values:
i = 3
j = 3
k = 4 - 1
print(id(i), id(j), id(k)) # they all refer to the same object aka aliasing

# Larger integers and all floating-point values aren't necessarily cached. Python decides for 
# itself when to cache a value. 

### Defining Our Own Functions ####################################################################

# To define a function in Python:
# def <<function_name>>(<<parameters>>):
#     <<block>>
#     return <<expression>> # optional

# Keywords are words that Python reserves for its own use. We can't use them except as Python 
# intends: False, None, True, and, as, assert, break, class, continue, def, del, elif, else, 
# except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, 
# return, try, while, with, yield.

### Using Local Variables for Temporary Storage ###################################################

# Variables that are created within a function are called local variables. Local variables get 
# created each time that a function is called, and they are erased when the function returns (can't 
# be used outside of the function).

def quadratic(a: float, b: float, c: float, x: float) -> float:
    first = a * x ** 2
    second = b * x
    third = c
    return first + second + third

quadratic(2, 3, 5, 1.5)

# A function's parameters are also local variables. The area of a program that a variable can be 
# used in is called the variable's scope.

### Tracing Function Calls in the Memory Model ####################################################

# Whenever Python executes a function call, it creates a namespace (literally, a space for names) 
# in which to store local variables for that call. You can think of a namespace as a scrap piece of 
# paper; Python writes down the local variables on that piece of paper, keeps track of them as long 
# as the function is being executed, and throws that paper away when the function returns.

# Separately, Python keeps another namespace for variables created in the shell:
def f(x):
    x = 2 * x            # local x
    return x

x = 1                    # global x (different variable from local x)
x = f(x + 1) + f(x + 2)

print(x)

# Here are the rules to executing a function call:
#   1. Evaluate each argument one at a time, working left-to-right
#   2. Create a namespace to hold the function call's local variables (and parameters)
#   3. Pass the resulting values into the function
#   4. Execute the function

### Designing New Functions: A Recipe #############################################################

# Every time you write a function, you need to figure out the answers to the following:
#   1. What do you name the function?
#   2. What are the parameters, and what types of information do they refer to?
#   3. What calculations are you doing with that information?
#   4. What information does the function return?
#   5. Does it work like you expect it to?

# Python uses three quotation marks to start and end the function documentation, called a docstring 
# or documentation string.

def days_difference(day1: int, day2: int) -> int: # Type notations
    '''
    Return the number of days between day1 and day2, which are both in the range 1-365
    '''
    return day2 - day1

def get_weekday(current_weekday: int, days_ahead: int) -> int:
    '''
    Return which day of the week it will be days_ahead day from current_weekday day
    '''
    return (current_weekday + days_ahead - 1) % 7 + 1

def get_birthday_weekday(current_weekday: int, 
                         current_day: int, 
                         birthday_day: int) -> int:
    '''
    Return the day of the week it will be on birthday_day given that the day of the week is 
    current_weekday and the day of the year is current_day
    '''

    days_diff = days_difference(current_day, birthday_day)
    
    return get_weekday(current_weekday, days_diff)

### Writing and Running a Program #################################################################

# In order to have a program print the value of an expression to the terminal, we use the built-in 
# function print()

# If you don't have a return statement in a funciton it'll return None. You can also return None 
# yourself explicitly if you'd like. The value None is used to signal the absence of a value.

# If you made assumptions about the values of parameters or you know that your function won't work 
# with particular values, write a precondition to warn other programmers.
