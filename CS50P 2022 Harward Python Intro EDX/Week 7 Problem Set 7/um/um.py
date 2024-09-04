import re

def main():
    """
    Prompts the user for input and prints the count of occurrences
    of the substring "um" that are surrounded by non-alphanumeric characters.
    """
    # Prompt user for input text
    user_input = input("Text: ")
    # Print the count of occurrences of "um" that match the criteria
    print(count(user_input))

def count(s):
    """
    Counts the number of occurrences of the substring "um" in the input string
    where "um" is either at the beginning or end of the string, or surrounded
    by non-alphanumeric characters.

    Parameters:
    s (str): The input string to search.

    Returns:
    int: The count of valid occurrences of "um".
    """
    # Define a regular expression pattern to match "um"
    # - ^|\W: Matches "um" at the beginning of the string or after a non-alphanumeric character
    # - um: The literal substring to match
    # - $|\W: Matches "um" at the end of the string or before a non-alphanumeric character
    regex = r"(?:^|\W)um(?:$|\W)"

    # Find all occurrences of the pattern in the input string, case-insensitively
    match = re.findall(regex, s, re.IGNORECASE)

    # Return the number of matches
    return len(match)

if __name__ == "__main__":
    # Run the main function if this script is executed
    main()
