
import emoji

def main():
    # Prompt user for input
    user_input = input("Input: ")

    # Convert emoji codes to actual emojis
    emojized_text = emoji.emojize(user_input, language='alias')  #emoji.emojize : emojize function provided by emoji import
                                                                 #language='alias' : parameter so function recognizes std emoji codes &  aliases i.e., :thumbsup:

    # Output the emojized text
    print(emojized_text)

if __name__ == "__main__":
    main()
