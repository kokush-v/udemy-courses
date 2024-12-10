# TODO-1: Import and print the logo from art.py when the program starts.


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(encryption_mode, original_text, shift_amount):
    res = ''
    if encryption_mode == 'decode':
        shift_amount *= -1

    for x in original_text:
        try:
            alphabet_index = alphabet.index(x) + shift_amount
        except:
            res += x
            continue
        alphabet_length = len(alphabet)
        alphabet_index %= alphabet_length
        res += alphabet[alphabet_index]

    return res



# TODO-3: Can you figure out a way to restart the cipher program?


def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    res = caesar(original_text=text, shift_amount=shift, encryption_mode=direction)
    print(res)

while True:
    main()



