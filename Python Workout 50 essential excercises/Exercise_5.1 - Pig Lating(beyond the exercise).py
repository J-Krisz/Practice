# TODO Handle capitalized words. The translation should be capitalized if the
# original word is capitalized

def pig_latin(word):

    if word[0].isupper():
        if word[0] in "aeiou":
            return f"{word.capitalize()}way"
        else:
            return f"{word[1:].capitalize()}{word[0].lower()}ay"
    else:
        if word[0] in "aeiou":
            return f"{word}way"
        else:
            return f"{word[1:]}{word[0]}ay"

if __name__ == "__main__":

    inp = input("Enter your word: ")
    print(pig_latin(inp))
