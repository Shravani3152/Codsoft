import math
def add(a,b):
    return a+b 

def subtract(a, b):
    return a - b 

def multiply(a, b):
    return a * b 

def divide(a, b):
    return a /  b 

def sqrt(a): 
    return math.sqrt(a)

while True:
    print('Please enter the given below options')
    print('1. Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Square root\n6.Close App')
    action = int(input('Enter the option: '))
    if action == 1:
        a = float(input('Enter number 1: '))
        b = float(input('Enter numeber 2: '))
        print()
        print('-'*10)
        print(add(a,b))
        print('-'*10)
        print()
    elif action == 2:
        a = float(input('Enter number 1: '))
        b = float(input('Enter numeber 2: '))
        print()
        print('-'*10)
        print(subtract(a,b))
        print('-'*10)
        print()
    elif action == 3:
        a = float(input('Enter number 1: '))
        b = float(input('Enter numeber 2: '))
        print()
        print('-'*10)
        print(multiply(a,b))
        print('-'*10)
        print()
    elif action == 4:
        a = float(input('Enter number 1: '))
        b = float(input('Enter numeber 2: '))
        print()
        print('-'*10)
        print(divide(a,b))
        print('-'*10)
        print()
    elif action == 5:
        a = float(input('Enter number: '))
        print()
        print('-'*10)
        print(sqrt(a))
        print('-'*10)
        print()
    elif action == 6:
        print()
        print('-'*10)
        print('Closing the app')
        print('-'*10)
        break 
