import re

def main():
    """
    Prompts the user for an HTML string and prints the extracted YouTube link if present.
    """
    # Prompt user for HTML input
    html_input = input("HTML: ")
    # Parse the HTML input to extract and convert the YouTube link
    print(parse(html_input))

def parse(s):
    """
    Parses the provided HTML string to find a YouTube iframe embed link and
    converts it to a shortened YouTube URL.

    Args:
        s (str): The HTML string containing the iframe element.

    Returns:
        str or None: The shortened YouTube URL if an iframe is found; otherwise, None.
    """
    # Regular expression pattern to match YouTube iframe embed URLs
    pattern = r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>"

    # Search for the pattern in the provided HTML string
    match = re.search(pattern, s)

    if match:
        # If a match is found, construct the shortened YouTube URL
        return f"https://youtu.be/{match.group(2)}"
    else:
        # Return None if no valid iframe is found
        return None

if __name__ == "__main__":
    # Execute the main function only if this script is run directly
    main()
