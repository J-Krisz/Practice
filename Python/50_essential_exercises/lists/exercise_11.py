# Write a function, alphabetize_names() that assumes the existence of a POPLE
# constant defined as shown in the code. The function should return the list of
# dicts, but sorted by last name and then by first name.

## NOTE Python doesn't have constants; with the exception of some intenal types
## and data structures, every veriable, function and attribute can always be
## modified. That said, variables defined outside of any function are generally
## referred ro as "constant" and are defined in ALL CAPS.

# You can solve this excercise several ways, but all will require using the
# sorted() method that you saw in the last chapter, along with a function
# passed as an argument to its key parameter. One of the options for solving
# this excercise involves operator.itemgetter()


PEOPLE = [
{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.li'},
{'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
{'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'}
]

def change_key_order(contact_book):
    return [contact_book['last'], contact_book['first']]

def alphabetize_names(people):
    return sorted(people, key=change_key_order)

print(alphabetize_names(PEOPLE))


