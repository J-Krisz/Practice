#############
# Pig Latin #
#############

# Handle apitalized words -- If a word is capitalized (i.e. the first letter is
# capitalized, but the rest of the word isn't), then the Pig Latin translation
# should be similarly capitalized.


def translator():

    word = input("Enter the word you wish to translate : ")
    
    if word[0] in "aeiou":
        trans_word = f"{word}way"
    else:
        trans_word = f"{word[1:]}{word[0]}ay"


    if word[0].isupper():
        return trans_word.capitalize()

    return trans_word


print(translator())
