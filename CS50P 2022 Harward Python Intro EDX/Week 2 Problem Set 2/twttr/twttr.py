def main():
    vowels = ["a","e", "i", "o", "u" , "A" , "E", "I" , "O", "U"]
    raw_sentence = input("Enter your sentence")
    final_sentence_twttr = final_sentence(raw_sentence, vowels)
    print(final_sentence_twttr)


def final_sentence(raw_sentence, vowels):
    for vowel in vowels:
             raw_sentence = raw_sentence.replace(vowel,"")
    return (raw_sentence)



main()
