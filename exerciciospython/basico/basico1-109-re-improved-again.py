'''109 - write a Python program to check if a number is positive, negative or zero.'''
number = int(input('Write a number: '))

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

def primo(number):
    mult = 0
    for count in range(2, number):  # transformar esse for em um list comprehension
        if (number % count == 0):
            print(f'it is multiple of {count}.')
            mult += 1
    if (mult == 0):
       return 'it is prime.'
    
print(f'The number is {number} and it is {check(number)} and {recheck(number)} and {primo(number)}')