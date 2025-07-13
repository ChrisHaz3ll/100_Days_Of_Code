# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
# # student_data_frame = pd.DataFrame(student_dict)
# #Loop through rows of a data frame


# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_data = pd.read_csv('nato_phonetic_alphabet.csv')

# nato_dict = {d['letter']:d['code'] for d in nato_data.to_dict(orient='records')}
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = list(input('Enter a Word:  ').upper())
user_nato = [nato_dict[item] for item in user_input if item in nato_dict]
print(user_nato)