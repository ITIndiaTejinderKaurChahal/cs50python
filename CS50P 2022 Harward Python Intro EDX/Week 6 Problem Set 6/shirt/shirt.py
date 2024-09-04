#type on terminal to test: python shirt.py before1.jpg after1.jpg


# from PIL import Image, ImageOps
import sys
import os

def main():
    """
    Main function to handle command-line arguments and call the `edit_photo` function.
    """
    # Check the number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments. Please provide both input and output filenames.")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments. Please provide exactly two filenames.")

    # Define acceptable image formats
    valid_formats = [".jpg", ".jpeg", ".png"]

    # Extract file extensions
    input_ext = os.path.splitext(sys.argv[1])[1].lower()
    output_ext = os.path.splitext(sys.argv[2])[1].lower()

    # Validate the output file extension
    if output_ext not in valid_formats:
        sys.exit("Invalid output file format. Supported formats are: .jpg, .jpeg, .png.")

    # Check if input and output file extensions match
    if input_ext != output_ext:
        sys.exit("Input and output file extensions do not match. Please ensure they have the same extension.")

    # Process the image
    edit_photo(sys.argv[1], sys.argv[2])

def edit_photo(input_file, output_file):
    """
    Edit the input image by overlaying it with a shirt image and save the result.

    Args:
        input_file (str): The path to the input image file.
        output_file (str): The path where the edited image will be saved.

    Raises:
        SystemExit: If the input file does not exist or cannot be processed.
    """
    try:
        # Load the shirt image
        shirt = Image.open("shirt.png")

        # Open and process the input image
        with Image.open(input_file) as img:
            # Resize and crop the input image to match the shirt's size
            img_cropped = ImageOps.fit(img, shirt.size)

            # Overlay the shirt image onto the cropped input image
            img_cropped.paste(shirt, mask=shirt)

            # Save the edited image to the output file
            img_cropped.save(output_file)

    except FileNotFoundError:
        sys.exit(f"Input file '{input_file}' does not exist. Please check the file path and try again.")
    except Exception as e:
        sys.exit(f"An error occurred while processing the image: {e}")

if __name__ == "__main__":
    main()
