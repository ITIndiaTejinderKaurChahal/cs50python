import sys

def main():
    # Check the number of command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments. Please provide a filename.")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments. Only one filename is allowed.")

    # Validate the file extension
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("The file does not have a .py extension. Please provide a Python file.")

    # Print the number of non-empty, non-comment lines
    print(count_lines(filename))

def count_lines(file):
    """
    Count the number of non-empty, non-comment lines in the given file.

    Args:
        file (str): The path to the file to be read.

    Returns:
        int: The count of non-empty, non-comment lines.

    Raises:
        SystemExit: If the file is not found.
    """
    try:
        # Initialize line counter
        counter = 0

        # Open the file and count lines
        with open(file, "r") as f:
            for line in f:
                # Check if the line is not empty and does not start with a comment
                if not (line.lstrip().startswith("#") or line.strip() == ""):
                    counter += 1

        return counter

    except FileNotFoundError:
        sys.exit("File does not exist. Please check the file path and try again.")

if __name__ == "__main__":
    main()
