#pip install inflect module for generating grammatically correct phrases

import sys
import inflect

def main():
    # Create an inflect engine instance
    p = inflect.engine()

    # Empty List to store names
    names = []

    print("Enter names, one per line (Ctrl-D to finish):")

    # Read names from user input until EOF (Ctrl-D)
    while True:
        try:
            name = input().strip()
            if name:
                names.append(name)
        except EOFError:              #End-of-File Error: user inputs Ctrl-D or when Python reached end of user input without receiving any input
            break

    # Format the names list into a grammatically correct string
    farewell_message = f"Adieu, adieu, to {p.join(names)}"

    # Print the farewell message
    print(farewell_message)

if __name__ == "__main__":
    main()
