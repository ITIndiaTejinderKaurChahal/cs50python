import csv
import sys

def main():
    """
    Main function to handle command-line arguments and call the `clean` function.
    """
    # Check the number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments. Please provide both input and output filenames.")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments. Please provide exactly two filenames.")

    # Validate the input file extension
    input_file = sys.argv[1]
    if not input_file.endswith(".csv"):
        sys.exit("The input file does not have a .csv extension. Please provide a CSV file.")

    # Get the output file name
    output_file = sys.argv[2]

    # Call the clean function to process the CSV file
    clean(input_file, output_file)

def clean(input_file, output_file):
    """
    Read a CSV file, clean and reformat its contents, and write the result to a new CSV file.

    Args:
        input_file (str): The path to the input CSV file.
        output_file (str): The path to the output CSV file where the cleaned data will be saved.

    Raises:
        SystemExit: If the input file is not found or cannot be read.
    """
    try:
        # Open the input CSV file for reading
        with open(input_file, mode='r', newline='') as infile:
            reader = csv.DictReader(infile)

            # Open the output CSV file for writing
            with open(output_file, mode='w', newline='') as outfile:
                # Define the header for the output CSV file
                header = ["first", "last", "house"]
                writer = csv.DictWriter(outfile, fieldnames=header)

                # Write the header row to the output file
                writer.writeheader()

                # Process each row in the input CSV file
                for student in reader:
                    # Split the "name" field into "last" and "first" names
                    last, first = student["name"].split(", ")
                    # Get the "house" field
                    house = student["house"]
                    # Write the cleaned data to the output CSV file
                    writer.writerow({"first": first, "last": last, "house": house})

    except FileNotFoundError:
        sys.exit(f"Could not read the file: {input_file}. Please ensure the file exists and try again.")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
