#rot13_lab_13_myversion.py
def encode13(message):
    output_message = ""
    english_alphabet = "abcdefghijklmnopqrstuvwxyz"
    rot13 = "nopqrstuvwxyzabcdefghijklm"
    for char in message:
        # print(char)
        if char in english_alphabet:
            index = english_alphabet.find(char)
            # print(index)
            encoded_character = rot13[index]
            # print(encoded_character)
            output_message += encoded_character
            # print(output_message)
        else:
            output_message += char
            # print(f"{output_message}")
    print(output_message)

abc = encode13('abc') #nop
print(abc)
encode13('xyz') #nop

user_in = input('Enter a message to decode: ')
encode13(user_in.lower())

# encode13(output_message)

# def decode13(message):
    # output_message = ""
    # for char in message:
        # if char in rot13
