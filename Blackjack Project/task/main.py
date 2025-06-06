import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_scores(cards):
    if sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        user_hand.remove(11)
        user_hand.append(1)
    else:
        return sum(cards)

def compare(score1, score2):
    if score1 == score2:
        if score1 and score2 == 0:
            print("Computer got a Blackjack.")
        else:
            print("It's a Draw.")
    elif score1 == 0:
        print("You got a Blackjack!")
    elif score2 == 0:
        print("Computer got a Blackjack.")
    elif score1 > 21:
        print("You went over 21.\nYou lose.")
    elif score2 > 21:
        print("Computer went over 21.\nYou Win!")
    else:
        if score1 > score2:
            print("You win!")
        elif score2 > score1:
            print("You Lose.")


#----------------------------------------------------------------------------
keep_playing = True
while keep_playing:
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
        if len(computer_hand) > 2:
            if computer_score == 0:
                print("Computer got a Blackjack.")
                game_over = True
        if user_score == 0:
            print("You got a Blackjack!")
            game_over = True
        elif user_score > 21:
            print("You got over 21.")
            game_over = True
        elif computer_score > 21:
            print("Computer went over 21. You Win!")
            game_over = True
        else:
            deal_new_card = input("Hit or Stop?: ").lower()
            if deal_new_card == "hit":
                user_hand.append(deal_card())
                calculate_scores(user_hand)
                calculate_scores(computer_hand)
                user_score = sum(user_hand)
                computer_score = sum(computer_hand)

                print(f"Your hand: {user_hand}, current score: {user_score}")
                print(f"Computer hand: {computer_hand[0]}")
                computer_hand.append(deal_card())

            else:
                computer_score = sum(computer_hand)
                print(f"Computer hand: {computer_hand}, score: {computer_score}")
                computer_hand.append(deal_card())
                compare(user_score, computer_score)
                game_over = True