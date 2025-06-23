#HIGHER OR LOWER
#Get instagram accounts & followers... create a dictionary???
#Who has more? A or B
    #Two random people from dictionary...
    #Format: Compare "Name", a "Description", from "Country"
#Evaluate answer
    #If correct, B becomes A and is compared to another... score + 1
    #If incorrect, game is over, "your score is"


from game_data import data #DICTIONARY KEYS: 'name'  'follower_count'  'description'  'country'
import art
import random


game = True
score = 0
answer_result = ""

#selects dictionary within list
a = data[random.randint(0, len(data))]
b = data[random.randint(0, len(data))]


#compare answer function:
def compare_answer():
    global game, score, answer_result, a, b
    guess = input("Who has more followers? 'A' or 'B':  ").lower()
    if guess == 'a' and a['follower_count'] > b['follower_count']:
        score += 1
        answer_result = f"Correct! Your score is now {score}"
        a = b
        b = data[random.randint(0, len(data))]
    elif guess == 'b' and b['follower_count'] > a['follower_count']:
        score += 1
        answer_result = f"Correct! Your score is now {score}"
        a = b
        b = data[random.randint(0, len(data))]
    elif guess != 'a' and guess != 'b': #if they've mistyped
        print("You have typed an invalid answer")
    else:
        play_again = input(
            f"You're wrong, game over! Your score was {score}. Would you like to play again? 'y' or 'n':  ").lower()
        if play_again == 'y':
            score = 0
            game_loop()
        else:
            game = False



def game_loop():
    global game, score, answer_result, a, b
    # print(art.logo)

    #game loop
    while game:
        #ensure a and b are not the same
        if a == b:
            b = data[random.randint(0, len(data))]

        print('\n', answer_result) #"Correct, your score is X"
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
        print(f"For Testing: {a['follower_count']} vs {b['follower_count']}")

        #comparing answer
        compare_answer()


game_loop()