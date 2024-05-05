import string

# Caesar Cipher

alphabet = list(string.ascii_lowercase)


def encrypt(message, shift):
    encrypted_message = ""
    for letter in message:
        position = alphabet.index(letter)
        encrypted_message += alphabet[(position + shift) % len(alphabet)]
    return encrypted_message


def decrypt(message, shift):
    decrypted_message = ""
    for letter in message:
        position = alphabet.index(letter)
        decrypted_message += alphabet[((position - shift) + len(alphabet)) % len(alphabet)]
    return decrypted_message


end_program = False
while not end_program:
    message = input("Type your message: ")
    shift = int(input("Type the shift: "))
    mode = input("Type encrypt or decrypt: ")
    if mode == "encrypt":
        encrypted_message = encrypt(message, shift)
        print(encrypted_message)
    else:
        decrypted_message = decrypt(message, shift)
        print(decrypted_message)
    print("Do you want to continue? ", end="")
    if input("y/n\n") == "y":
        end_program = False
    else:
        end_program = True

