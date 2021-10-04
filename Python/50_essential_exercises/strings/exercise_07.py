##############
# Ubbi Dubbi #
##############

# For this exercise write a function called ubbi_dubbi() that takes a single
# word (string) as an argument. It returns a string, the word's translationinto
# Ubbi Dubbi. So if the function is called with "octopus" the function
# will return the string uboctubopubus. And if the user passes the argument
# elelpant, you'll output ubelubephubant

def ubbi_dubbi(word):

    translated_word = []
    for char in word:
        if char in "aeiou":
            translated_word.append(f"ub{char}")
        else:
            translated_word.append(char)

    return "".join(translated_word)

print(ubbi_dubbi("octopus"))
