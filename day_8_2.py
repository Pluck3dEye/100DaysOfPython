import string

# Caesar Cipher

alphabet = list(string.ascii_lowercase)


# def encrypt(message, shift):
#     encrypted_message = ""
#     for letter in message:
#         position = alphabet.index(letter)
#         encrypted_message += alphabet[(position + shift) % len(alphabet)]
#     return encrypted_message
#
#
# def decrypt(message, shift):
#     decrypted_message = ""
#     for letter in message:
#         position = alphabet.index(letter)
#         decrypted_message += alphabet[((position - shift) + len(alphabet)) % len(alphabet)]
#     return decrypted_message


def caesar(message_, shift_, mode_):
    new_message = ""
    if mode_ == "encrypt":
        for letter in message_:
            position = alphabet.index(letter)
            new_message += alphabet[(position + shift_) % len(alphabet)]
    if mode_ == "decrypt":
        for letter in message_:
            position = alphabet.index(letter)
            new_message += alphabet[((position - shift_) + len(alphabet)) % len(alphabet)]
    return new_message


end_program = False
while not end_program:
    message = input("Type your message: ")
    shift = int(input("Type the shift: "))
    mode = input("Type encrypt or decrypt: ")
    message = caesar(message, shift, mode)
    print(message)
    print("Do you want to continue? ", end="")
    if input("y/n\n") == "y":
        end_program = False
    else:
        end_program = True

