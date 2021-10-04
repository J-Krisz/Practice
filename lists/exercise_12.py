# Write a function, most_repeating_word(), that takes a sequence of strings as
# input. The function dhould return the string that contains the greatest
# number of repeated letters. In other words...

    # For each word, find the letter thet appears the most times.
    # Find the word whose most-repeated letter appears more than any other.

# That is if words is set to 

WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']

# then your function should return 'elementary'. That's because
    
    # this has no repeating letters.
    # is has no repeating letters.
    # an hads no repeating letters.
    # elementary has one repeating lette, e, which appears thress times.
    # test has one repeating letter, r, which appears twice.
    # example has one repeatinh letter, e, which appears twice.

# So the most common letter in elementary eppears more often than the most
# common letters in any of the other words. (If it's a tie, then any or the
# appropriate words can be returned.)
# You'll probably want to use Counter(), form the collenctions module, which is
# perfect for counting the number of items in a sequence.

from collections import Counter

def most_freq_letter(word):
    return Coutner(word).most_common(1)[0][1]

def word_with_most_rep_letter(words):

