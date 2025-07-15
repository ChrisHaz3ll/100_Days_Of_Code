import random
from hangman_words import word_list # TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_art import stages
from hangman_art import logo # TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

lives = 6

print(logo)

chosen_word = random.choice(word_list) #select random word

placeholder = ""
placeholder += ("_" * len(chosen_word))
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")     # TODO-6: - Update the code below to tell the user how many lives they have left.
    guess = input("Guess a letter: ").lower()

    display = ""
    if guess in correct_letters:     # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
        print("You've already guessed this letter!")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)

    if guess not in chosen_word:     # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}. That's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE, THE WORD WAS {chosen_word}**********************")             # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
