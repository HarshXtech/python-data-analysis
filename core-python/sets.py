# set : collection of unique values
# sets are unordered
# sets are immutable / unchangeable
# sets can not be accessed by indexing
# sets are denoted by {}
# It will not allow duplicate or repeated values!


language = {"Python", "Javascript", "Java", "c", "c++", "Python", "Javascript"}
frameworks = {"Django", "springboot", "laravel", "Python", "Javascript"}

# language[0] = "HTML"
# print(language)

# methods of sets

# add : to add an element
# language.add('PHP')
# print(language)

# remove  : to remove element
# language.remove('CSS')
# print(language)

# language.discard('CSS')
# print(language)

# remove and discard 

# if element is not available in set, remove method will throw an error
# if element is not available in set, discard method will not throw an error and return complete set


# pop : will remove random element!
# language.pop()
# print(language)

# union method is used to merge two or more sets.
# x = language.union(frameworks)
# print(x)

# intersection : gives common element present in both sets
# x = language.intersection(frameworks)
# print(x)