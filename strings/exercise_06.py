######################
# Pig Latin Sentence #
######################

# Write a function pl_sentence() that takes a string containing several words,
# separated by spaces. (To make things easier, we won't actually ask for a real
# sesntence. More specifically, there will be no capital letters or
# punctuation.)


def pl_sentence(sentence):

    return " ".join([pig_latin(word) for word in sentence.split()])



def pig_latin(word):

    if word[0] in "aeiou":
        return f"{word}way"
    else:
        return f"{word[1:]}{word[0]}ay"

print(pl_sentence("this is just a test"))
