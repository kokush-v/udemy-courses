alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def encrypt(original_text, shift_amount):
#     res = ''
#     for x in original_text:
#         alphabet_index = alphabet.index(x) + shift_amount
#         alphabet_length = len(alphabet)
#         alphabet_index %= alphabet_length
#         res += alphabet[alphabet_index]
#     print(res)
#
# def decrypt(encrypted_text, shift_amount):
#     res = ''
#     for x in encrypted_text:
#         alphabet_index = alphabet.index(x) - shift_amount
#         alphabet_length = len(alphabet)
#         alphabet_index %= alphabet_length
#         res += alphabet[alphabet_index]
#     print(res)

def ceaser(encryption_mode, original_text, shift_amount):
    res = ''
    if encryption_mode == 'decode':
        shift_amount *= -1

    for x in original_text:
        alphabet_index = alphabet.index(x) + shift_amount
        alphabet_length = len(alphabet)
        alphabet_index %= alphabet_length
        res += alphabet[alphabet_index]

    print(res)


ceaser(original_text=text, encryption_mode=direction, shift_amount=shift)