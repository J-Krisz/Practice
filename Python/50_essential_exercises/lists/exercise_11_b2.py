# Given a list of strings, sort them according to how many vowels they contain.



def count_vowels(word):
    return sum(char in 'aeiou' for char in word)


def sort_by_vowels(word_list):
    return sorted(word_list, key=count_vowels, reverse=True)


