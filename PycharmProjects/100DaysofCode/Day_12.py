from number_guessing_art import logo
import random, os


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0
def clear():
    print("\n" * 10)

def check_answer(guess, answer, turns):
    """Checks answer against guess, returns turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
        #print(f"You have {turns} attempts left.")
    elif guess < answer:
        print("Too low.")
        return turns - 1
        #print(f"You have {turns} attempts left.")
    else:
        print(f"That's correct! You guessed the right number! The answer was {answer}")

def set_difficulty():
    difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS

def play_game():
    numbers = list(range(0, 101))
    print(logo)

    print("Welcome to the Number Guessing game!\nI'm thinking of a number between 1 and 100.")

    answer = random.choice(numbers)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} tries left.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses; you lose.")
            return
        elif guess != answer:
            print("Guess again.")
        if guess == answer:
            choice = input("Would you like to play again? Y/N: ").lower()
            if choice == "y":
                clear()
                play_game()
            else:
                print("Thanks for playing!")
                return

play_game()