import random

guess = int(input('Guess a number between 1 to 10: \n'))
pcGuess = random.randint(1, 10)

while  guess != pcGuess:
    if guess < pcGuess:
        print('Guess Higher')
    elif guess > pcGuess:
        print('Guess Lower')
    guess = int(input('Guess a number between 1 to 10: \n'))

print('Right!')