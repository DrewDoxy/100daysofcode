import cipher_art

print(cipher_art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(start_text, shift_amount, cipher_direction):
        new_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                new_text += alphabet[new_position]
            else:
                new_text += char
        print(f"The {cipher_direction}d text is {new_text}.")


still_going = True
while still_going:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    choice = input("Would you like to play again? Yes or no. ").lower()
    if choice == "yes":
        still_going = True
    else:
        still_going = False
        print("Goodbye!")


