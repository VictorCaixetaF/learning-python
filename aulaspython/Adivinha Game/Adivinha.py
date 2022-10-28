import random
print('Discovery the secret number between 1 to 100 !')
print()
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, Too low.')
        elif guess > random_number:
            print ('Sorry, Too high.')
    print(f'Wow! Congrats. You have guessed the corrected number {random_number}!')
guess(100)

