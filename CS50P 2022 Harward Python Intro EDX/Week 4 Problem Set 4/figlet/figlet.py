#use pip install pyfiglet for module installation before running program

#to handle command-line arguments + exit the program
import sys

#to choose a random font if no specific font is provided
import random

#import Figlet class
from pyfiglet import Figlet

def main():
    # Initialize the Figlet object
    figlet = Figlet()

    # Check the number of command-line arguments
    if len(sys.argv) == 1:
        # No font specified, use a random font
        font = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3:
        # Check if -f or --font is provided
        if sys.argv[1] in ('-f', '--font'):
            font = sys.argv[2]
            # Check if the font is valid
            if font not in figlet.getFonts():
                print(f"Error: Font '{font}' not found.")
                sys.exit(1)
        else:
            print("Error: Invalid argument. Use -f or --font to specify a font")
            sys.exit(1)
    else:
        print("Error: Invalid number of arguments")
        sys.exit(1)                                 #exits program with a non-zero status code indicating an error

    # Set the chosen font
    figlet.setFont(font=font)

    # Prompt the user for text
    text = input("Input: ")

    # Render and print the text in the chosen font
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
