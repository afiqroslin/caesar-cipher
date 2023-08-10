import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(logo.art)


def caesar(direction, text, shift):
    cipher_text = ""  # encrypted text string
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)              # find alphabet index position of the text
            if direction == "encode":
                caesar_direction = "Encoded"
                position_encrypt = position + shift      # add position with how many shifts
            elif direction == "decode":
                caesar_direction = "Decoded"
                position_encrypt = position - shift
            encrypt_letter = alphabet[position_encrypt]  # encrypted letter with new shifted position
            cipher_text += encrypt_letter                # add the letters into encypted text
        else:
            cipher_text += char
    print(f"{caesar_direction} text is {cipher_text}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != "encode" and direction != "decode":     # if user choice is not encode/decode, it is invalid
        print("Invalid encryption type")
        continue                # repeat the loop again until user insert right choice
    else:                       # if user made right choice, execute next instruction
        text = input("Type your message:\n").lower()        # take text to be de/encode
        shift = int(input("Type the shift number:\n"))      # take how many alphabet shift user wants
        shift = shift % 26                                  # for big shift number, take the remainder as position
        caesar(direction, text, shift)
        repeat = input("Do you want to go again? Yes or No\n").lower()
        if repeat == "yes":
            continue
        elif repeat == "no":
            print("Goodbye")
            break

# def encrypt(plain_text, number_shift):
#   cipher_text = ""  #encrypted text string
#   for letter in plain_text:
#     position = alphabet.index(letter)  #find alphabet index position of the text
#     position_encrypt = position + shift  #add position with how many shifts
#     encrypt_letter = alphabet[position_encrypt]  #encrypted letter with new shifted position
#     cipher_text += encrypt_letter  #add the letters into encypted text
#   print(f"Encoded text is {cipher_text}")

# def decrypt(cipher_text, number_shift):
#   cipher_text = ""  #encrypted text string
#   for letter in cipher_text:
#     position = alphabet.index(letter)  #find alphabet index position of the text
#     position_encrypt = position - shift  #add position with how many shifts
#     encrypt_letter = alphabet[position_encrypt]  #encrypted letter with new shifted position
#     cipher_text += encrypt_letter  #add the letters into encypted text
#   print(f"Decoded text is {cipher_text}")

# if direction == "encode":
#   encrypt(plain_text=text, number_shift=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, number_shift=shift)
