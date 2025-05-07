# tuples : collection of values
# tuples are denoted by ()
# tuples are immutable / unchangeable
# tuples have only two methods in python (index, count)
# tuples can be accessed by indexing
# tuples are ordered

mark = (17, 30, 50, 3, 67, 30, 30)

# print(type(mark))
# mark[0] = 50
# print(mark)

# two methods in tuple : 

# print(mark.count(30))

# print(mark.index(50))

# what if I want to manipulate tuple?
# to modify / manipulate tuples, we can convert them into lists!

# print(mark)

# mark is current tuple, and we want to convert it into list
mark_list = list(mark)

mark_list[0] = 100
mark_list.pop()
mark_list.pop()
# print(type(mark_list))

# after modifying, we will convert our list back into tuple!

mark = tuple(mark_list)

print(mark)