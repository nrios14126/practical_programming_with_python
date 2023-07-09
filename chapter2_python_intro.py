
#### Chapter 2: Hello Python ######################################################################

### What is a Type? ###############################################################################

# In Python, a type consists of two things:
#   1. a set of values
#   2. a set of operations that can be applied to those values

# int type and their operations (same for float types):
1 + 1  # addition
1 - 1  # subtraction
1 * 1  # multiplication
1 / 1  # division (always returns float type)
1 // 1 # integer division
1 % 1  # modulo
1 ** 1 # exponentiation

## Finite Precision *******************************************************************************

# Computers have a finite amount of memory and (to make calculations fast and memory efficient), so 
# most programming languages limit how much information can be stored for any single number.
2 / 3
5 / 3

## Operator Precedence ****************************************************************************

# Python follows the PEMDAS order of operations (negation is after exponentiation).
-2 ** 4   # -16
-(2 ** 4) # -16
(-2) ** 4 # 16

# Operations are applied left to right (except exponentiation, which is right to left).
(212 - 32) * 5 / 9
2 ** 3 ** 2          # 512, not 64

# It's a good rule to parenthesize complicated expressions even if not needed, but to also not 
# parenthesize simple expressions.

### Variables and Computer Memory #################################################################

# A name that refers to a value is called a variable.
#   1. Can contain letters, numbers, and underscores
#   2. Cannot begin with numbers

# In Python, you create a new variable by assigning it a value.
degrees_celsius = 26.0

# Whenever Python sees a variable in an expression, it substitutes the value to which the variable 
# refers:
9 / 5 * degrees_celsius + 32

# Variables are so-called because their values can vary as the program executes:
degrees_celsius = 0.0
9 / 5 * degrees_celsius + 32

# Assigning a value to a variable that already exists doesn't create a second variable. Instead, 
# the existing variable is reused (refers to its new value, not the old value).

# The symbol '=' does not means 'equals' in Python as it does in math. Instead, we say 'x is 
# assigned 12' or 'x gets 12':
x = 12

## Values, Variables, and Computer Memory *********************************************************

# Every location in the computer's memory has a memory address that uniquely identifies that 
# location. During execution of a program, every value that Python keeps track of is stored inside 
# an object in computer memory. An object is a value at a memory address with a specified type. 

# In our memory model, a variable contains the memory address of the object to which it refers: 
#   degrees_celsius(id1) -> id1(float, 26.0)
#   value 26.0 has the memory address id1
#   the object at the memory address id1 has type float and the value 26.0
#   variable degrees_celsius contains the memory address id1
#   variable degrees_celsius refers to the value 26.0

# Whenever Python needs to know which value degrees_celsius refers to, it looks at the object at 
# the memory address that degrees_celsius contains.

## Assignment Statement ***************************************************************************

# Assignment statement: <<variable>> = <<expression>>
#   1. Evaluate the expression to get value; this value has a memory address
#   2. Store the memory address of the value to the variable

## Reassigning to Variables ***********************************************************************

# Note that assigning to a variable does not change any other variable:
difference = 20
double = 2 * difference
double                   # 40
difference = 5
double                   # still 40, not 10

## Augmented Assignment ***************************************************************************

# An augmented assignment combines an assignment statement with an operator to make the statement 
# more concise. Same as d = d * (3 + 4), expression is evaluated first then operation with d is 
# applied:
d = 2
d += 3 + 4 
d

# Can be done with the following operations:
x = 7
x += 2
x -= 2
x *= 2
x /= 2
x //= 2
x %= 2
x **= 2

### How Python Tells You Something Went Wrong #####################################################

# Broadly speaking, there are two types of errors in Python:

# Syntax errors, which happen when you type something that isn't valid Python code. Assigning a 
# variable name to a literal will yield a syntax error:
# 12 = x

# A literal is any value (like 5 or 12.7)

# Semantic errors, which happen when you instruct Python to do something it can't do like divide by 
# zero or use a variable that doesn't exist:
# x = 7
# print(x / 0, x / y) 

# In Python, in order to split up a statement into more than one line:
#   1. Make sure your line break occurs inside parentheses
#   2. Use the line-continuation character \

# inside parentheses
print(2 
    + 3 
    + 4 
    + 5)

# using backslash
print(2 \
    + 3 \
    + 4 \
    + 5)
