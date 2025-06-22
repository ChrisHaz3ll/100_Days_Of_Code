import random
#GUESS THE NUMBER
#Thinking of number between 1 and 100
#Easy = 10 guesses
#Hard mode = 5 guesses
numbers = list(range(1,101))

lives_left = 0

#begin guessing number
def number_guesser():
    correct_answer = random.choice(numbers)
    # print(f"For testing, correct answer is: {correct_answer}")
    global lives_left
    #select difficulty
    difficulty = input("Select your difficulty: 'easy' or 'hard':  ").lower()
    if difficulty == 'easy':
        lives_left = 10
        print(f"You will start with {lives_left} lives. ")
    elif difficulty == 'hard':
        lives_left = 5
        print(f"You will start with {lives_left} lives. ")
    else:
        print("You have provided an invalid response.")
        number_guesser()
    #begin game
    while lives_left > 0:
        user_guess = int(input("Guess a number between 1 and 100:  "))
        if user_guess > correct_answer: #too high
            lives_left -= 1
            print(f"Too High... You have {lives_left} guesses left.")
        elif user_guess < correct_answer: #too low
            lives_left -= 1
            print(f"Too Low... You have {lives_left} guesses left.")

        else: #correct, new game???
            new_game = input(f"Correct! The correct guess was {correct_answer}! You had {lives_left} lives left. Would you like to go again? 'yes' or 'no':  ").lower()
            if new_game == 'yes':
                number_guesser()
            else:
                print("Thank you for playing!")
                break

    try_again = input(f"You are out of lives the correct answer was {correct_answer}, would you like to try again? 'yes' or 'no':  ").lower()
    if try_again == 'yes':
        number_guesser()
    elif try_again == 'no':
        print("Thank you for playing!")
        lives_left = 0


number_guesser()
