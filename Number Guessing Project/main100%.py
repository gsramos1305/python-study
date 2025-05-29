from random import randint
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def difficulty():
    level = input("---set a difficulty--- Easy or hard: ").lower()
    if level == 'easy':
        return EASY_LEVEL
    elif level == 'hard':
        return HARD_LEVEL

def compare(u_guess, c_guess, turns):
    if u_guess > c_guess:
        print("Too high.")
        return turns - 1
    elif u_guess < c_guess:
        print("Too low")
        return turns - 1
    else:
        print("You got it!")

def playgame():
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    turns = difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining.")
        guess = int(input("Guess it: "))
        turns = compare(guess, answer, turns)
        if turns == 0:
            print("You lost.")

playgame()