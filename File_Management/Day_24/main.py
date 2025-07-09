#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


with open('./Input/Names/invited_names.txt') as names:
    names = names.readlines()

#replaces the line break string in the list...
names = [n.replace('\n', '') for n in names]


# saves letters to variable
with open('./Input/Letters/starting_letter.txt', mode='r') as letters:
    base_letter = letters.read()
    for i in names:
        new_letter = base_letter.replace('[name]', i)
        with open(f'./Output/ReadyToSend/letter_for_{i}.docx', mode='w') as completed_letter:
            completed_letter.write(new_letter)

        #wasn't sure about saving new letters individually... but looks like the f-string with index sorts that



#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp