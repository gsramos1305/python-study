import random

def deal_card():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)

    return card

user_hand = []
computer_hand = []

for n in range(2):
    new_card = deal_card()
    user_hand.append(new_card)
    computer_hand.append(new_card)


def calculate_scores(cards):
