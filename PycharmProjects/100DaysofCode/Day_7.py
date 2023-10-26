import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"The chosen word is {chosen_word}.")
display = []

for i in range(len(chosen_word)):
    display[len(chosen_word)] == "_"

print(display)

#guess = input("Please guess a letter: ").lower()

#for letter in chosen_word:
 #   if letter == guess:
  #      print("Right")
   #     lives += 1
    #else:
     #   print("Wrong")
      #  lives += 1
