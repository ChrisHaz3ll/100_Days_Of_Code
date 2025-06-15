alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def encrypt(original_text, shift_amount):
    encoded_text = ''
    for letter in original_text: #loop through input
        # alphabet.index(letter) #find input of letter, returns int
        new_index = alphabet.index(letter) + shift_amount # shift amount to index of letter, returns int
        new_index %= len(alphabet) #makes sure you're always in index range, work around IndexError
        encoded_text += alphabet[new_index] #add new letter with shifted index to string, returns str
    print(f"Your message is: {encoded_text}")

def decrypt(original_text, shift_amount):
    decoded_text = ''
    for letter in original_text:
        new_index = alphabet.index(letter) - shift_amount
        new_index %= len(alphabet)
        decoded_text += alphabet[new_index]
    print(f"Your message is: {decoded_text}")

def caesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)

caesar()




