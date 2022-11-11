'''109 - write a Python program to check if a number is positive, negative or zero.'''
number = float(input('Write a number: '))
if number == 0:
    print('Zero')
elif number < 0:
    print('Negative')
else:
    print('Positive')
