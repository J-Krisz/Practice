#############
# Pig Latin #
#############

# If words end with punctuation, then that punctuation should be shifted to the
# end of the translated word
import string

def shift_punct():
    
    punct = ""
    word = input("Enter a word : ")

    if word[-1] in string.punctuation:
        punct = word[-1]
        stripped_word = word[:-1]

    if stripped_word[0].lower() in "aeiou":
        outp = f"{stripped_word}way"
    else:
        outp = f"{stripped_word[1:]}{stripped_word[0]}ay"

    return outp + punct


print(shift_punct())

