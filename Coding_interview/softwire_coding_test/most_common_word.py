# Find commonly reocurring word in two strings

from string import punctuation

def common_words(string1, string2):

    first = set([word.strip(punctuation) for word in string1.split()])
    second = set([word.strip(punctuation) for word in string2.split()])

    return first.intersection(second)

one = 'This is a great tasting pizza.'
two = ' The pizza is great!'

print(common_words(one, two))
