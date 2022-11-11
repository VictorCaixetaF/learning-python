'''109 - write a Python program to check if a number is positive, negative or zero.'''
number = float(input('Write a number: '))

def check(number):
    if number == 0:
        return 'Zero'
    elif number < 0:
        return 'Negative'
    else:
        return 'Positive'

print(f'The number is {number} and it is {check(number)}')