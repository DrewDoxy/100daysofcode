import random, hangman_words, hangman_art

print(hangman_art.logo)
word_list = hangman_words.word_list
stages = hangman_art.stages
chosen_word = random.choice(word_list)
end_of_game = False

display = []

word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"

lives = 6
while not end_of_game:
    guess = input("Please guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}.")
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(f"Incorrect! You guessed '{guess}', and you now have {lives} lives left.")

        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])





if "_" in display:
    print("You lost!")

print(f"The chosen word was {chosen_word}.")