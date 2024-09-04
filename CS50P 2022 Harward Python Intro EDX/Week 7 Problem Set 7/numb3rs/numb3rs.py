import re

def main():
    """
    Main function to prompt the user for an IPv4 address and validate it.
    """
    # Prompt the user for an IPv4 address
    ip = input("IPv4 Address: ")

    # Validate the IPv4 address and print the result
    print(validate(ip))

def validate(ip):
    """
    Validate an IPv4 address using a regular expression.

    Parameters:
    - ip (str): The IPv4 address to validate.

    Returns:
    - bool: True if the IP address is valid, False otherwise.
    """
    # Regular expression for validating IPv4 address
    # Breakdown:
    # - ([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)
    #   This matches a number from 0 to 255.
    # - The IP address consists of four octets separated by dots.
    regex = "([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)"

    # Combine the regex for all four octets with dots in between
    pattern = r"^" + regex + "\." + regex + "\." + regex + "\." + regex + "$"

    # Search for a match using the regular expression
    match = re.search(pattern, ip)

    # Return True if a match is found, otherwise return False
    return bool(match)

if __name__ == "__main__":
    # Execute the main function if the script is run directly
    main()
