'''109 - write a Python program to check if a number is positive, negative or zero.'''
number = float(input('Write a number: '))

def check(number):
    if number == 0:
        return 'Zero'
    elif number < 0:
        return 'Negative'
    else:
        return 'Positive'

def recheck(number):
    if number == 0:
        return 'Zero'
    elif number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

print(f'The number is {number} and it is {check(number)} and {recheck(number)}')