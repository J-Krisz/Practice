##########################
# Printing tuple records #
##########################

# Acommon use for typles is as records, similar to a struct in some other
# languages. And of course, displaying thise records in a table is a standerd
# thing for programs to do. In this exercise, we'll do a bit of both--reading
# from a list of tuples and turning them into formattd output for hte user.
# For example, assume we're in charge of an international summit in London. We
# know how many hours it'll take each of seceral world leaders to arrive:

PEOPLE = [('Donald', 'Trump', 7.85),
        ('Vladimir', 'Putin', 3.626),
        ('Jinping', 'Xi', 10.603)]

# The planner for this summit needs to have alist of theworld leaders who are
# coming, aling with thetime it'll take for them to arrive. However, this
# travel planner doesn't need the degree of trecision that the computer has
# provided; it's enough for us to have two digits after the decimal point.
# for this exercise, write a Pythin function, format_sort_records(), that takes
# hte PEOPLE list and returns a formatted string that looks like the following:

    # Trump     Donald      7.85
    # Putin     Vladimir    3.63
    # Xi        Jinping     10.60

# Notice that the alst name is printed before the first name (taking into
# account that Chinese names are generally shwn that way), followed by a
# decimal-aligned indication of how long it'll take for each leader to arrive
# in London. Each name should be printed in a 10-character field, and the time
# should be printed in a 5-character field, with one space character of padding
# between each of the columns. Travel time should display only teo digits after
# the decimal point, which means that even though the inpyt for Xi Jinping's
# flight is 10.603 hours, the value displayed should be 10.60.


def format_data(tup_list):
    pass

