
import pandas as pd
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_data = pd.read_csv('nato_phonetic_alphabet.csv')

# nato_dict = {d['letter']:d['code'] for d in nato_data.to_dict(orient='records')}
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#TODO 3: Exception
def generate_nato():
    user_input = list(input('Enter a Word:  ').upper())
    try:
        user_nato = [nato_dict[item] for item in user_input]
    except KeyError:
        print('Only input letters in the alphabet')
        generate_nato()
    else:
        print(user_nato)

generate_nato()