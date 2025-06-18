
#add, subtract, multiply, divide functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#add functions to dictionary, as values... keys = + - * /
operations = {
    "+": add, #don't use () when storing a function, adding () would call it...
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#use dictionary operations to perform calculations... try out multiply, 4 by 8, using dictionary
# print(operations["*"](4, 8))

#CALCULATOR
# from art import logo
# print(logo)
def calculator():
    continue_calc = True
    n1 = float(input("Type your first number:  "))
    while continue_calc:
        operator = input("What operator would you like to use: +  -  *  /:  ")
        n2 = float(input("Type your second number:  "))
        answer = operations[operator](n1, n2)
        print(f"Your result is: {answer}")
        again = input("Would you like to continue working with calculated answer? 'y' or 'n':  ").lower()
        if again == "y":
            n1 = answer
        else:
            continue_calc = False
            print("\n" * 20)
            calculator()

calculator()



