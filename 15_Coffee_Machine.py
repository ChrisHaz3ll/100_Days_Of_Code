# from symbol import continue_stmt

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


total_money = 0.00


# TODO: Check resources sufficient when ordering drink
# define function to evaluate choice and check resources:
def process_order(user_input, coffee_resources):
    """Returns True when order can be made... False if it can't"""
    drink = MENU[user_input]["ingredients"]
    for ingredient in drink:
        if drink[ingredient] > coffee_resources[ingredient]:
            print(f"There is not enough {ingredient} for a {user_input}")
            return False
    print(f"The price is ${'{0:,.2f}'.format(MENU[user_input]['cost'])}.")
    return True


# TODO: Process Coins
# TODO: Check transaction successful (ie enough coins)
def process_coins():
    """Returns total"""
    print("Please enter your coins. ")
    quarters = int(input("How many quarters?:  ")) * 0.25
    dimes = int(input("How many dimes?:  ")) * 0.10
    nickels = int(input("How many nickels?:  ")) * 0.05
    pennies = int(input("How many pennies?:  ")) * 0.01
    total = [quarters, dimes, nickels, pennies]
    return sum(total)


def transaction_successful(money_received, user_input):
    """return True when payment accepted... otherwise False"""
    global total_money
    if money_received >= user_input:
        total_money += money_received
        leftover_change = money_received - user_input
        if leftover_change > 0:
            print(f"Here is ${'{0:,.2f}'.format(leftover_change)} in change")
            total_money -= leftover_change
        return True
    else:
        amount_short = user_input - money_received
        print(f"You are ${'{0:,.2f}'.format(amount_short)} short. You have been refunded.")
        return False

# TODO: Deduct resources from dictionary
def resources_left(resources_available, user_input):
    drink = MENU[user_input]["ingredients"]
    for ingredient in resources_available:
        resources_available[ingredient] -= drink[ingredient]




def coffee_loop():
    coffee_machine = True
    while True:
        # TODO: Ask user what would you like?
        coffee_choice = input("What would you like? espresso/latte/cappuccino:  ").lower()
        # TODO: Turn coffee off by entering "off" to prompt:
        if coffee_choice == "off":
            print("Turning off the coffee machine...")
            break
        elif coffee_choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money Made: ${'{0:,.2f}'.format(total_money)}")
        else:
            drink = MENU[coffee_choice]
            if process_order(coffee_choice, resources): #can the order be made?
                payment = process_coins() #store payment value
                if transaction_successful(payment, drink['cost']):
                    print(f"Here is your {coffee_choice}! Enjoy!")
                    resources_left(resources, coffee_choice)

        # TODO: Print Report: Generate resource values and money made


coffee_loop()







