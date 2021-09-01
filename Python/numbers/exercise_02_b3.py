###################
# Summing numbers #
###################

# Write a function that takes alist of words (strings). It should return a tuple
# containing three integers, representing the length  of the shortest word the
# length of th longest word, and average word length.

def words_data(words):

    word_length = [len(word) for word in words]

    return max(word_length), min(word_length), sum(word_length)/len(word_lenght)

print(words_data())
