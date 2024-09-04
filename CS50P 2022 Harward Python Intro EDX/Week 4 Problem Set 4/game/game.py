#module to generate random numbers.
import random

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    # Prompt the user for the level
    level = get_positive_integer("Enter the level (positive integer): ")

    # Generate a random number between 1 and the level
    target_number = random.randint(1, level)

    print(f"Guess the number between 1 and {level}.")

    while True:
        guess = get_positive_integer("Your guess: ")

        if guess < target_number:
            print("Too small!")
        elif guess > target_number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
