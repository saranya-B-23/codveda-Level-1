"""
Level 1:
Task 1: Develop a basic calculator that can perform four primary arithmetic operations: addition, subtraction, multiplication and Division.
"""

# define functions for each operation
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return 'Error: Division by zero is not possible.'
    return a/b

# Take input from the user
print("select operation (+,-,*,/)")
operation = input('Enter the operation: ')
n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))

# performing operation
if operation == "+":
    print(f'Addition of {n1} and {n2} is {add(n1,n2)}')
elif operation == "-":
    print(f'Subtraction of {n1} and {n2} is {sub(n1,n2)}')
elif operation == "*":
    print(f'Multiplication of {n1} and {n2} is {mul(n1,n2)}')
elif operation == "/":
    print(f'Division of {n1} and {n2} is {div(n1,n2)}')
else:
    print('Invalid operation!!!, please select a valid operation.')
