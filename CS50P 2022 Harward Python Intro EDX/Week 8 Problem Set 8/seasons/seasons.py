from datetime import date
import inflect
import sys
import operator

def main():
    try:
        dob = input("Date of Birth (YYYY-MM-DD): ")
        # Validate and parse the date
        birth_date = date.fromisoformat(dob)
        today = date.today()
        difference = operator.sub(today, birth_date)
        print(convert(difference.days))
    except ValueError:
        sys.exit("Invalid date format. Please enter the date in YYYY-MM-DD format.")

def convert(days):
    minutes = days * 24 * 60
    p = inflect.engine()
    # Convert number to words
    words = p.number_to_words(minutes, andword='')

    # Format the string
    words = words.replace(", and", " and").replace(", zero", "")  # Adjust commas and "and" placement
    words = words.replace(", zero", "")  # Remove trailing ", zero" if present

    # Capitalize the first letter and add " minutes" at the end
    return f"{words.capitalize()} minutes"

if __name__ == "__main__":
    main()
