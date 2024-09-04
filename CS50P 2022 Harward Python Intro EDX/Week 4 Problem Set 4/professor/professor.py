import random

def main():
    # Get the level from the user
    level = get_level()

    # Initialize score counter
    score = 0

    # Generate and evaluate 10 math problems
    for _ in range(10):
        # Generate the problem components
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        # Prompt user for an answer
        tries = 0
        while tries < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_answer:
                    print("Correct!")
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")

            tries += 1

        # If still incorrect after 3 tries, display the correct answer
        if tries == 3 and user_answer != correct_answer:
            print(f"The correct answer was {correct_answer}.")

    # Output the final score
    print(f"Your score: {score} out of 10")

def get_level():
    while True:
        try:
            level = int(input("Enter the level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Invalid level. Level must be 1, 2, or 3.")
    digits = level
    return random.randint(0, 10**digits - 1)

if __name__ == "__main__":
    main()
