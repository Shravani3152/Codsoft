import string
import random
def generatePassword(length):
    characters = string.ascii_letters + string.digits + '!@#$%'
    password = ''
    for i in range(length):
        password += characters[random.randint(0,66)]
    print()
    print('-'*10)
    print(password)
    print('-'*10)
    print()
while True:
    print('Enter the given options')
    print('1. Generate Password\n2. Close ')
    action = int(input('Enter the option: '))
    if action == 1:
        length = int(input('Enter the length of the password: '))
        generatePassword(length)
    elif action == 2:
        print()
        print('-'*10)
        print('Closing the App!')
        print('-'*10)
        break 
