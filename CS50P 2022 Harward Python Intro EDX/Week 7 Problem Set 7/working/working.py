import re

def main():
    """
    Prompts the user to input a time range in 12-hour format and prints
    the converted time range in 24-hour format.
    """
    # Prompt the user to input a time range
    time_input = input("Hours: ")
    # Convert and print the time range in 24-hour format
    print(convert(time_input))

def convert(s):
    """
    Converts a time range in 12-hour format to 24-hour format.

    Args:
        s (str): A string representing a time range in 12-hour format.

    Returns:
        str: The time range in 24-hour format, or raises a ValueError if the input is invalid.
    """
    # Regular expression pattern for matching 12-hour time format
    regex = "(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"
    # Search for the time range pattern in the input string
    match = re.search(r"^" + regex + " to " + regex + "$", s)

    if match:
        # Extract the start and end times from the matched groups
        from_time = standardize(match.group(1), match.group(2), match.group(3))
        to_time = standardize(match.group(4), match.group(5), match.group(6))
        # Return the formatted time range in 24-hour format
        return f"{from_time} to {to_time}"
    else:
        # Raise ValueError if the input does not match the expected format
        raise ValueError("Invalid time format")

def standardize(hr, min, period):
    """
    Converts a single time from 12-hour format to 24-hour format.

    Args:
        hr (str): The hour part of the time in 12-hour format.
        min (str or None): The minute part of the time in 12-hour format, or None if not provided.
        period (str): The AM/PM period.

    Returns:
        str: The time in 24-hour format.
    """
    # Convert the hour based on the AM/PM period
    if hr == "12":
        # Special case for 12 AM and 12 PM
        if period == "AM":
            hour = "00"
        else:
            hour = "12"
    else:
        # Convert hour for AM/PM cases
        if period == "AM":
            hour = f"{int(hr):02}"
        else:
            hour = f"{int(hr)+12:02}"

    # Handle minutes
    if min is None:
        minute = "00"
    else:
        minute = f"{int(min):02}"

    # Return the time in 24-hour format
    return f"{hour}:{minute}"

if __name__ == "__main__":
    # Execute the main function only if this script is run directly
    main()
