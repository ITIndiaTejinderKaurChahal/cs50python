import csv
import sys
from tabulate import tabulate

def main():
    """
    Main function to handle command-line arguments and process the CSV file.
    """
    # Check the number of command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments. Please provide a CSV filename.")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments. Only one CSV filename is allowed.")

    # Validate the file extension
    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("The file does not have a .csv extension. Please provide a CSV file.")

    # Print the tabulated content of the CSV file
    print(tabulize(filename))

def tabulize(file):
    """
    Read a CSV file and return its contents formatted as a table.

    Args:
        file (str): The path to the CSV file to be read.

    Returns:
        str: The CSV content formatted as a table using the tabulate library.

    Raises:
        SystemExit: If the file is not found.
    """
    try:
        # Open the CSV file and create a reader object
        with open(file, newline='') as f:
            reader = csv.reader(f)
            # Convert the CSV data to a table format
            table = tabulate(reader, headers="firstrow", tablefmt="grid")
            return table

    except FileNotFoundError:
        sys.exit("File does not exist. Please check the file path and try again.")

if __name__ == "__main__":
    main()
