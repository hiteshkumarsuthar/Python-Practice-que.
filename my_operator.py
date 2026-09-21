# """[Arithmetic Operators]
# Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication and division.

# In Python, the division operator (/) returns a floating-point result, while floor division (//) returns an integer result."""

# a = 15
# b = 4
# print("Addition", a + b)
# print("Substraction", a - b)
# print("Multiplication", a * b)
# print("Division", a / b)
# print("Floor Division", a // b)
# print("Modulas", a % b)
# print("Exponentiation", a ** b)

# """[Comparison Operators]
# Comparison(or Relational) operators compares values. It either returns True or False according to the condition."""

# a = 15
# b = 25
# print("Equal", a == b)
# print("not equal", a != b)
# print("Greater than", a > b)
# print("Less than", a < b)
# print("Greater than equal", a >= b)
# print("Less than equal", a <= b)

# """[Logical Operators]
# Logical operators perform Logical AND, Logical OR and Logical NOT operations. It is used to combine conditional statements.

# The precedence of Logical Operators in Python is as follows:

# Logical not
# logical and
# logical or"""

# a = True
# b = False
# print(a and b) # Dono conditions True honi chahiye.
# print(a or b) # Ek bhi condition True ho to result True hoga.
# print(not a) # Result ko ulta kar deta hai. 
# #              # True → False
# #              # False → True

# """[Bitwise Operators]
# Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.

# Bitwise Operators in Python are as follows:

# Bitwise NOT
# Bitwise Shift
# Bitwise AND
# Bitwise XOR
# Bitwise OR"""

# a = 10
# b = 4

# print(a & b)
# print(a | b)
# print(~a)
# print(a ^ b)
# print(a >> 2)
# print(a << 2)

# """[Assignment Operators]
# Assignment operators are used to assign values to the variables. This operator is used to assign the value of the right side of the expression to the left side operand. Example:"""

# a = 10
# b = a

# print(b)
# b += a   #add and assign
# print(b) 
# b -= a   #subtract and assign
# print(b)
# b *= a   #multiply and assign
# print(b)
# b /= a   # division and assign
# print(b)


# """[Identity Operators]
# "is" and "is not" are the identity operators and both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 

# is      ->    True if the operands are identical 
# is not  ->    True if the operands are not identical """

# a = 10
# b = 20
# c = a
# print(a is not b) # -> True
# print(a is c) # -> True


# """Membership Operators
# "in" and "not in" are the membership operators that are used to test whether a value or variable is in a sequence.

# in      ->     True if value is found in the sequence
# not in  ->     True if value is not found in the sequence"""

# x = 25
# y = 10
# my_list = [10, 20, 30, 40, 50]

# if(x not in my_list):
#     print("x is NOT in my list")
# else:
#     print("x is in my list")
# if("y in my_list"):
#     print("y is in my list")
# else:
#     print("y is NOT in my list")


# """[Ternary Operator]
# Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. 

# It simply allows testing a condition in a single line replacing the multiline if-else, making the code compact.

# Syntax :  [on_true] if [expression] else [on_false]"""

# a, b = 10, 20
# min = a if a < b else b

# print(min)

# """Precedence and Associativity of Operators
# [Operator Precedence]
# This is used in an expression with more than one operator with different precedence to determine which operation to perform first."""

# expr = 10 + 20 * 30
# print(expr)
# name = "Alex"
# age = 0

# if name == "Alex" or name == "John" and age >= 2:
#     print("Hello! Welcome.")
# else:
#     print("Good Bye!!")
    
# """"
# [Operator Associativity]
# If an expression contains two or more operators with the same precedence then Operator Associativity is used to determine. It can either be Left to Right or from Right to Left."""

# print(100 / 10 * 10)
# print(5 - 2 + 3)
# print(5 - (2 + 3))
# print(2 ** 3 ** 2)
