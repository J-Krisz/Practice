#############
# Pig latin #
#############

# For this exercise, write a Python function pig_lating() that takes a string
# as input, assumed to be an English word. The function should return the
# translation of this word into Pig Latin. You may assume that the word
# contains no capital letters or punctutation.j

def pig_latin():
    word = input("Choose a word to translate ")

    if word[0] in "aeiou":
        return f"{word}way"
    else:
        return f"{word[1:]}{word[0]}ay"

print(pig_latin())
