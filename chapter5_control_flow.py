
#### Chapter 5: Making Choices ####################################################################

# Making choices: we do this whenever we want our program to behave differently depending on the 
# data it's working with. We'll introducestatements for making choices, called control flow 
# statements (because they control the way the computer executes programs).

### A Boolean Type ################################################################################

# Boolean type: in Python, there is a type called 'bool'. Unlike 'int' and 'float', 'bool' only has 
# two possible values: 'True' and 'False'

## Boolean Operators ******************************************************************************

# Boolean operators: there are only three basic boolean operators: 'and', 'or', and 'not'. 'not' 
# has the highest precedence, followed by 'and', then 'or'.

# 'not' is an unary operator: it is applied to just one value, like the negation in the expression 
# -(3 + 2). An expression involving not produces 'True' if the original value is 'False', and 
# vice-versa:
print(not True)
print(not False)

# We typically apply 'not' to a boolean variable or complex boolean expression. The same goes for 
# 'and' and 'or'.

# 'and' is a binary operator. It produces 'True' if both operands are 'True', and produces 'False' 
# otherwise:
print(True and True)
print(False and False)
print(True and False)
print(False and True)

# 'or' is also a binary operator. it produces 'True' if either operand is 'True', and it produces 
# 'False' only if both are 'False':
print(True or True)
print(False or False)
print(True or False)
print(False or True)

# The above 'or' definition is called 'inclusive or', since it allows both possibilities as well as 
# either. Sometimes 'or' can mean to be an 'exclusive or'. Unlike English, most programming 
# languages interpret 'or' as inclusive.

## Relational Operators ***************************************************************************

# Relational operators: typically boolean values are not written down directly in expressions but 
# rather created in expressions. The most common way to do this is by doing a comparison using 
# relational operators:
#   >     greater-than
#   <     less-than
#   >=    greater-than or equal to
#   <=    less-than or equal to
#   ==    equal to
#   !=    not equal to

# All relational operators are binary operators: they compare two values and produce 'True' or 
# 'False' as appropriate:
print(45 > 34)
print(45 > 79)

# To achieve an 'exclusive or', you may use the following:
print(True != True)
print(True != False)
print(False != True)
print(False != False)

## Combining Comparisons **************************************************************************

# Combining operators:
#   Arithmetic operators have higher precedence than relational operators.
#   Relational operators have higher precedence than boolean operators.
#   All relational operators have the same precedence.

# It's very common in math to check whether a value lies in a certain range:
x = 3
print(1 < x and x < 5)

# However, you can chain the comparisons in Python:
print(1 < x < 5)

# Python treats 0 and 0.0 as 'False' and treats all other numbers as 'True':
print(not 0, not 1, not -34.2)

# Similarly, the empty string is treates as 'False' and all other strings are treated as 'True':
print(not '', not 'hello', not 'world')

# In general, you should only use boolean operators on boolean values.

## Short-Circuit Evaluation ***********************************************************************

# When Python evaluates an expression containing 'and' or 'or', it does so from left to right. As 
# soon as it knows enough to stop evaluating, it stops (even if some operands haven't been looked 
# at yet). This is called short-circuit evaluation.

# In an 'or' expression, if the first operand is 'True', we know that the expression is 'True' and 
# so Python stops evaluating the expression. 

## Comparing Strings ******************************************************************************

# Comparing strings: it's possible to compare strings as you would numbers. The characters in 
# strings are represented by integers as directed by ASCII. One of the most common reasons to 
# compare two strings is to decide which one comes first alphabetically (known as dictionary 
# ordering or lexicographic ordering).

# Python decides which string is greater than which by comparing corresponding characters from left 
# to right. If the character from one string is greater than the second string, then the first 
# string is greater than the second string.

# If all the characters are the same, the two strings are equal; if one string runs out of 
# characters while the comparison is being done, then it is less.

# Python provides an operator that checks whether one string appears inside another one. The 'in' 
# operator produces 'True' exactly when the first string appears in the second string. The 
# operation is case sensitive:
print('Jan' in '01 Jan 1838')

# The empty string is always a subset of every string:
print('' in 'hello world')

# The 'in' operator is also applied to other types, as we'll see later.

### Choosing Which Statements to Execute ##########################################################

# An 'if' statement lets you change how your program behaves based on a condition. The general form 
# of an 'if' statement is as follows:
# if <<condition>>:
#     <<block>>

# The condition is an expression, such as "color != 'neon green'". Note that the expression does 
# not need to be a boolean one.

# If the condition is true, the statements in the block are executed, otherwise they are not:
ph = 8.0

if ph < 7.0:
    print(ph, 'is acidic.')

if ph > 7.0:
    print(ph, 'is basic.')

# If we have multiple cases, we can use 'else if' blocks instead. The difference is that with 
# several 'if' blocks each one is checked (regardless if the first one is true or not), whereas 
# with 'else if' blocks if the first 'if' block is true, then the subsequent 'elif' blocks are not 
# checked:
elif ph > 7.0:
    print(ph, 'is basic.')

# As a rule of thumb, if two conditions are related, use 'if/elif' blocks. Optionally (but very 
# usefully) we can add an 'else' clause at the end of the chain for situations that are outside of 
# the preceding 'if/elif' blocks:
else:
    print(ph, 'is neutral.')

# An 'if' statement can have at most one 'else' clause, and it has to be the final clause in the 
# statement.

### Nested if Statements ##########################################################################

# An 'if' statement's block can contain any type of Python statement, including another 'if' 
# statement, called a 'nested if' statement:
value = input('Enter the pH level: ')
if len(value) > 0:
    ph = float(value)
    if ph < 7.0:
        print(ph, 'is acidic.')
    elif ph > 7.0:
        print(ph, 'is basic.')
    else:
        print(ph, 'is neutral.')
else:
    print('No pH value was given!')

### Remembering Results of a Boolean Expression Evaluation ########################################

# Results of a boolean expression can be saved to a variable:
x = 15 > 5

# The most common situation in which you would want to do this comes up when translating decision 
# tables into software:
age: int = 30
bmi: float = 23.1

if age < 45:
    if bmi < 22.0:
        risk = 'low'
    else:
        risk = 'medium'
else:
    if bmi < 22.0:
        risk = 'medium'
    else:
        risk = 'high'

# Note that the expression 'bmi < 22.0' is used multiple times. To simplify this code, we can 
# evaluate each of the boolean expressions once, create variables that refer to the values
# produced those expressions, and use those variables:
young: bool = age < 45
slim: bool = bmi < 22.0
if young:
    if slim:
        risk = 'low'
    else:
        risk = 'medium'
else:
    if slim:
        risk = 'medium'
    else:
        risk = 'high'
