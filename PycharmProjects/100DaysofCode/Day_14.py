#Import art and random functionality to use
import random, game_data_14


#Create a game loop function that ends when a player guesses the wrong answer
def higher_lower():
    score = 0
    still_playing = True
    while still_playing:
        print(game_data_14.logo)
        choice_A = random.randint(0, 50)
        choice_B = random.randint(0, 50)
        choice_A = game_data_14[choice_A]
        choice_B = game_data_14[choice_B]
        print(f"Compare A: {choice_A}")

        print(game_data_14.vs)
        print(f"Against B: {choice_B}")
        selection = input("Who has more followers? Type 'A' or 'B': ").lower()
        if selection == "a" and choice_A > choice_B:
            score += 1
            still_playing = True
        elif selection == "b" and choice_B > choice_A:
            score += 1
            still_playing = True
        else:
            still_playing = False

    print(f"Your final score was {score}")

higher_lower()

game_loop = input("Would you like to play again? Y/N ").lower()
if game_loop == "y":
    higher_lower()
#Get two random entries from the imported list/dictionary and print three out of the four keys

#Compare the IG follower key between the two values from the list/dictionary

#Add a point if the user guesses correctly and continue the game loop. End the game loop if they guess incorrectly.