from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        """
        Define the header of the PDF.
        This includes the shirt image and the title text.
        """
        # Add the shirt image to the PDF
        self.image("./shirtificate.png", x=10, y=70, w=190)

        # Set font for the header text
        self.set_font("helvetica", size=48)

        # Add the title text, centered
        self.cell(0, 57, "CS50 Shirtificate", align="C")

        # Add a line break after the header
        self.ln(20)

def main():
    """
    Main function to prompt the user for their name and generate the shirtificate PDF.
    """
    # Prompt the user for their name
    name = input("Name: ")

    # Create the shirtificate PDF with the provided name
    shirt(name)

def shirt(s):
    """
    Create a shirtificate PDF with the user's name.

    Parameters:
    - s (str): The name to be added to the shirtificate.
    """
    # Create a PDF instance
    pdf = PDF()

    # Add a new page with portrait orientation and A4 format
    pdf.add_page(orientation="portrait", format="a4")

    # Set font for the name text
    pdf.set_font("helvetica", size=24)

    # Set text color to white
    pdf.set_text_color(255, 255, 255)

    # Add the user's name text on top of the shirt image, centered
    pdf.cell(0, 213, f"{s} took CS50", align="C")

    # Save the PDF to a file named 'shirtificate.pdf'
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    # Execute the main function if the script is run directly
    main()
