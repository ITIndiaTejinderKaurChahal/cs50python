menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

price = 0

while True:
        try:
            food = input("Item: ").title() #user input of food choice in order # No need to check if item in foods. KeyError is handled separately.
            price = price + menu[food]
            print(f"Total: ${price:.2f}")  # round off float to 2 decimal

        except EOFError:  # manage control plus D to stop further input and exit
            print()
            break
        
        except KeyError:  # if user input(key) not found in menu dictionary
            pass


  # for food in menu:    #take user input and compare in menu
