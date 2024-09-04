import validators

def main():
    """
    Main function to prompt the user for their email address and
    validate it using the validate function.
    """
    # Prompt the user for their email address
    email = input("What's your email address? ")
    # Print whether the email address is valid or not
    print(validate(email))

def validate(s):
    """
    Validate the given email address using the validators library.

    Parameters:
    s (str): The email address to validate.

    Returns:
    str: "Valid" if the email address is valid, otherwise "Invalid".
    """
    # Check if the provided email address is valid
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
