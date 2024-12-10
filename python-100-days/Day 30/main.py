import pandas

nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

while True:
    name = input("What is your name?")
    try:
        nato_name = [nato_dict[letter.upper()] for letter in name]
    except KeyError:
        print("Use only alphabet symbols")
    else:
        print(nato_name)
        break