###########
# Strings #
###########


# Consider a few other variations of, and extensions to, this excercise, which
# also use str.split() and str.join() as well as sorted:

# ~ Given the string "Tom Dick Harry" break it into individual words, and then
# sort those words alphabetically. Once they're sorted, print them with commas
# (,) between the names.

# ~ Which is the last word, alphabetically, in a text file?

# ~ Which is the longest word in a text file?

def comma_separate(string):
    return ", ".join(sorted(string.split()))

def last_word(string):
    pass

def longest(string):
    pass

