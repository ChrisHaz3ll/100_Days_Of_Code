from os import makedev
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker() #calling Class
money_machine = MoneyMachine() #calling Class
menu = Menu() #calling Class
drinks_available = menu.get_items()

coffee_loop = True
while coffee_loop:
    #request user input
    user_input = input(f"What coffee would you like? {drinks_available}:  ").lower()
    drink_choice = menu.find_drink(user_input) #returns MenuItem object with details of drink (e.g. returns latte and associated ingredients/cost)

    if user_input == 'off': # if input is off, turn machine off
        print("Turning machine off...")
        coffee_loop = False
    elif user_input == 'report': # print report if input is "report"
        print(coffee_machine.report())
        print(money_machine.report())
    else:
        process_order = coffee_machine.is_resource_sufficient(drink_choice) #check resources are sufficient
        take_payment = money_machine.make_payment(drink_choice.cost) #process payment

        if process_order:
            payment = take_payment
            if payment:
                coffee_machine.make_coffee(drink_choice) #makes coffee, deducts resources
