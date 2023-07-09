
#### Chapter 4: Working with Text #################################################################

### Creating Strings of Characters ################################################################

# In Python, text is represented as a string, which is a sequence of characters (letters, digits, 
# symbols):

# Single quote string
print('Aristotle')

# Double quote string
print('Isaac Newton')

# Strings can contain any number of characters, limited only by computer memory.

# Shortest is the empty string
print('')

## Operations on Strings **************************************************************************

# Python has a built-in function that returns the length of a string:
len('Albert Einstein')

# We can add two strings using the '+' operator:
print('Albert' + ' Einstein')

# The above is an example of operator overloading, which is when an operator has more than one 
# operation associated with it. So '+' can perform addition with numbers and concatenation with 
# strings.

# When using '+' the two inputs must be of the same type (numerical or string).

# You can convert an object to a string using str():
str(7)

# Functions int() and float() can convert numerical strings to numbers:
int('1')
float('5.24')

# A string can be repeated using the operator '*' and an integer:
print('AT' * 5)

# If the number provided is less than or equal to 0 is will return an empty string:
print('GC' * 0)

# Strings are values, so you can assign a string to a variable:
sequence = 'ATTGTCCCC'
len(sequence)

new_sequence = sequence + 'GGCCTCCTGC'
print(new_sequence)

### Using Special Characters in Strings ###########################################################

# When you want to use a single quote character in a single quote string (or a double quote 
# character in a double quote string) you can preface it with a backward slash character '\'. The 
# backslash is called an escape character, and the combination of the backslash and the single 
# quote is called an escape sequence. The name comes from the fact that we're escaping from 
# Python's usual syntax rules for a moment. When Python sees a backslash inside a string, it means 
# that the next character represents something that Python normally uses for other purposes, such 
# as marking the end of a string.

# The escape sequence \' is indicated using two symbols, but those two symbols represent a single 
# character:
print(len('\''))
print(len('it\'s'))

# Python recognizes several escape sequences:
#   \'    single quote
#   \"    double quote mark
#   \\    backslash
#   \t    tab
#   \n    newline
#   \r    carriage return

## Creating a Multiline String ********************************************************************

# If you create a string using single or double quotes, the whole string must fit onto a single 
# line (on the interpreter or in your editor). To span multiple lines, put three single quotes (or 
# double quotes) around the string:
multi_line_string = '''
this is a multiline string
'''

# Each of the three major operating systems uses a different set of characters to indicate the end 
# of a line (EOL). On Linux/MacOS it is \n and on pre-Unix MacOS it was \r, and on Windows it is 
# \r\n. Python always uses a single \n to indicate a newline, even on operating systems like 
# Windows that do things differently. This is called normalizing the string; Python does this so 
# that you can write exactly the same program no matter what kind of machine you're running on.

### Printing Information ##########################################################################

# Printing information: we use the print() function to display messages to the users of our 
# program. Those messages may include the values that expressions produce or the values that the 
# variables refer to. 

# When printing strings, it will strip off the quote marks and present the string in a human 
# readable form.
print('The Latin \"Oryctolagus cuniculus\" means \"domestic rabbit.\"')

# When Python prints a string, any escape sequences are converted to a form that humans expect. The 
# print() function takes a comma-separated list of values and prints the values with a single space 
# between them and then a newline after the last value:
print(1, 2, 3)

# When called with no arguments (a list of values with length zero), print() ends the current line 
# and moves to the next one (prints empty line):
print(2, 4, 6)
print()
print(1, 3, 5)

# The print() function can print values of any type and even print values of different types within
# the same call:
print('1', 2, 3.0)

# May also print variables and expressions:
radius = 5
print('The diameter of the circle is', radius*2, 'cm.')

# The parameters sep, end, file, and flush have assignment statements in the function header. These 
# are called default parameter values: by default, if we call print() with a comma-separated list 
# of values, the separator is a space.

# We can supply different values by using keyword arguments (kwargs). That is a term for assigning 
# a value to a parameter name in the function call:
print('a', 'b', 'c', sep=', ')

### Getting Information from the Keyboard #########################################################

# Another built-in function is input, which reads a single line of text from the keyboard. It 
# returns whatever the user enters as a string:
species = input()
print(type(species))

# input() can be given a string argument, which is used to prompt the user for input:
species = input('Please enter a species: ')
print(species)

