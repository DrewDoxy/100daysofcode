#Import art and random functionality to use
import random, game_data_14

def clear():
    print("\n" * 10)

def format_function(choice):
    """Format data into a printable format"""
    account_name = choice["name"]
    account_desc = choice["description"]
    account_country = choice["country"]
    return(f"{account_name}, a[n] {account_desc}, from {account_country}")

def check_answer(guess, a_followers, b_followers):
    """Take the user guess plus the follower counts and return if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
#Create a game loop function that ends when a player guesses the wrong answer
def higher_lower():
    print(game_data_14.logo)
    score = 0
    still_playing = True
    choice_B = random.choice(game_data_14.data)
    while still_playing:
        choice_A = choice_B
        choice_B = random.choice(game_data_14.data)
        while choice_A == choice_B:
            choice_B = random.choice(game_data_14.data)

        print(f"Compare A: {format_function(choice_A)}. ")

        print(game_data_14.vs)
        print(f"Against B: {format_function(choice_B)}. ")
        selection = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers = choice_A["follower_count"]
        b_followers = choice_B["follower_count"]
        is_correct = check_answer(selection, a_followers, b_followers)
        clear()
        if is_correct:
            score += 1
            still_playing = True
            print(f"That's correct. You have {score} point[s].")
        else:
            print(f"Sorry, that's wrong.")
            still_playing = False

    print(f"Your final score was {score} points.")

higher_lower()

game_loop = input("Would you like to play again? Y/N ").lower()
if game_loop == "y":
    higher_lower()

