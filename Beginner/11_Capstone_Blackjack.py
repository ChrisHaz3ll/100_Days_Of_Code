import random
# from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#start a new game
def new_game():
    start = input("Would you like to play Blackjack? 'y' or 'n':  ").lower()
    if start == 'y':
        game = True
        # print(logo)
    elif start == 'n':
        game = False
        new_game()
    else:
        print("You have typed an invalid response.")


def hit_or_stand():
    hit_stand = input("Would you like to 'hit', or 'stand'?:  ").lower()
    if hit_stand == "stand":
        print(f"Your cards were: {player_cards}, with a score: {sum(player_cards)}")
        print(f"Computer's cards were: {computer_cards}, with a score of {sum(computer_cards)}")

        #checking the scores to see who wins
        who_wins()

    # "draw" another card, add to player and computer list
    elif hit_stand == "hit":
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        print(f"Your cards are: {player_cards}, with a score: {sum(player_cards)}")
        bust_check()
        print(f"Computer's first card is: {computer_cards[0]}")
        hit_or_stand()


#function to see who wins
def who_wins():
    if sum(computer_cards) > 21:
        print("You Win!!!")
        game = False
    elif (sum(player_cards) > sum(computer_cards)) and sum(player_cards) <= 21:
        print("You Win!!!")
        game = False
    elif sum(player_cards) == sum(computer_cards) and sum(player_cards) <= 21:
        print("You Draw")
        game = False
    else:
        print("Sorry, you lose.")
        game = False


#check the score after drawing a card to see if player is bust
def bust_check():
    if sum(player_cards) > 21:
        print(f"You are bust! You Lose!")
        new_game()


#start with empty list
player_cards = []
computer_cards = []


#The Game Loop
game = True
while game:
    new_game()
    #assign two random cards
    player_cards = random.sample(cards, 2)
    computer_cards = random.sample(cards, 2)
    #show both player cards and first computer card
    print(f"Your cards: {player_cards}, score: {sum(player_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    #would you like to hit or stand???
    hit_or_stand()






