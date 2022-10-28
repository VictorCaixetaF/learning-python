import random
print('I.A. Please, discovery the secret number between 1 to 100 !')
print()
def computer_guess(x):
    low = 1
    high = x
    feedback =''
    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high(h), too low(l) or correct (c)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Wow! The computer guessed the correct number {guess}!')
computer_guess(100)
