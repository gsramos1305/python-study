import random
from operator import truediv


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_scores(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        user_hand.remove(11)
        user_hand.append(1)
    if sum(cards) == 21:
        return 0
    else:
        return sum(cards)


#----------------------------------------------------------------------------

user_hand = []
computer_hand = []
game_over = False


for n in range(2):
    user_hand.append(deal_card())
    computer_hand.append(deal_card())

user_score = calculate_scores(user_hand)
computer_score = calculate_scores(computer_hand)
print(f"Your hand: {user_hand}, current score: {user_score}")
print(f"Computer's first hand: {computer_hand[0]}")

while not game_over:
    if computer_score == 0:
        print("Computer got a Blackjack.")
        game_over = True
    elif user_score == 0:
        print("You got a Blackjack!")
        game_over = True
    elif user_score > 21:
        print("You got over 21.")
        game_over = True
    else:
        deal_new_card = input("Hit or Stop?: ").lower()
        if deal_new_card == "hit":
            user_hand.append(deal_card())
            calculate_scores(user_hand)
            user_score = sum(user_hand)
            print(f"Your hand: {user_hand}, current score: {user_score}")
            print(f"Computer hand: {computer_hand}, computer score {computer_score}")
            if len(user_hand) >= 3:
                computer_hand.append(deal_card())
        else:
            game_over = True
            