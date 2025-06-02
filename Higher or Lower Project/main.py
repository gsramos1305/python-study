import random
from game_data import data
from art import logo, vs

def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, {account_description}, {account_country}."


def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == 'a'
    elif b_followers > a_followers:
        return user_guess == 'b'

score = 0
should_continue = True
account_b = random.choice(data)


while should_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(format_data(account_a))
    print(vs)
    print(format_data(account_b))

    guess = input("Who has more followers? a or b: ").lower()
    print('\n' * 20)

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"Correct. Score: {score}")
    else:
        print(f"Wrong. Score: {score}")
        should_continue = False
