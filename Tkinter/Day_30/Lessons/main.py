
#FileNotFoundError
# with open('a_file.txt') as file:
#     file.read()

#KeyError
# a_dictionary = {'key': 'value'}
# value = a_dictionary['non_key']

#IndexError
# n_list = [1,2,3]
# n = n_list[4]

#TypeError
# text = 'abcd'
# print(text + 3)



# TODO: Catching Exceptions
# try: #something that might cause exception
#     file = open('a_file.txt')
#     a_dictionary = {'key': 'value'}
#     value = a_dictionary['key']
# except FileNotFoundError: #do this if there was an exception
#     file = open('a_file.txt', 'w')
#     file.write('add something')
# except KeyError as error_message:
#     print(f'the key {error_message} does not exist')
# else: #do this if no exceptions
#     content = file.read()
#     print(content)
# finally: #do this no matter what happens
#     raise TypeError('This is an error (maybe)...') #raises on exception

# TODO: Raise Own Exception
height = float(input('Height in m:  '))
weight = int(input('Weight in kg:  '))

if height > 3:
    raise ValueError('Height value is unrealistic')

bmi = weight / height**2
print(bmi)
