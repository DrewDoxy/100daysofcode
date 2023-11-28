import random, blackjack_art, os

############### Blackjack Project #####################


## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

def clear():
    print("\n" * 10)
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    sum(cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw"
    elif user_score == 0:
        return "You won with a Blackjack"
    elif computer_score == 0:
        return "The computer won with a blackjack"
    elif user_score > 21:
        return "You went over 21. That's a loss"
    elif computer_score > 21:
        return "The computer went over 21. You won"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"



def main_game_loop():
    print(blackjack_art.logo)
    user_cards = []
    computer_cards = []
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())



    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}. Your score: {user_score}.")
        print(f"Computer's first card: {computer_cards[0]}.")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_choice = input("Would you like to draw another card? Y/N ").lower()
            if user_choice == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}.\n Your final score: {user_score}.")
    print(f"The computer's final hand: {computer_cards}.\n The computer's final score: {computer_score}.")
    print(compare(user_score, computer_score))
while input("Do you want to play a game of blackjack? Y/N ").lower() == "y":
    clear()
    main_game_loop()
