import pandas as pd
import random
import smtplib
import datetime as dt
import os
##################### Extra Hard Starting Project ######################
my_email = 'chrishaz3ll@gmail.com'
password = 'ifonenjqselafccv'
global new_letter

# 1. Update the birthdays.csv
birthdays = pd.read_csv('birthdays.csv')
birthdays = birthdays.to_dict(orient='records')
print(birthdays)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
list_letters = []
for file in os.listdir('letter_templates'):
    if file.endswith('txt'):
        list_letters.append(file)

if month == birthdays[0]['month']:
    letter_number = random.randint(0, len(list_letters))
    print('yes')
    with open(f'letter_templates/{list_letters[letter_number]}', 'r') as letter:
        new_letter = letter.read()

    new_letter = new_letter.replace('[NAME]', birthdays[0]['name'])


# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr= my_email,
                        to_addrs= 'chrishaz3ll@yahoo.co.uk',
                        msg=f'Subject: Happy Birthday\n\n{new_letter}')



