import random

choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors: "))

computer_choice = random.choice([0, 1, 2])

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if choice == 0:
    print(rock)
    if computer_choice == 0:
        print(rock)
        print("Draw")
    elif computer_choice == 1:
        print(paper)
        print("You Lose")
    else:
        print(scissors)
        print("You Win!")
elif choice == 1:
    print(paper)
    if computer_choice == 0:
        print(rock)
        print("You Win!")
    elif computer_choice == 1:
        print(paper)
        print("Draw")
    else:
        print(scissors)
        print("You Lose")
elif choice == 2:
    print(rock)
    if computer_choice == 0:
        print(rock)
        print("You Lose")
    elif computer_choice == 1:
        print(paper)
        print("You Win!")
    else:
        print(scissors)
        print("Draw")
else:
    print("Pick either 0, 1 or 2")
