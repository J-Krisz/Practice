def pig_latin():
    
    """
    translate word to pig latin

    :return: translation to pig latin
    """

    
    word = input("Enter a word you'd like translated: ")
    vowels = ["a,", "e", "i", "o", "u"]
    
    translated_word = ""

    if word[0] in vowels:
        return f"{word}way"
    else:
        return f"{word[1:]}{word[0]}ay"


print(pig_latin())
