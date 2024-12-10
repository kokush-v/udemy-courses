# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
#Loop through rows of a data frame
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
name = input("What is your name?")
nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}
nato_name = [nato_dict[letter.upper()] for letter in name]
print(nato_name)