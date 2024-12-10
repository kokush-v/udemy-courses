#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def create_letters(names, template):
    for name in names:
        new_letter = template.replace("[name]", name)
        with open(f'Output/ReadyToSend/{name}Letter.txt', mode='w') as new_file:
            new_file.write(new_letter)


with open('Input/Letters/starting_letter.txt') as template_file:
    message_template = template_file.read().strip()

with open('Input/Names/invited_names.txt') as name_list_file:
    invited_names = name_list_file.read().split('\n')

create_letters(names=invited_names, template=message_template)